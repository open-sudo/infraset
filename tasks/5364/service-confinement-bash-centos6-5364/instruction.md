On `node1`, run a background worker as the dedicated unprivileged account `inventorysvc`, managed as `inventory-worker`. Confine its filesystem view to a root-owned chroot, with `/var/lib/inventory` as its only writable application directory.

Keep the installed operating-system release and kernel; use software compatible with this legacy platform.
