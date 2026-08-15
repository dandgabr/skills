import os
import sys
import argparse
import subprocess
import ctypes
from ctypes import wintypes

# Define basic structures and GUIDs for dbgeng.dll COM interface
class GUID(ctypes.Structure):
    _fields_ = [
        ("Data1", ctypes.c_ulong),
        ("Data2", ctypes.c_ushort),
        ("Data3", ctypes.c_ushort),
        ("Data4", ctypes.c_byte * 8)
    ]

    def __init__(self, l, w1, w2, b1, b2, b3, b4, b5, b6, b7, b8):
        self.Data1 = l
        self.Data2 = w1
        self.Data3 = w2
        self.Data4 = (ctypes.c_byte * 8)(b1, b2, b3, b4, b5, b6, b7, b8)

# Interface GUIDs
IID_IDebugClient = GUID(0x27fe5639, 0x840f, 0x4f47, 0x83, 0x44, 0x00, 0xca, 0x14, 0x16, 0x8a, 0x8e)
IID_IDebugControl = GUID(0x518201c3, 0x8f65, 0x4f3a, 0x9c, 0x93, 0xd0, 0x44, 0xbe, 0x03, 0x3f, 0x5d)

class DbgEngDebugger:
    """Wrapper to interact with dbgeng.dll directly using COM Interfaces."""
    def __init__(self):
        self.dbgeng = None
        self.client = None
        self.control = None
        self._load_dbgeng()

    def _load_dbgeng(self):
        try:
            # Load the system dbgeng.dll
            self.dbgeng = ctypes.windll.LoadLibrary("dbgeng.dll")
            
            # Set up DebugCreate prototype
            self.dbgeng.DebugCreate.argtypes = [ctypes.POINTER(GUID), ctypes.POINTER(ctypes.c_void_p)]
            self.dbgeng.DebugCreate.restype = ctypes.c_long

            # Create IDebugClient
            client_ptr = ctypes.c_void_p()
            hr = self.dbgeng.DebugCreate(ctypes.byref(IID_IDebugClient), ctypes.byref(client_ptr))
            if hr < 0:
                raise Exception(f"DebugCreate failed with HRESULT: {hr:X}")
            self.client = client_ptr

            # Query IDebugControl interface
            # The COM QueryInterface method is the 0th vtable index for IUnknown
            # vtptr -> [QueryInterface, AddRef, Release, ...]
            # We will use ctypes to call the virtual function.
            # However, mapping the full COM vtable in pure Python ctypes is notoriously verbose.
            # Instead, we instantiate a fallback interface or query control via Ctypes COM wrapper helpers.
        except Exception as e:
            self.dbgeng = None
            # print(f"[DbgEng] Direct DLL loading failed/not fully supported: {e}")

    def execute_command_native(self, dump_path, pid, exec_path, command):
        """Native COM implementation (stub/placeholder for direct COM if desired, otherwise delegates to cdb)."""
        if not self.dbgeng:
            return None
        # We fall back to the CLI wrapper for complex scenarios to guarantee maximum compatibility
        return None

class CdbDebugger:
    """Invokes cdbX64.exe or cdb.exe to execute commands in a subprocess."""
    def __init__(self):
        self.cdb_path = self._find_cdb()

    def _find_cdb(self):
        # Look in standard WindowsApps folders first (for WinDbg Preview store installs)
        user_profile = os.environ.get("USERPROFILE", "")
        windows_apps = os.path.join(user_profile, "AppData", "Local", "Microsoft", "WindowsApps")
        
        candidates = [
            os.path.join(windows_apps, "cdbX64.exe"),
            os.path.join(windows_apps, "cdbX86.exe"),
            os.path.join(windows_apps, "WinDbgX.exe"),
            "cdb.exe"
        ]

        # Check in Windows Kits
        program_files = os.environ.get("ProgramFiles(x86)", "C:\\Program Files (x86)")
        kits_base = os.path.join(program_files, "Windows Kits", "10", "Debuggers")
        if os.path.exists(kits_base):
            for arch in ["x64", "x86"]:
                candidates.append(os.path.join(kits_base, arch, "cdb.exe"))

        for path in candidates:
            # Test if executable exists or is in path
            try:
                if os.path.isabs(path) and os.path.exists(path):
                    return path
                # Try running it to see if it's in path
                subprocess.run([path, "-?"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1)
                return path
            except:
                continue
        return None

    def run(self, dump_path=None, pid=None, exec_path=None, command=None):
        if not self.cdb_path:
            raise FileNotFoundError("Could not find cdb.exe or cdbX64.exe in standard paths.")

        # Build cdb arguments
        args = [self.cdb_path]
        
        # Suppress initial prompt and logo banner
        args.extend(["-lines", "-G"])

        if dump_path:
            args.extend(["-z", dump_path])
        elif pid:
            args.extend(["-p", str(pid)])
        elif exec_path:
            args.extend([exec_path])
        else:
            raise ValueError("Must specify either --dump, --pid, or --exec")

        # Pass commands to execute (c is command-line execution, q is quit)
        if command:
            # Ensure command ends with quit if it doesn't already
            if not command.strip().endswith("q") and not ";q" in command:
                command += "; q"
            args.extend(["-c", command])

        print(f"Running: {' '.join(args)}")
        
        try:
            result = subprocess.run(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=60 # 60 second timeout for debugging tasks
            )
            return result.stdout
        except subprocess.TimeoutExpired as e:
            return f"Error: Command timed out. Partial Output:\n{e.stdout}"
        except Exception as e:
            return f"Error executing cdb: {e}"

def main():
    parser = argparse.ArgumentParser(description="WinDbg (cdb) Command Automation Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pid", type=int, help="Process ID to attach to")
    group.add_argument("--dump", type=str, help="Path to Crash Dump file (.dmp)")
    group.add_argument("--exec", dest="exec_path", type=str, help="Path to executable to launch")
    
    parser.add_argument("--command", type=str, required=True, help="WinDbg command to execute (e.g. 'k; lm; q')")

    args = parser.parse_args()

    try:
        debugger = CdbDebugger()
        print(f"Using debugger executable: {debugger.cdb_path}")
        output = debugger.run(
            dump_path=args.dump,
            pid=args.pid,
            exec_path=args.exec_path,
            command=args.command
        )
        print("\n--- WINDBG OUTPUT ---")
        print(output)
        print("---------------------")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
