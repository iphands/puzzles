#!/bin/bash

_fail() {
  echo -e "\n\nFail: $1"
  exit 1
}

_list() {
  find src/ | grep '[a-z]/main.py$' | sort -u | sed -r -e 's|/|.|g' -e 's|.py$||'
  exit 0
}

[[ "$1" == list ]] && _list $1

for var in `find src/ | fgrep main.py | sort -u | sed -r -e 's|/|.|g' -e 's|.py$||'`
do
  echo -ne "\n\nTesting: $var"
  time python -m $var >/dev/null || _fail $var
done
