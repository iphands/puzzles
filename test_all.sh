#!/bin/bash

_fail() {
  echo -e "\n\nFail: $1"
  exit 1
}

for var in `find src/ | fgrep main.py | sort -u | sed -r -e 's|/|.|g' -e 's|.py$||'`
do
  echo -ne "\n\nTesting: $var"
  time python -m $var >/dev/null || _fail $var
done
