Repair the upload endpoint on node1 so POST /upload on TCP port 8080 accepts raw
request bodies up to 65536 bytes and rejects larger ones with HTTP 413 before
publishing a receipt. Each accepted upload belongs in a separate file under
received/ with identical bytes. An interrupted request should leave no completed
receipt, and other paths should return HTTP 404. Preserve the existing receipt
in /srv/legacy2/http-upload-size-boundary. Node2 is the application client.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
