The documentation and purchasing teams need separate websites on node1, sharing
TCP port 8080. Requests for docs.branch.test should serve the supplied docs tree;
requests for orders.branch.test should serve the orders tree. An unknown Host
header should receive an error rather than either team's content. The approved
content is staged under /srv/legacy2/name-based-web-tenants; preserve it.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
