Each router answers DNS for the private network it serves. Have `node1`
resolve the name `app.internal` to `node3`'s address for hosts on `lan-a`,
and `node2` resolve the same name to `node4`'s address for hosts on `lan-b`,
so each host reaches the service on its own side of the transit network by
that one name.
