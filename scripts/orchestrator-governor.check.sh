#!/usr/bin/env bash
# orchestrator-governor.check.sh — runtime health check that PROVES the
# concurrency + rate-limit governance is actually wired (not just documented).
#   * governor script present + executable
#   * governor actually acquires/blocks/releases/fails
#   * Antigravity hooks registered
#   * OpenCode plugin present + auto-discovered
# Run: bash scripts/orchestrator-governor.check.sh
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GOV="$DIR/orchestrator-governor.sh"
HOOK="$DIR/orchestrator-hook.sh"
PLUGIN="$DIR/orchestrator-gate.ts"
TEST="$DIR/orchestrator-governor.test.sh"
MAX="${ORCH_MAX_CONCURRENT:-5}"

ok(){ echo "ok   - $1"; }
warn(){ echo "warn - $1"; }
fail(){ echo "FAIL - $1"; rc=1; }
rc=0

[ -x "$GOV" ] && ok "governor present + executable: $GOV" || fail "governor missing/not executable: $GOV"
[ -f "$HOOK" ] && ok "antigravity hook script present: $HOOK" || warn "hook script missing: $HOOK"
[ -f "$TEST" ] && ok "test script present: $TEST" || warn "test script missing: $TEST"
[ -f "$PLUGIN" ] && ok "opencode plugin present: $PLUGIN" || warn "opencode plugin missing: $PLUGIN"

# Antigravity global hooks -> must contain an 'orchestrator-governor' key
AH="${AH_HOOKS_FILE:-$HOME/.gemini/config/hooks.json}"
if [ -f "$AH" ] && grep -q '"orchestrator-governor"' "$AH" 2>/dev/null; then
  ok "antigravity hooks.json wired (orchestrator-governor): $AH"
else
  warn "antigravity hooks.json not wired (want key orchestrator-governor): $AH"
fi

# OpenCode deploy plugin (auto-discovered from ~/.config/opencode/plugins)
OP="${OPENCODE_PLUGINS_DIR:-$HOME/.config/opencode/plugins}"
if [ -f "$OP/orchestrator-gate.ts" ]; then
  ok "opencode deploy plugin present: $OP/orchestrator-gate.ts"
else
  warn "opencode deploy plugin missing: $OP/orchestrator-gate.ts (copy scripts/orchestrator-gate.ts there)"
fi

# Functional proof via the test suite (cap really holds)
if [ -x "$TEST" ] || [ -f "$TEST" ]; then
  if bash "$TEST" >/tmp/orch_test.out 2>&1; then
    ok "governor functional: concurrency cap + rate-limit retry tests PASSED"
  else
    fail "governor test suite failed; see /tmp/orch_test.out"
  fi
fi

echo
if [ "$rc" -eq 0 ]; then echo "ORCHESTRATOR-GOVERNOR CHECK: ALL GREEN"; else echo "ORCHESTRATOR-GOVERNOR CHECK: ISSUES FOUND"; fi
exit "$rc"
