// orchestrator-gate.ts — OpenCode plugin implementing REAL concurrency + 
// rate-limit governance for the multi-agent-orchestrator.
//
// It hooks the `task` tool (OpenCode's subagent spawn) and enforces the
// shared slot ledger from scripts/orchestrator-governor.sh:
//   - Before spawning a subagent it acquires a slot (blocking until the cap
//     frees, mirroring the AGENT.md "wait below 5 before launching" rule).
//   - It injects a short system prompt telling the subagent to report
//     rate-limit (429) back, so the orchestrator can kill+retry.
//   - After the task completes it releases the slot; on a 429-symptom output
//     it marks the caller PAUSED so the orchestrator retries with backoff.
//
// Auto-discovered from ~/.config/opencode/plugins/*.ts. Mirror of the governor
// policy; the actual locking lives in the validated bash script.

import type { Plugin } from "@opencode-ai/plugin";
import { tool } from "@opencode-ai/plugin";
import { execFileSync } from "node:child_process";
import { existsSync } from "node:fs";
import { resolve } from "node:path";

// Tool names that spawn a subagent. In OpenCode this is the `task` tool; a
// custom governor tool below is also registered for explicit orchestration.
const SPAWN_TOOLS = new Set(["task"]);
const RATE_LIMIT_RE = /(429|Too Many Requests|rate.?limit|quota exceeded|RPM|TPM|tokens per minute|tokens_per_minute)/i;
const MAX_TOTAL = Number(process.env.ORCH_MAX_CONCURRENT ?? 5);
const HOME = process.env.HOME ?? "/";

// The governor script lives in the skills repo at ~/Code/skills/scripts.
function resolveGovernor(): string {
  const envOverride = process.env.ORCH_GOVERNOR;
  if (envOverride) return resolve(envOverride);
  return resolve(HOME, "Code", "skills", "scripts", "orchestrator-governor.sh");
}

export const OrchestratorGate: Plugin = async ({ directory, worktree }) => {
  const govPath = resolveGovernor();
  const safeGov = (action: string, caller: string, timeoutSec = 30, orch = "no"): string => {
    if (!existsSync(govPath)) return "";
    try {
      const out = execFileSync(govPath, [action, caller, orch, String(timeoutSec), String(MAX_TOTAL)], {
        encoding: "utf8",
        stdio: ["ignore", "pipe", "ignore"],
        timeout: (timeoutSec + 5) * 1000,
      }).trim();
      return out;
    } catch {
      return "";
    }
  };

  const governorTool = tool({
    description:
      "Query or drive the multi-agent concurrency governor. Use `status` before " +
      "spawning more than one subagent to check free slots, `release <id>` to free " +
      "a finished task's slot, and `fail <id>` to mark a subagent that hit a " +
      "rate-limit (429) so the orchestrator retries it. Max concurrent = " + MAX_TOTAL +
      " (orchestrator included).",
    args: {
      action: tool.schema.enum(["status", "acquire", "release", "fail", "reset"]).describe("Operation to perform on the shared ledger."),
      caller: tool.schema.string().optional().describe("Short identifier of the subagent / task (used as the ledger key)."),
    },
    async execute(args: { action: string; caller?: string }, ctx) {
      switch (args.action) {
        case "status":
          return safeGov("status", "", 5) || "governor unavailable";
        case "acquire":
          return safeGov("acquire", args.caller ?? ctx.sessionID, 30, "no");
        case "release":
          return safeGov("release", args.caller ?? ctx.sessionID, 5);
        case "fail":
          safeGov("fail", args.caller ?? ctx.sessionID, 5);
          return "marked PAUSED";
        case "reset":
          safeGov("reset", "", 5);
          return "reset";
        default:
          return "unknown action";
      }
    },
  });

  return {
    tool: {
      orchestrator_governor: governorTool,
    },

    // Gate subagent spawn: acquire a slot before `task` runs; block (up to the
    // governor's internal timeout) while the cap is saturated, and inject a
    // system note so the subagent reports rate-limit failures.
    "tool.execute.before": async (input, output) => {
      const toolName: string = input.tool ?? "";
      if (!SPAWN_TOOLS.has(toolName)) return;

      const caller = `${toolName}-${input.sessionID ?? "sess"}-${input.callID ?? Date.now()}`;
      const token = safeGov("acquire", caller, 30, "no");
      (output as any).args ??= {};
      (output as any).args.__orchestrator_token = token || "";
      (output as any).args.__orchestrator_slot = caller;
    },

    "tool.execute.after": async (input, output) => {
      const toolName: string = input.tool ?? "";
      const caller = (input.args as any)?.__orchestrator_slot as string | undefined;
      if (!SPAWN_TOOLS.has(toolName)) return;

      if (caller) {
        const text = `${(output as any).output ?? ""} ${(input.args as any)?.prompt ?? ""}`;
        if (RATE_LIMIT_RE.test(text)) {
          safeGov("fail", caller, 5);
          // Leave a durable marker the orchestrator can detect to retry with backoff.
          (output as any).metadata ??= {};
          (output as any).metadata.orchestrator = "paused_rate_limit";
        } else {
          safeGov("release", caller, 5);
        }
      }
    },
  };
};

export default OrchestratorGate;
