#!/bin/sh
# Harbor task-validation sentinel. The configured custom verifier replaces it.
echo "Tasks must run with harbor_antrieb.verifier:AntriebVerifier" >&2
exit 2
