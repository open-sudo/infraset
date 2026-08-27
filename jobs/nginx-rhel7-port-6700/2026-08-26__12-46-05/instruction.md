Configure `node1` to provide an HTTP service using the distribution-supported
Nginx software on RHEL 7.9.

The service must return a successful HTTP response at `/` over TCP port `6700`
when addressed through `node1`'s managed network address. Port `6700` must be
the only HTTP listening port for this Nginx service.

The Nginx configuration, network access, and service must remain operational
after `node1` is rebooted.
