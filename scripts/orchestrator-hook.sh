#!/usr/bin/env bash
# orchestrator-hook.sh — Antigravity lifecycle hook bridging to the shared
# orchestrator-governor.sh. Reads the hook JSON payload from stdin.
#
# Wire it in ~/.gemini/config/hooks.json:
#   - PreToolUse  (matcher invoke_subagent|manage_subagents|task): reserve a slot.
#   - PostToolUse (matcher invoke_subagent|manage_subagents|task): release the slot,
#                 or mark PAUSED if the subagent failed with a rate-limit symptom (429).
#   - PreInvocation: inject the current concurrency budget + retry contract.
#
# The stdin payload uses camelCase keys (protojson): toolCall.name, error, etc.
# The slot key is derived deterministically from conversationId+stepIdx so the
# same subagent step releases the exact slot it acquired.

set -euo pipefail

GOV="${ORCH_GOVERNOR:-/home/daniel/Code/skills/scripts/orchestrator-governor.sh}"
MAX_TOTAL="${ORCH_MAX_CONCURRENT:-5}"

# Consume stdin into a temp file once (json_value reads from it afterwards).
PAY_FILE="$(mktemp)"
cat > "$PAY_FILE"
trap 'rm -f "$PAY_FILE"' EXIT

json_value() { # $1: dotted path e.g. "toolCall.name" -> prints scalar or ""
  GO_PATH="$1" python3 - "$PAY_FILE" <<'PYEOF'
import json,sys,os
path=os.environ["GO_PATH"].split(".")
try:
    d=json.load(open(sys.argv[1]))
except Exception:
    sys.exit(0)
cur=d
for p in path:
    if isinstance(cur,dict) and p in cur:
        cur=cur[p]
    else:
        sys.exit(0)
if isinstance(cur,(str,int,float)) or cur is None:
    sys.stdout.write("" if cur is None else str(cur))
PYEOF
}

# Stable per-step key shared between pretool and posttool for the same subagent.
slot_id() {
  local conv step; conv="$(json_value conversationId || true)"; step="$(json_value stepIdx || true)"
  echo "agy-${conv:-none}-${step:-none}"
}

RATE_RE='(429|Too Many Requests|rate.?limit|quota exceeded|RPM|TPM|tokens_per_minute|tokens per minute)'

case "${1:-}" in
  pretool)
    tool="$(json_value toolCall.name || true)"
    case "$tool" in
      invoke_subagent|manage_subagents|task)
        "$GOV" acquire "$(slot_id)" no 30 "$MAX_TOTAL" >/dev/null 2>&1 || true
        echo '{}'
        ;;
      *) echo '{}' ;;
    esac
    ;;
  posttool)
    err="$(json_value error || true)"
    if [ -n "$err" ] && echo "$err" | grep -qiE "$RATE_RE"; then
      "$GOV" fail "$(slot_id)" 2>/dev/null || true
      GO_MSG="Rate-limit (429) detected in a spawned agent. Orchestrator: mark that task PAUSED, wait until fewer than ${MAX_TOTAL} agents run (counting you), then relaunch it with exponential backoff. Do NOT relaunch while the cap is saturated." \
        python3 -c 'import json,sys,os; print(json.dumps({"ephemeralMessage":os.environ["GO_MSG"]}))'
    else
      "$GOV" release "$(slot_id)" 2>/dev/null || true
      echo '{}'
    fi
    ;;
  preinv)
    status="$("$GOV" status "$MAX_TOTAL" 2>/dev/null || echo "running=0 paused=0 max=$MAX_TOTAL slots_free=$MAX_TOTAL")"
    GO_STATUS="$status" GO_CAP="$MAX_TOTAL" python3 -c 'import json,sys,os
cap=os.environ["GO_CAP"]; status=os.environ["GO_STATUS"]
msg="[CONCURRENCY GOVERNOR] Max concurrent agents counting the orchestrator = "+cap+". Current ledger: "+status+". Do not spawn a new subagent while running >= cap: enqueue it (QUEUED) and wait for a running agent to finish. If a subagent fails with HTTP 429 / Too Many Requests / quota, kill it, mark it PAUSED, wait until running < cap and relaunch with exponential backoff."
print(json.dumps({"injectSteps":[{"ephemeralMessage":msg}]}))'
    ;;
  *) echo '{}' ;;
esac
exit 0
