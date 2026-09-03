Treat `/etc/inventory/app.conf` on `node1` as the source of truth for the
inventory application's configuration. Keep the copy of that file on `node2`
synchronized with `node1`, picking up any change within 15 minutes.
