#!/bin/sh
# Harbor task-validation sentinel. The configured custom verifier replaces it.
echo "Tasks must run with an infraset verifier" >&2
exit 2
