`node1` is a Debian HTTPS server running the distribution-supported Nginx service
on TCP port 443. Its current self-signed certificate has expired. Rotate the
endpoint to a new self-signed certificate that is valid for the DNS name `node1`
and has at least 180 days of validity remaining.

Preserve the existing web content and HTTPS endpoint. Existing HTTPS connections
and endpoint availability must continue without interruption during the rotation.
From the Debian client `node2`, the OpenSSL client must retrieve the new certificate
from `node1:443` and validate its hostname, validity period, and self-signature.

The Nginx configuration, rotated certificate, protected private key, HTTPS content,
and client access must remain operational after both systems are rebooted.
