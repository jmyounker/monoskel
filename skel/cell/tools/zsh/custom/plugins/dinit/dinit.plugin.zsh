# Runs actions when you enter or leave a directory.

run-dinit() {
  local cwd=$(pwd)
  if [[ -n "${DINIT_PREVIOUS_DIR}" ]]; then
	  local cur=${DINIT_PREVIOUS_DIR}
	  local prev=''
      while [[ "$cur" != "$prev" ]]; do
         if [ -f "$cur/.dinit" ]; then
            source "$cur/.dinit" leave
         fi
         prev="$cur"
         cur=$(dirname $cur)
      done
  fi
  export DINIT_PREVIOUS_DIR=${cwd}
  local d=''
  local cur=''
  for d in ${(s:/:)cwd}; do
    cur="$cur/$d"
    if [ -f "$cur/.dinit" ]; then
       source "$cur/.dinit" enter
    fi
  done
}

# Create a template directory state file.
mk-dinit() {
  cat <<'EOF' >.dinit
# Simple directory state file that adds or removes a child bin directory
# to/from your path. Used by the dinit zsh plugin.
local PWD=${0:h}
case "$1" in
    enter)
        path=("$PWD/bin" $path)
        ;;
    leave)
        path=(${(@)path:#$PWD/bin})
        ;;
    *)
        echo "Usage: $0 {enter|leave}" >&2
        ;;
esac
EOF
}

if ! (( $chpwd_functions[(I)run-dinit] )); then
  chpwd_functions+=(run-dinit)
fi

cd .