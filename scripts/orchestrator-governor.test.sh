#!/usr/bin/env bash
# orchestrator-governor.test.sh — executable validation for the slot governor.
# Proves the concurrency cap really holds (not just documented):
#   1. Exactly MAX agents acquire a concurrent slot.
#   2. The (MAX+1)th concurrent acquire is queued/denied until a slot frees.
#   3. fail() marks an agent PAUSED (rate-limit) and release() frees its slot.
# Run: bash scripts/orchestrator-governor.test.sh
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GOV="$DIR/orchestrator-governor.sh"
export GOVERNOR_STATE_DIR="${GOVERNOR_STATE_DIR:-$(mktemp -d)/orchestrator-test}"
MAX="${ORCH_MAX_CONCURRENT:-5}"

fail() { echo "FAIL: $*" >&2; exit 1; }
pass() { echo "ok - $*"; }

rm -rf "$GOVERNOR_STATE_DIR"
"$GOV" reset

# --- 1) exactly MAX acquire concurrently ---
echo "== test 1: cap of $MAX holds (concurrent) =="
rm -f /tmp/orch_ok /tmp/orch_deny
for i in $(seq 1 "$((MAX + MAX + 1))"); do
  (
    if timeout 4 "$GOV" acquire "w$i" no 2 "$MAX" >/dev/null 2>&1; then
      echo "$i" >> /tmp/orch_ok
    else
      echo "$i" >> /tmp/orch_deny
    fi
  ) &
done
wait
ok_count=$(wc -l < /tmp/orch_ok 2>/dev/null || echo 0)
deny_count=$(wc -l < /tmp/orch_deny 2>/dev/null || echo 0)
[ "$ok_count" -eq "$MAX" ] || fail "expected $MAX concurrent acquires, got $ok_count (denied=$deny_count)"
pass "cap holds: exactly $MAX concurrent acquired, $deny_count enqueued/denied"

# --- 2) ledger reflects exactly MAX running ---
sleep 0.5  # let any still-writing concurrent workers settle
running=$("$GOV" status "$MAX" | sed -n 's/.*running=\([0-9]*\).*/\1/p')
[ -n "$running" ] || running=0
[ "$running" -eq "$MAX" ] || fail "ledger running=$running, want $MAX"
pass "ledger running=$running == $MAX"

# --- 3) fail marks a live RUNNING caller PAUSED (rate-limit) ---
live_caller=$("$GOV" status "$MAX" | awk 'NR>1 && $1=="RUNNING"{print $2; exit}')
[ -n "$live_caller" ] || fail "no RUNNING caller to fail"
"$GOV" fail "$live_caller"
sleep 0.2
paused=$("$GOV" status "$MAX" | sed -n 's/.*paused=\([0-9]*\).*/\1/p')
[ -n "$paused" ] || paused=0
if [ "$paused" -lt 1 ]; then
  echo "  debug: live_caller='$live_caller' ledger=${GOVERNOR_STATE_DIR}/ledger" >&2
  "$GOV" status "$MAX" >&2
  fail "expected paused>=1 after fail(), got $paused"
fi
pass "fail() marked '$live_caller' PAUSED (rate-limit)"

# --- 4) release frees a slot so a new one can acquire ---
rel=$("$GOV" status "$MAX" | awk 'NR>1 && $1=="RUNNING"{print $2; exit}' | head -1)
[ -n "$rel" ] || fail "no RUNNING caller to release"
"$GOV" release "$rel"
free_slots=$("$GOV" status "$MAX" | sed -n 's/.*slots_free=\([0-9]*\).*/\1/p')
[ -n "$free_slots" ] || free_slots=0
[ "$free_slots" -ge 1 ] || fail "no free slot after release"
pass "release() freed a slot (slots_free=$free_slots)"

echo
echo "ALL ORCHESTRATOR-GOVERNOR TESTS PASSED"
