# shellcheck shell=bash
# Sourced by push.sh and propagate-pages.sh; the caller sets $env_file to the repository-root .env.
#
# load_dotenv_value NAME reads NAME from that file without overriding a value already exported by
# the caller. The file is intentionally local-only and ignored; it may contain shell quoting for
# command prefixes with arguments.
load_dotenv_value() {
    local name=$1 value
    [[ -f "$env_file" ]] || return 0
    [[ -v "$name" ]] && return 0
    value=$(bash -c 'source "$1"; var=$2; printf "%s" "${!var-}"' _ "$env_file" "$name")
    if [[ -n "$value" ]]; then
        printf -v "$name" '%s' "$value"
        export "$name"
    fi
}
