#!/usr/bin/env bash
# orchestrator-governor.sh — real concurrency + rate-limit governor for the
# multi-agent-orchestrator. Shared between OpenCode (plugin) and Google
# Antigravity (PreInvocation hook). Idempotent, pure-bash, validates cleanly
# with `bash -n`.
#
# Maintains an on-disk slot ledger guarded by flock() so concurrent agent
# processes (orchestrator + subagents) cannot overshoot the parallel cap,
# preventing 429/rate-limit failures. Executable counterpart of the policy in
# the orchestrator's AGENT.md.
#
# Usage:
#   orchestrator-governor.sh acquire <caller-id> [orchestrator-yes|no] [timeout-secs] [max-total]
#   orchestrator-governor.sh release <caller-id> [orchestrator-yes|no]
#   orchestrator-governor.sh fail    <caller-id>              # rate-limit hit
#   orchestrator-governor.sh status [max-total]
#   orchestrator-governor.sh reset
#
# Slot semantics (matches "5 counting the orchestrator"): max-total defaults to
# 5. The orchestrator's own slot uses flag `yes`. acquire blocks (up to
# timeout) until a slot frees, then reserves it. release frees the slot. fail
# tags the caller PAUSED so the orchestrator can retry it after backoff.

set -euo pipefail

GOV_STATE_DIR="${GOVERNOR_STATE_DIR:-${XDG_RUNTIME_DIR:-/tmp}/orchestrator-governor}"
GOV_LOCK_FILE="${GOV_STATE_DIR}/ledger.lock"
GOV_LEDGER_FILE="${GOV_STATE_DIR}/ledger"
GOV_MAX_TOTAL_DEFAULT="${ORCH_MAX_CONCURRENT:-5}"

mkdir -p "${GOV_STATE_DIR}" 2>/dev/null || true
# A dedicated lock file that is never truncated; flock() uses its inode.
: > "${GOV_LOCK_FILE}"

# Run a body function under an exclusive flock. The body reads the ledger from
# $1 and writes its replacement to stdout; we swap it in atomically. tmp file is
# unique per process to avoid cross-process clobbering.
with_lock() {
  local fn="$1"; shift
  local tmp; tmp="$(mktemp "${GOV_STATE_DIR}/ledger.tmp.XXXXXX")"
  flock -x 9
  "$fn" "${GOV_LEDGER_FILE}" "$@" < /dev/null > "${tmp}" 2>/dev/null || true
  mv "${tmp}" "${GOV_LEDGER_FILE}"
  flock -u 9
} 9<>"${GOV_LOCK_FILE}"

_acq_body() {
  # stdout becomes the new ledger. Start from the current ledger so we never
  # drop other callers' slots; append our own reservation at the end.
  local ledger="$1" caller="$2" orch_flag="$3" token="$4" max_total="$5" timeout="$6"
  local now deadline running
  # if already the holder, re-emit ledger unchanged (no new reservation)
  if grep -q "^RUNNING ${caller} " "${ledger}" 2>/dev/null; then
    cat "${ledger}" 2>/dev/null || true
    return 0
  fi
  now="$(date +%s)"; deadline=$(( now + timeout ))
  running=$(grep -c '^RUNNING ' "${ledger}" 2>/dev/null || true); running=${running:-0}
  while [ "${running}" -ge "${max_total}" ]; do
    [ "$(date +%s)" -ge "${deadline}" ] && { cat "${ledger}" 2>/dev/null || true; return 0; }
    sleep 0.3
    running=$(grep -c '^RUNNING ' "${ledger}" 2>/dev/null || true); running=${running:-0}
  done
  cat "${ledger}" 2>/dev/null || true
  echo "RUNNING ${caller} ${orch_flag} ${token}"
}
cmd_acquire() {
  local caller="$1" orch_flag="$2" timeout="$3" max_total="$4"
  local token="${caller}-$$-$(date +%s%N)"
  with_lock _acq_body "${caller}" "${orch_flag}" "${token}" "${max_total}" "${timeout}"
  if grep -q "^RUNNING ${caller} " "${GOV_LEDGER_FILE}" 2>/dev/null; then
    echo "${token}"
    return 0
  fi
  return 1
}

_rel_body()  {
  # re-emit everything except the caller's RUNNING row; keep PAUSED rows.
  local ledger="$1" caller="$2"
  grep -v "^RUNNING ${caller} " "${ledger}" 2>/dev/null || true
}
cmd_release() { local caller="$1"; with_lock _rel_body "${caller}"; }

_fail_body()  {
  # turn the caller's RUNNING row into a PAUSED rate-limit row.
  local ledger="$1" caller="$2"
  grep -v "^RUNNING ${caller} " "${ledger}" 2>/dev/null || true
  echo "PAUSED ${caller} $(date +%s)"
}
cmd_fail()    { local caller="$1"; with_lock _fail_body "${caller}"; }

cmd_status() {
  local max_total="$1"
  local ledger
  flock -x 9
  ledger="${GOV_LEDGER_FILE}"
  if [ -f "${ledger}" ]; then
    local running paused free
    running=$(grep -c '^RUNNING ' "${ledger}" 2>/dev/null || true); running=${running:-0}
    paused=$(grep -c '^PAUSED '  "${ledger}" 2>/dev/null || true); paused=${paused:-0}
    free=$(( max_total - running < 0 ? 0 : max_total - running ))
    echo "running=${running} paused=${paused} max=${max_total} slots_free=${free}"
    cat "${ledger}"
  else
    echo "running=0 paused=0 max=${max_total} slots_free=${max_total}"
  fi
  flock -u 9
} 9<>"${GOV_LOCK_FILE}"

cmd_reset() {
  local tmp; tmp="$(mktemp "${GOV_STATE_DIR}/ledger.tmp.XXXXXX")"
  flock -x 9; rm -f "${GOV_LEDGER_FILE}"; flock -u 9; rm -f "${tmp}"
} 9<>"${GOV_LOCK_FILE}"

main() {
  local cmd="${1:-status}"; shift || true
  case "${cmd}" in
    acquire) cmd_acquire "${1:-x}" "${2:-no}" "${3:-30}" "${4:-${GOV_MAX_TOTAL_DEFAULT}}";;
    release) cmd_release "${1:-x}";;
    fail)    cmd_fail "${1:-x}";;
    status)  cmd_status "${1:-${GOV_MAX_TOTAL_DEFAULT}}";;
    reset)   cmd_reset;;
    *) echo "unknown command: ${cmd}" >&2; exit 2;;
  esac
}
main "$@"
