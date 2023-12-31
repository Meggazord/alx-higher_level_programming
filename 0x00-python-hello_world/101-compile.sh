#!/bin/bash

if [ -z "$PYFILE" ]; then
  echo "Error: PYFILE environment variable is not set."
  exit (1)
fi

echo "Compiling $PYFILE ..."
python3 -m py_compile "$PYFILE"

exit (0)
