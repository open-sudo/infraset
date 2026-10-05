"""Authoring source for 60 distinct, paired legacy infrastructure scenarios.

Files are installed beneath /srv/legacy2/<slug> on the indicated managed node.
This module is used only by the static generator, never by task executors.
"""
from textwrap import dedent
from inspect import cleandoc

FAMILIES = []


def add(slug, category, request, distinction, files, nodes=1, archives=None, links=None):
    FAMILIES.append(dict(slug=slug, category=category, nodes=nodes,
        instruction=dedent(request).strip() + '\n', distinction=distinction,
        files={name: (cleandoc(body) + '\n') if '\n' in body.rstrip('\n') and not '\r' in body else body for name, body in files.items()},
        archives=archives or {}, links=links or {}))


add('name-based-web-tenants', 'web', '''
    The documentation and purchasing teams need separate websites on node1, sharing
    TCP port 8080. Requests for docs.branch.test should serve the supplied docs tree;
    requests for orders.branch.test should serve the orders tree. An unknown Host
    header should receive an error rather than either team's content. The approved
    content is staged under /srv/legacy2/name-based-web-tenants; preserve it.
    ''', 'Host-based tenant routing and default-host isolation, not a load-balanced web tier.', {
    'docs/index.html': '<h1>Branch documentation</h1>\n',
    'docs/handbook.txt': 'Office hours: weekdays 09:00-17:00\n',
    'orders/index.html': '<h1>Purchasing desk</h1>\n',
    'orders/catalog.csv': 'sku,description\nP100,Printer paper\nT200,Shipping tape\n',
    'handover.txt': 'Both sites belong on the same address and TCP port 8080.\n'})

add('web-authentication-boundary', 'web', '''
    On node1, publish the staged public and staff trees under /public/ and /staff/
    on TCP port 8080. Public pages are anonymous; staff pages require HTTP Basic
    authentication as reader using the demonstration password in access.txt.
    Failed authentication must leave staff content inaccessible, and neither the
    password file nor directory listings should be served. Keep the supplied pages
    under /srv/legacy2/web-authentication-boundary intact.
    ''', 'HTTP authentication and content boundaries, not SSH policy or host firewalling.', {
    'public/index.html': '<h1>Visitor information</h1>\n',
    'staff/index.html': '<h1>Staff schedules</h1>\n',
    'staff/roster.csv': 'name,shift\nAlex,early\nSam,late\n',
    'access.txt': 'Demonstration account: reader\nDemonstration password: BranchDemo-2704\n'})

add('permanent-url-migration', 'web', '''
    The help site on node1 has moved from /manual/ to /help/. Serve the staged help
    tree on TCP port 8080 and permanently redirect old manual URLs to the corresponding
    help URL, retaining the remaining path and query string. Existing /status.txt
    requests must still return the supplied status document without a redirect.
    Source content is in /srv/legacy2/permanent-url-migration.
    ''', 'URL migration semantics and query preservation, not DNS or TLS setup.', {
    'help/index.html': '<h1>Help centre</h1>\n',
    'help/network/setup.html': '<h1>Network setup guide</h1>\n',
    'status.txt': 'service=helpdesk\nstatus=available\n'})

add('cgi-report-execution', 'web', '''
    The report bundle staged on node1 was retired after its endpoint exposed the script instead of running it.
    Configure a legacy-compatible web service on TCP port 8080 so /cgi-bin/report
    executes the supplied report and returns its text output. Static files in public/
    should remain available at /; application source and private/ must stay outside
    the published content. Use the assets in /srv/legacy2/cgi-report-execution and
    preserve the report's business output.
    ''', 'CGI execution and source disclosure, not generic daemon installation.', {
    'cgi-bin/report': r'''#!/bin/sh
        printf 'Content-Type: text/plain\r\n\r\n'
        printf 'warehouse=west\nopen_orders=7\n'
        ''',
    'public/index.html': '<h1>Warehouse reports</h1>\n',
    'private/report-source.txt': 'Internal reporting calculation notes.\n',
    'handover.conf': 'The previous server treated cgi-bin as a static directory.\n'})

add('webdav-document-locks', 'web', '''
    Provide a WebDAV workspace at /documents/ on node1, TCP port 8080, using the
    supplied project documents. The editor account in access.txt should be able to
    create, read, replace, and delete documents. Honor exclusive document locks so
    an update without the lock token cannot overwrite a locked document. Anonymous
    clients may not access the workspace. Preserve the initial project documents
    in /srv/legacy2/webdav-document-locks.
    ''', 'WebDAV write and lock semantics; no equivalent protocol task exists in legacy.', {
    'documents/brief.txt': 'Project Cedar: relocate the branch help desk.\n',
    'documents/budget.csv': 'item,amount\ndesks,2400\ncabling,850\n',
    'access.txt': 'Demonstration account: editor\nDemonstration password: CedarDemo-2704\n'})

add('ftp-dropbox-confinement', 'file-services', '''
    A legacy scanner on node2 only supports passive FTP. Set up node1 as its upload
    destination with the scanner account described in access.txt, confined to a
    dedicated dropbox. It needs to upload and retrieve its files, including the
    supplied sample scan, with host files outside that dropbox inaccessible.
    Anonymous access should be unavailable. The handover and sample are staged in
    /srv/legacy2/ftp-dropbox-confinement on both nodes.
    ''', 'Passive FTP client compatibility and confinement, not NFS or a shared sticky directory.', {
    'sample-scan.txt': 'Scanner batch SC-0042\nPages: 3\n',
    'dropbox/received.txt': 'Previously received scanner document.\n',
    'access.txt': 'Demonstration account: scanner\nDemonstration password: ScanDemo-2704\n'}, nodes=2)

add('tftp-firmware-distribution', 'file-services', '''
    The boot controller on node2 needs to download boot.cfg and firmware.bin from
    node1 using TFTP. Publish the staged boot tree as a read-only TFTP root, preserving
    the firmware bytes. Upload attempts and requests outside the boot root should
    be rejected. The approved files are in /srv/legacy2/tftp-firmware-distribution.
    ''', 'TFTP boot artifacts and read-only transfer policy, not a package repository.', {
    'boot/boot.cfg': 'device=branch-terminal\nfirmware=firmware.bin\n',
    'boot/firmware.bin': 'BRANCH-FIRMWARE\nrevision=7\npayload=0042\n',
    'private/vendor-notes.txt': 'Internal vendor service notes.\n'}, nodes=2)

add('rsync-module-publication', 'file-services', '''
    Publish the release tree on node1 as a read-only rsync daemon module named
    releases. Node2 needs to retrieve the full tree with file modes and symlinks
    intact. Writes through the module and access outside its tree must be denied.
    Preserve the approved release under /srv/legacy2/rsync-module-publication.
    ''', 'An rsync wire-protocol module and metadata fidelity, not periodic configuration sync.', {
    'releases/v1/README': 'Branch client release 1\n',
    'releases/v1/bin/client': '#!/bin/sh\nprintf "branch-client 1\\n"\n',
    'private/signing-policy.txt': 'Release approval belongs to the release team.\n'},
    nodes=2, links={'releases/current': 'v1'})

add('samba-team-share', 'file-services', '''
    Set up the staged projects directory on node1 as an SMB share named projects
    for the design team. Node2 must be able to list, read, and update documents as
    designer using the demonstration credentials in access.txt. Guest access and
    access to sibling directories should be rejected. Keep the initial drawings
    in /srv/legacy2/samba-team-share intact.
    ''', 'SMB authentication and file sharing, distinct from the existing NFS family.', {
    'projects/drawing.txt': 'Design D-100: reception layout\n',
    'projects/materials.csv': 'material,count\npanel,6\nrail,12\n',
    'private/contracts.txt': 'Design team purchasing contracts.\n',
    'access.txt': 'Demonstration account: designer\nDemonstration password: DesignDemo-2704\n'}, nodes=2)

add('print-spool-recovery', 'file-services', '''
    Recover the branch's staged print jobs on node1 into a working CUPS queue named
    archive. This is an electronic archive printer: completed raw job payloads belong
    in /srv/legacy2/print-spool-recovery/printed, one file per job. Process each job
    listed in spool/jobs.tsv exactly once, retaining its bytes and the original
    spool files. New raw jobs submitted to the queue should follow the same path;
    no physical printer is available.
    ''', 'CUPS queue recovery and a file-backed print sink, not a scheduled maintenance job.', {
    'spool/jobs.tsv': 'job_id\tpayload\nJ100\tJ100.prn\nJ101\tJ101.prn\n',
    'spool/J100.prn': 'Invoice I-9001\nTotal: 45.00\n',
    'spool/J101.prn': 'Packing slip S-9002\nCartons: 3\n'})

add('ldap-directory-import', 'identity', '''
    Bring up an LDAP directory on node1 for dc=branch,dc=test and import the staged
    LDIF without changing the supplied identities or mail addresses. Node2 must be
    able to search the people subtree and find both users. Directory updates require
    an authenticated administrator; anonymous writes should fail. The directory
    export is in /srv/legacy2/ldap-directory-import.
    ''', 'LDAP schema and LDIF import, absent from legacy.', {
    'directory.ldif': r'''dn: dc=branch,dc=test
        objectClass: top
        objectClass: domain
        dc: branch

        dn: ou=people,dc=branch,dc=test
        objectClass: organizationalUnit
        ou: people

        dn: uid=alex,ou=people,dc=branch,dc=test
        objectClass: inetOrgPerson
        uid: alex
        cn: Alex North
        sn: North
        mail: alex@branch.test

        dn: uid=sam,ou=people,dc=branch,dc=test
        objectClass: inetOrgPerson
        uid: sam
        cn: Sam West
        sn: West
        mail: sam@branch.test
        '''}, nodes=2)

add('ldap-attribute-privacy', 'identity', '''
    The HR directory needs field-level privacy. Load the supplied LDIF into LDAP on
    node1. The directory-reader identity must be able to search employee names and
    mail addresses from node2, but only the HR administrator may read or change the
    employeeNumber attribute. Anonymous users should see no employee records.
    Retain the supplied records in /srv/legacy2/ldap-attribute-privacy; provision
    dedicated demonstration credentials for the reader and administrator.
    ''', 'LDAP attribute-level authorization, not host permissions or LDAP import alone.', {
    'hr.ldif': r'''dn: dc=hr,dc=test
        objectClass: top
        objectClass: domain
        dc: hr

        dn: uid=morgan,dc=hr,dc=test
        objectClass: inetOrgPerson
        uid: morgan
        cn: Morgan Lake
        sn: Lake
        mail: morgan@hr.test
        employeeNumber: HR-4815
        '''}, nodes=2)

add('kerberos-service-identity', 'identity', '''
    Establish the BRANCH.TEST Kerberos realm on node1 for a legacy application on
    node2. Create the user principal analyst and the service principal
    reports/node2.branch.test, with a keytab for the application on node2. An analyst
    should be able to obtain a ticket for that service; the application keytab must
    validate the service ticket. Keep the principal ownership notes under
    /srv/legacy2/kerberos-service-identity intact.
    ''', 'Kerberos ticket issuance and keytab service identity, not SSH keys or a CA.', {
    'principals.tsv': 'principal\towner\nanalyst\tReporting team\nreports/node2.branch.test\tReport application\n',
    'realm-notes.txt': 'Realm BRANCH.TEST; KDC on node1; report service on node2.\n'}, nodes=2)

add('radius-network-authentication', 'identity', '''
    A legacy access concentrator on node2 needs RADIUS authentication from node1.
    Configure a dedicated client secret and the demonstration user in access.txt.
    Correct credentials should receive Access-Accept, wrong credentials Access-Reject,
    and requests with the wrong client secret should not be accepted. Keep the
    handover in /srv/legacy2/radius-network-authentication intact.
    ''', 'RADIUS protocol authentication and client secrets, absent from legacy.', {
    'access.txt': 'Demonstration user: branch-user\nDemonstration password: RadiusDemo-2704\n',
    'client-notes.txt': 'node2 represents the branch concentrator; node1 is the RADIUS server.\n'}, nodes=2)

add('snmp-readonly-monitoring', 'monitoring', '''
    The monitoring station on node2 needs SNMPv2c access to node1 using the
    demonstration community branch-readonly. Expose system identity and uptime,
    with sysLocation set to West Branch and sysContact set to ops@branch.test.
    The community must permit reads but reject writes. Preserve the asset register
    in /srv/legacy2/snmp-readonly-monitoring.
    ''', 'SNMP management objects and read-only community access, not log collection.', {
    'asset-register.csv': 'asset,location,contact\nbranch-server,West Branch,ops@branch.test\n'}, nodes=2)

add('smtp-alias-delivery', 'mail', '''
    Restore local mail delivery for branch.test on node1. Mail sent from node2 to
    helpdesk@branch.test should reach both the alice and bob local mailboxes;
    accounts@branch.test should reach bob only. Unknown recipients should be rejected,
    and relaying for unrelated domains should be rejected. Preserve the
    sample messages and routing handover in /srv/legacy2/smtp-alias-delivery.
    ''', 'SMTP recipient routing and relay boundaries, not any existing legacy service.', {
    'aliases.txt': 'helpdesk: alice,bob\naccounts: bob\n',
    'sample.eml': 'From: sender@branch.test\nTo: helpdesk@branch.test\nSubject: Branch case 42\nMessage-ID: <case42@branch.test>\n\nThe printer needs paper.\n'}, nodes=2)

add('imap-maildir-cutover', 'mail', '''
    Move the staged archive mailbox into a working IMAP service on node1 for the
    archive account. Node2 should be able to authenticate and retrieve both messages,
    preserving their Message-ID values, bodies, and the read/unread state described
    in mailbox.tsv. The supplied mailbox under /srv/legacy2/imap-maildir-cutover is
    the only copy and must remain intact. Use a dedicated demonstration password.
    ''', 'Mailbox migration with message flags and IMAP access, not file copying alone.', {
    'mailbox.tsv': 'file\tstate\none.eml\tread\ntwo.eml\tunread\n',
    'maildir/cur/one.eml': 'From: desk@branch.test\nTo: archive@branch.test\nMessage-ID: <one@branch.test>\nSubject: Arrival\n\nShipment arrived.\n',
    'maildir/new/two.eml': 'From: desk@branch.test\nTo: archive@branch.test\nMessage-ID: <two@branch.test>\nSubject: Departure\n\nShipment departed.\n'}, nodes=2)

add('mail-filter-routing', 'mail', '''
    Restore the node1 mail-processing entry point bin/deliver beneath
    /srv/legacy2/mail-filter-routing. It reads one RFC822 message from standard input.
    Messages whose X-Department header is accounts belong in Maildir/accounts/new;
    messages tagged support belong in Maildir/support/new; everything else belongs
    in Maildir/general/new. Match header names without case sensitivity and leave
    each delivered message byte-for-byte intact. Messages with repeated subjects must remain separate deliveries. Retain the staged samples.
    ''', 'Header-driven mail filtering and collision-free delivery, not SMTP alias expansion.', {
    'bin/deliver': r'''#!/bin/sh
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        mkdir -p "$base/Maildir/general/new"
        cat > "$base/Maildir/general/new/message"
        ''',
    'samples/accounts.eml': 'From: finance@branch.test\nX-Department: accounts\nSubject: Monthly update\n\nInvoice 88.\n',
    'samples/support.eml': 'From: customer@branch.test\nx-department: support\nSubject: Monthly update\n\nCase 88.\n',
    'samples/general.eml': 'From: office@branch.test\nSubject: Monthly update\n\nOffice notice.\n'})

add('mail-spool-deduplication', 'mail', '''
    A restored mail spool on node1 contains duplicate queue entries. Repair bin/replay
    under /srv/legacy2/mail-spool-deduplication so it recovers the pending messages
    into delivered/, once per Message-ID, without losing distinct messages that have
    the same subject. Re-running recovery must skip messages already recorded in delivered/index.tsv. Preserve the original spool and the already-delivered
    message; malformed messages belong in quarantine with an explanation.
    ''', 'Durable mail queue replay and Message-ID deduplication, not scheduled backup.', {
    'bin/replay': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        mkdir -p "$base/delivered"
        for message in "$base"/spool/*.eml; do
            cp "$message" "$base/delivered/latest.eml"
        done
        ''',
    'spool/a.eml': 'Message-ID: <a@branch.test>\nSubject: Notice\n\nFirst notice.\n',
    'spool/a-copy.eml': 'Message-ID: <a@branch.test>\nSubject: Notice\n\nFirst notice.\n',
    'spool/b.eml': 'Message-ID: <b@branch.test>\nSubject: Notice\n\nSecond notice.\n',
    'spool/bad.eml': 'Subject: Broken queue entry\n\nNo message identifier.\n',
    'delivered/index.tsv': 'message_id\tfile\n<old@branch.test>\told.eml\n',
    'delivered/old.eml': 'Message-ID: <old@branch.test>\nSubject: Earlier\n\nAlready delivered.\n'})

add('forward-proxy-destination-policy', 'web', '''
    Node2 needs an HTTP forward proxy on node1, TCP port 3128, for the legacy document
    origin running on node2. Permit requests to that origin on TCP port 8081 and
    reject other destination ports, including CONNECT tunnels. The staged origin
    application in /srv/legacy2/forward-proxy-destination-policy serves the approved
    handbook. Preserve it and make it reachable through the proxy from node2.
    ''', 'Forward-proxy destination authorization, not reverse-proxy load balancing.', {
    'origin/handbook.txt': 'Approved branch handbook, revision 3.\n',
    'origin/serve.py': r'''import os
        try:
            import SimpleHTTPServer as http
            import SocketServer as server
        except ImportError:
            import http.server as http
            import socketserver as server
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        server.TCPServer.allow_reuse_address = True
        server.TCPServer(('', 8081), http.SimpleHTTPRequestHandler).serve_forever()
        '''}, nodes=2)

add('selective-tape-restore', 'recovery', '''
    On node1, restore the missing invoices named in restore-request.txt from the
    supplied tar archive into live/. The live directory also contains a newer
    customer register that must retain its current contents. Recover the requested
    invoice bytes and file modes without restoring unrelated archived files.
    The archive and live data are under /srv/legacy2/selective-tape-restore.
    ''', 'Selective archive recovery around newer live data, not filesystem snapshot rollback.', {
    'restore-request.txt': 'invoices/INV-100.txt\ninvoices/INV-101.txt\n',
    'live/customers.csv': 'id,name\nC100,North Branch Ltd\nC101,New Customer Ltd\n'}, archives={
    'tapes/friday.tar': {'invoices/INV-100.txt': 'Invoice 100: 125.00\n',
        'invoices/INV-101.txt': 'Invoice 101: 240.00\n',
        'customers.csv': 'id,name\nC100,North Branch Ltd\n',
        'old-notes.txt': 'Obsolete archived notes.\n'}})

add('incremental-archive-chain', 'recovery', '''
    Reconstruct the shipping workspace on node1 from the base archive and ordered
    change archives under /srv/legacy2/incremental-archive-chain. Each change archive
    contains replacement files; its deletions.txt records paths removed at that stage.
    The recovered/ tree must represent the end of day 3, including deletions and the
    latest version of changed files. Preserve all recovery media and the order
    documented in chain.txt.
    ''', 'Ordered incremental archive replay with tombstones, not a live filesystem snapshot.', {
    'chain.txt': 'base.tar\nday2.tar\nday3.tar\n'}, archives={
    'base.tar': {'dispatch.txt': 'dispatch=Monday\n', 'obsolete.txt': 'Old route\n', 'retain.txt': 'Shipping policy remains current.\n'},
    'day2.tar': {'dispatch.txt': 'dispatch=Tuesday\n', 'route.txt': 'route=west\n', 'deletions.txt': 'obsolete.txt\n'},
    'day3.tar': {'dispatch.txt': 'dispatch=Wednesday\n', 'deletions.txt': 'route.txt\n'}})

add('archive-member-safety', 'recovery', '''
    Repair bin/unpack on node1 so supplier tar packages can be unpacked into incoming/
    without writing outside that directory. Ordinary nested files should be accepted;
    packages with absolute paths, parent traversal, or symlink-based escapes should
    be rejected before any members are installed. The packages under
    /srv/legacy2/archive-member-safety include normal and malformed deliveries.
    Preserve those source packages and the sibling protected/ files.
    ''', 'Safe archive ingestion and all-or-nothing rejection, not integrity monitoring.', {
    'bin/unpack': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        mkdir -p "$base/incoming"
        tar -xf "$1" -C "$base/incoming"
        ''',
    'protected/customer.txt': 'Original customer agreement.\n'}, archives={
    'packages/normal.tar': {'docs/notice.txt': 'Supplier notice.\n'},
    'packages/traversal.tar': {'accepted.txt': 'Must not be partially installed.\n', '../protected/customer.txt': 'Unapproved replacement.\n'},
    'packages/absolute.tar': {'/outside.txt': 'Absolute member.\n'},
    'packages/symlink.tar': {'escape': {'symlink': '../protected'}, 'escape/customer.txt': 'Unapproved replacement.\n'}})

add('hardlink-aware-deduplication', 'storage', '''
    Reclaim duplicate payload storage in the release-cache/ tree on node1 beneath
    /srv/legacy2/hardlink-aware-deduplication. Identical immutable payload files with
    matching ownership and mode may share an inode. Preserve every pathname, byte,
    and mode, keep files with different permissions independent, and leave mutable/
    files independently writable. A later cache pass should make no further changes.
    ''', 'Inode sharing for immutable duplicates, not quotas, LVM, or permissions repair.', {
    'release-cache/r1/payload.dat': 'Identical immutable payload.\n' * 64,
    'release-cache/r2/payload.dat': 'Identical immutable payload.\n' * 64,
    'release-cache/r2/different.dat': 'A genuinely different payload.\n',
    'release-cache/private.dat': 'Identical immutable payload.\n' * 64,
    'mutable/active.dat': 'Identical immutable payload.\n' * 64})

add('filename-encoding-migration', 'storage', '''
    Convert the staged Latin-1 filenames in imported/ on node1 into UTF-8 filenames
    under converted/, retaining their directory structure and file contents. The
    export and its filename inventory are under /srv/legacy2/filename-encoding-migration.
    Preserve the imported tree. A collision with an existing UTF-8 destination must
    be reported without overwriting that destination or silently dropping a source.
    ''', 'Filename byte-encoding conversion and collision handling, absent from legacy.', {
    'inventory.txt': 'Source encoding: ISO-8859-1\nNames include caf\u00e9.txt and r\u00e9sum\u00e9.txt.\n',
    'imported/caf\u00e9.txt': 'Cafe delivery notes.\n',
    'imported/r\u00e9sum\u00e9.txt': 'Resume archive document.\n',
    'imported/plain.txt': 'Plain ASCII document.\n',
    'converted/plain.txt': 'Existing destination owned by a different department.\n'})

add('relative-symlink-relocation', 'storage', '''
    The report bundle on node1 was copied from a retired server and its absolute
    symlinks still refer to /opt/retired-reports. Repair the links in bundle/ under
    /srv/legacy2/relative-symlink-relocation so the bundle works in its current
    location and when copied to another directory. Preserve the regular files and
    the intended targets recorded in links.tsv; links must remain links.
    ''', 'Relocatable symlink graph repair, not a service chroot or ownership repair.', {
    'bundle/releases/one/report.txt': 'Report release one\n',
    'bundle/releases/two/report.txt': 'Report release two\n',
    'links.tsv': 'link\ttarget_inside_bundle\ncurrent\treleases/two\nlatest-report\treleases/two/report.txt\n'},
    links={'bundle/current': '/opt/retired-reports/releases/two',
           'bundle/latest-report': '/opt/retired-reports/releases/two/report.txt'})

add('sparse-image-copy', 'storage', '''
    The node1 disk-image transfer utility bin/copy-image consumes the full logical
    size of sparse files. Repair it so copying source.img to a chosen destination
    retains the logical length and bytes while preserving holes: the supplied
    64 MiB image should occupy less than 2 MiB of allocated space at the destination.
    Keep source.img intact and make repeated copying safe. The utility and image
    are in /srv/legacy2/sparse-image-copy.
    ''', 'Sparse-file allocation preservation, not provisioning LVM, swap, or encryption.', {
    'bin/copy-image': r'''#!/bin/sh
        set -eu
        cat "$1" > "$2"
        ''',
    'image-layout.txt': 'Logical length: 67108864 bytes. Payload at the beginning and end; holes between.\n'})

add('atomic-release-publication', 'storage', '''
    Repair the release publisher on node1 under /srv/legacy2/atomic-release-publication.
    bin/publish takes a release directory and updates current to expose that complete
    release. Concurrent readers must see either the complete previous release or the
    complete new one, with the current path continuously present and complete. Refuse a release missing
    MANIFEST and retain the previous current target on rejection. Preserve both
    staged releases and keep rollback to either release possible.
    ''', 'Atomic directory publication and rejected-release rollback, not snapshot recovery.', {
    'bin/publish': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        rm -f "$base/current"
        sleep 1
        ln -s "$1" "$base/current"
        ''',
    'releases/one/MANIFEST': 'release=one\n',
    'releases/one/index.txt': 'Complete release one.\n',
    'releases/two/MANIFEST': 'release=two\n',
    'releases/two/index.txt': 'Complete release two.\n',
    'releases/incomplete/index.txt': 'Missing manifest.\n'}, links={'current': 'releases/one'})

add('text-export-normalization', 'data-processing', '''
    The node1 records pipeline needs UTF-8 text with LF line endings. Convert the
    files in incoming/ according to encodings.tsv, writing matching filenames into
    normalized/. Preserve accented characters, empty records, and the final newline
    state. Report undecodable input without silently replacing characters or
    publishing a partial output. Keep all source files in
    /srv/legacy2/text-export-normalization intact.
    ''', 'Content encoding and newline normalization, distinct from filename migration.', {
    'encodings.tsv': 'file\tencoding\nwestern.txt\tISO-8859-1\nutf8.txt\tUTF-8\ninvalid.txt\tUTF-8\n',
    'incoming/western.txt': 'caf\u00e9\r\n\r\nr\u00e9sum\u00e9\r\n',
    'incoming/utf8.txt': 'na\u00efve\r\nlast record',
    'incoming/invalid.txt': 'invalid-byte-placeholder'})

add('numeric-record-ordering', 'data-processing', '''
    Repair bin/merge on node1 to merge the staged transaction exports into merged.csv.
    Order records by the numeric transaction_id, retain quoted fields containing
    commas, and emit one header. Duplicate IDs with identical data should collapse
    to one row; conflicting duplicate IDs must stop publication and explain the
    conflict. Keep the existing output intact on a failed merge. The handover is
    under /srv/legacy2/numeric-record-ordering.
    ''', 'Numeric CSV merge with conflict-safe publication, not a filesystem or service task.', {
    'bin/merge': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        cat "$@" | sort > "$base/merged.csv"
        ''',
    'exports/east.csv': 'transaction_id,description,amount\n2,"Tape, wide",12\n100,Paper,8\n',
    'exports/west.csv': 'transaction_id,description,amount\n10,Labels,7\n2,"Tape, wide",12\n',
    'conflict.csv': 'transaction_id,description,amount\n2,Tape,99\n',
    'merged.csv': 'transaction_id,description,amount\n1,Prior transaction,5\n'})

add('batch-exclusive-lock', 'batch', '''
    The reconciliation job on node1 sometimes processes the same batch twice when
    two operators start it together. Repair bin/reconcile under
    /srv/legacy2/batch-exclusive-lock so only one invocation processes pending.tsv
    at a time, each batch ID reaches ledger.tsv once, and an interrupted invocation
    does not permanently block later work. Preserve existing ledger entries and
    leave a clear result when another invocation already owns the job.
    ''', 'Concurrent batch exclusion and durable once-only ledger entries, not cron scheduling.', {
    'bin/reconcile': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        for batch in $(cat "$base/pending.tsv"); do
          if ! grep -q "^$batch$" "$base/ledger.tsv"; then
            sleep 1
            printf '%s\n' "$batch" >> "$base/ledger.tsv"
          fi
        done
        ''',
    'pending.tsv': 'B101\nB102\n', 'ledger.tsv': 'B100\n'})

add('stale-pidfile-startup', 'processes', '''
    The branch worker on node1 refuses to start after an unclean stop because it
    trusts a leftover PID file. Repair bin/control in
    /srv/legacy2/stale-pidfile-startup. Its start, stop, and status actions should
    distinguish a live worker, a stale PID, and a PID belonging to another process.
    Repeated starts should retain a single worker, and stopping it should leave
    unrelated processes running. Preserve the worker's existing journal.
    ''', 'Process identity and stale PID handling, not simply creating a managed service.', {
    'bin/control': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        case "$1" in
          start) [ ! -f "$base/run/worker.pid" ] || exit 1
                 python "$base/worker.py" & echo $! > "$base/run/worker.pid" ;;
          stop) kill "$(cat "$base/run/worker.pid")"; rm -f "$base/run/worker.pid" ;;
          status) test -f "$base/run/worker.pid" ;;
          *) exit 2 ;;
        esac
        ''',
    'worker.py': r'''import os, time
        base = os.path.dirname(os.path.abspath(__file__))
        while True:
            f = open(os.path.join(base, 'journal.txt'), 'a')
            f.write('tick\n')
            f.close()
            time.sleep(1)
        ''',
    'run/worker.pid': '99999999\n', 'journal.txt': 'previous worker completed batch B100\n'})

add('temporary-file-symlink-defense', 'batch', '''
    Repair the invoice export utility bin/export on node1 so concurrent exports use
    private temporary files and a pre-existing symlink cannot redirect its writes.
    The utility takes an output pathname and exports the supplied invoices.csv.
    Successful exports must retain all invoice rows, failures should leave the prior
    destination intact, and temporary files should be removed when the utility exits.
    The utility and a protected sentinel are under
    /srv/legacy2/temporary-file-symlink-defense; preserve the sentinel and source data.
    ''', 'Temporary-file creation races and safe publication, not file permission repair.', {
    'bin/export': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        cat "$base/invoices.csv" > "$base/tmp/export.tmp"
        cp "$base/tmp/export.tmp" "$1"
        rm -f "$base/tmp/export.tmp"
        ''',
    'invoices.csv': 'invoice,total\nI100,25\nI101,35\n',
    'protected.txt': 'This file is not export scratch space.\n'},
    links={'tmp/export.tmp': '../protected.txt'})

add('posix-shell-installer', 'batch', '''
    The branch report installer was written for Bash but is invoked through the
    system /bin/sh on node1. Make bin/install-report work under POSIX sh, including
    when the destination path contains spaces. It should install both supplied
    templates with their contents intact, make the launcher executable, and report
    failure when the destination cannot be populated. Repeating installation should
    be safe. The bundle is in /srv/legacy2/posix-shell-installer.
    ''', 'Shell dialect portability and quoted path handling, not scheduled maintenance.', {
    'bin/install-report': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        files=(summary.txt detail.txt)
        mkdir -p $1
        for file in "${files[@]}"; do cp "$base/templates/$file" $1/; done
        cp "$base/launcher" $1/run-report
        chmod +x $1/run-report
        ''',
    'templates/summary.txt': 'Daily summary template\n',
    'templates/detail.txt': 'Detailed report template\n',
    'launcher': '#!/bin/sh\nprintf "report launcher ready\\n"\n'})

add('minimal-environment-job', 'batch', '''
    bin/render on node1 works in the developer's login shell but fails in the batch
    environment. Repair it so it can run with an empty environment except for
    PATH=/usr/bin:/bin, from any working directory. It should find the supplied
    branch-format helper and templates, write the requested output file, and retain
    the report contents. The application lives under
    /srv/legacy2/minimal-environment-job; preserve its source template.
    ''', 'Explicit dependency discovery under a minimal environment, not cron timing or process limits.', {
    'bin/render': r'''#!/bin/sh
        set -eu
        branch-format < templates/report.txt > "$1"
        ''',
    'libexec/branch-format': '#!/bin/sh\nprintf "BRANCH REPORT\\n"\ncat\n',
    'templates/report.txt': 'Region: west\nShipments: 17\n'})

add('signal-driven-config-reload', 'processes', '''
    Repair the node1 status writer so SIGHUP reloads message.conf without terminating
    the process or creating a second writer. It should continue appending the current
    message to journal.txt, reject an empty configuration while retaining the last
    valid message, and exit cleanly on SIGTERM. The application is worker.py beneath
    /srv/legacy2/signal-driven-config-reload. Preserve the existing journal entries.
    ''', 'In-process signal handling and invalid-reload retention, not service enablement.', {
    'worker.py': r'''import os, time
        base = os.path.dirname(os.path.abspath(__file__))
        message = open(os.path.join(base, 'message.conf')).read().strip()
        while True:
            f = open(os.path.join(base, 'journal.txt'), 'a')
            f.write(message + '\n')
            f.close()
            time.sleep(1)
        ''',
    'message.conf': 'branch status: open\n', 'journal.txt': 'branch status: opening\n'})

add('child-process-reaping', 'processes', '''
    The node1 job supervisor leaves finished child processes behind. Repair
    supervisor.py under /srv/legacy2/child-process-reaping so it starts the requested
    number of short jobs, reaps every child, and records each job's exit status in
    results.tsv. Jobs numbered with an even integer succeed; odd-numbered jobs exit
    with status 3. Preserve the previous results and keep the supervisor available
    until its children have finished.
    ''', 'Child lifecycle and exit-status accounting, not resource limits or daemon startup.', {
    'supervisor.py': r'''import os, sys, time
        base = os.path.dirname(os.path.abspath(__file__))
        for number in range(int(sys.argv[1])):
            pid = os.fork()
            if pid == 0:
                time.sleep(0.1)
                os._exit((number % 2) * 3)
        time.sleep(15)
        ''',
    'results.tsv': 'run,job,exit_status\nprevious,0,0\n'})

add('file-descriptor-leak', 'processes', '''
    The node1 document reader exhausts file descriptors during large batches. Repair
    bin/read-documents.py beneath /srv/legacy2/file-descriptor-leak so it can process
    at least 500 successive reads with a soft open-file limit of 64, returning the
    same document length for every read and closing resources on failed opens too.
    Keep the supplied document unchanged and retain the command's count argument.
    ''', 'Fixing descriptor lifetime rather than increasing service resource limits.', {
    'bin/read-documents.py': r'''import os, sys
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        handles = []
        for number in range(int(sys.argv[1])):
            f = open(os.path.join(base, 'document.txt'))
            handles.append(f)
            sys.stdout.write(str(len(f.read())) + '\n')
        ''',
    'document.txt': 'Reference document for branch processing.\n'})

add('working-directory-independent-launch', 'processes', '''
    Repair bin/start-report on node1 so the report application loads its own
    config/report.conf regardless of the caller's working directory. A caller's
    unrelated file with the same relative name should have no effect on the application
    configuration. Preserve the existing configuration and business output in
    /srv/legacy2/working-directory-independent-launch. The launcher should propagate
    application errors to its caller rather than reporting success.
    ''', 'Executable-relative configuration resolution and exit propagation, distinct from PATH repair.', {
    'bin/start-report': r'''#!/bin/sh
        python app.py
        exit 0
        ''',
    'app.py': r'''import sys
        config = open('config/report.conf').read()
        sys.stdout.write(config)
        ''',
    'config/report.conf': 'region=west\nreport=weekly\n',
    'other-directory/config/report.conf': 'region=wrong-caller-directory\n'})

add('large-counter-overflow', 'data-processing', '''
    The node1 billing accumulator produces negative totals when a byte counter exceeds
    the signed 32-bit range. Repair bin/total.py in
    /srv/legacy2/large-counter-overflow to sum nonnegative decimal counters exactly,
    including totals larger than 4 GiB, and reject invalid or negative records without
    publishing a partial total. Keep the counters and the integer-decimal output
    interface intact. The same program must work on the installed system architecture.
    ''', 'Architecture-sensitive integer overflow in accounting, not disk allocation or quotas.', {
    'bin/total.py': r'''import sys, struct
        total = 0
        for line in open(sys.argv[1]):
            total = (total + int(line.strip())) & 0xffffffff
        total = struct.unpack('i', struct.pack('I', total))[0]
        sys.stdout.write(str(total) + '\n')
        ''',
    'counters.txt': '2147483647\n2147483647\n9\n',
    'invalid.txt': '100\n-2\nnot-a-counter\n'})

add('mysql-relational-import', 'databases', '''
    Restore the branch orders database on node1 from the supplied MySQL SQL export
    under /srv/legacy2/mysql-relational-import. Keep customer/order relationships,
    exact monetary values, and the supplied primary keys. Provide a reporting account
    that can read the orders and customers from node2 but cannot change them; the
    database administrator should retain write access. Preserve the export.
    ''', 'Relational import with a read-only database client, absent from legacy.', {
    'orders.sql': r'''CREATE DATABASE branch_orders;
        USE branch_orders;
        CREATE TABLE customers (id INTEGER PRIMARY KEY, name VARCHAR(80) NOT NULL) ENGINE=InnoDB;
        CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, amount DECIMAL(10,2) NOT NULL, FOREIGN KEY(customer_id) REFERENCES customers(id)) ENGINE=InnoDB;
        INSERT INTO customers VALUES (10,'North Branch'),(20,'West Branch');
        INSERT INTO orders VALUES (101,10,12.35),(102,20,99.90),(103,10,0.05);
        '''}, nodes=2)

add('postgresql-sequence-repair', 'databases', '''
    The branch ticket export on node1 restores explicit IDs but leaves its PostgreSQL
    sequence behind, causing subsequent inserts to collide. Restore the supplied
    tickets.sql into a PostgreSQL database named helpdesk and repair ID allocation.
    Existing tickets must keep their IDs and text; new tickets without an explicit
    ID must receive unique IDs greater than the imported maximum. Preserve the source
    export under /srv/legacy2/postgresql-sequence-repair.
    ''', 'PostgreSQL sequence state after bulk restore, not generic file restoration.', {
    'tickets.sql': r'''CREATE TABLE tickets (id SERIAL PRIMARY KEY, subject TEXT NOT NULL);
        INSERT INTO tickets(id,subject) VALUES (1,'Printer queue');
        INSERT INTO tickets(id,subject) VALUES (2,'Scanner cable');
        INSERT INTO tickets(id,subject) VALUES (100,'Office move');
        '''})

add('database-reader-writer-roles', 'databases', '''
    Deploy the supplied PostgreSQL stock schema as branch_stock on node1. The stock_app
    role on node2 needs to read and update stock quantities but not change schema or
    read supplier_costs. The auditor role needs read-only access to stock and
    supplier_costs. Establish separate credentials for those roles and preserve the
    supplied records in /srv/legacy2/database-reader-writer-roles.
    ''', 'Table-specific database privileges and schema boundaries, not OS group access.', {
    'stock.sql': r'''CREATE TABLE stock (sku VARCHAR(20) PRIMARY KEY, quantity INTEGER NOT NULL);
        CREATE TABLE supplier_costs (sku VARCHAR(20) PRIMARY KEY, cost NUMERIC(10,2) NOT NULL);
        INSERT INTO stock VALUES ('PAPER',40);
        INSERT INTO stock VALUES ('LABELS',18);
        INSERT INTO supplier_costs VALUES ('PAPER',3.25);
        INSERT INTO supplier_costs VALUES ('LABELS',1.75);
        '''}, nodes=2)

add('mysql-replication-catchup', 'databases', '''
    Restore the staged branch ledger on node1 as a MySQL database and establish node2
    as a read-only application replica. Committed inserts on node1 should arrive on
    node2. After a short replica disconnect, it must catch up without losing or
    duplicating ledger rows. Use a replication-only account, retain the original
    ledger IDs and amounts, and preserve the export in
    /srv/legacy2/mysql-replication-catchup. Node1 remains the sole application writer.
    ''', 'Database log replication and catch-up, not file synchronization or NFS.', {
    'ledger.sql': r'''CREATE DATABASE branch_ledger;
        USE branch_ledger;
        CREATE TABLE entries (id INTEGER PRIMARY KEY, amount DECIMAL(12,2) NOT NULL) ENGINE=InnoDB;
        INSERT INTO entries VALUES (1001,12.50),(1002,-3.25);
        '''}, nodes=2)

add('transactional-schema-upgrade', 'databases', '''
    The SQLite catalog application on node1 needs a schema upgrade from v1 to v2.
    Repair bin/upgrade.py to retain the existing IDs and descriptions, add a
    nonnegative price_cents field initialized to zero, and advance schema_version
    only after the whole upgrade succeeds. It must be safe to repeat and leave the
    v1 database usable if an upgrade fails. The v1 database and faulty migration
    are under /srv/legacy2/transactional-schema-upgrade.
    ''', 'Atomic database schema migration and version gating, not snapshot rollback.', {
    'schema.sql': r'''CREATE TABLE schema_version (version INTEGER NOT NULL);
        INSERT INTO schema_version VALUES (1);
        CREATE TABLE products (id INTEGER PRIMARY KEY, description TEXT NOT NULL);
        INSERT INTO products VALUES (1,'Paper');
        INSERT INTO products VALUES (2,'Tape');
        ''',
    'bin/upgrade.py': r'''import os, sqlite3
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db = sqlite3.connect(os.path.join(base, 'catalog.db'))
        db.execute('UPDATE schema_version SET version=2')
        db.commit()
        db.execute('ALTER TABLE products ADD COLUMN price_cents INTEGER NOT NULL')
        db.commit()
        db.close()
        '''})

add('sqlite-lock-contention', 'databases', '''
    The local reservation utility on node1 fails or loses changes when two clients
    reserve stock at once. Repair bin/reserve.py beneath
    /srv/legacy2/sqlite-lock-contention. A request takes a unique request ID and
    positive quantity; successful requests decrement remaining stock exactly once.
    Repeating a successful ID should return its earlier result, insufficient stock
    should be rejected, and competing requests must keep remaining stock nonnegative. Preserve existing
    reservations and use bounded lock waits rather than hanging indefinitely.
    ''', 'Database transaction isolation and request idempotency, not a shell job lock.', {
    'schema.sql': r'''CREATE TABLE stock (id INTEGER PRIMARY KEY, remaining INTEGER NOT NULL);
        INSERT INTO stock VALUES (1,5);
        CREATE TABLE reservations (request_id TEXT PRIMARY KEY, quantity INTEGER NOT NULL);
        INSERT INTO reservations VALUES ('previous-request',2);
        ''',
    'bin/reserve.py': r'''import os, sys, sqlite3, time
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db = sqlite3.connect(os.path.join(base, 'stock.db'), timeout=0)
        remaining = db.execute('SELECT remaining FROM stock WHERE id=1').fetchone()[0]
        quantity = int(sys.argv[2])
        time.sleep(1)
        db.execute('UPDATE stock SET remaining=? WHERE id=1', (remaining-quantity,))
        db.execute('INSERT INTO reservations VALUES (?,?)', (sys.argv[1], quantity))
        db.commit()
        db.close()
        '''})

add('cross-file-accounting-reconciliation', 'data-processing', '''
    Repair the node1 settlement utility bin/reconcile.py in
    /srv/legacy2/cross-file-accounting-reconciliation. Join payments.csv to invoices.csv
    by invoice ID, account for multiple payments and credit amounts exactly in cents,
    and publish balances.csv with invoice_id and outstanding_cents. Unknown invoice
    IDs and malformed amounts belong in rejected.csv with a reason. Preserve the
    source files and avoid counting a duplicate payment_id twice.
    ''', 'Financial record reconciliation with rejects, distinct from numeric record ordering.', {
    'invoices.csv': 'invoice_id,total_cents\nI100,1250\nI101,990\nI102,150\n',
    'payments.csv': 'payment_id,invoice_id,amount_cents\nP1,I100,500\nP2,I100,750\nP3,I101,-10\nP3,I101,-10\nP4,UNKNOWN,100\nP5,I102,bad\n',
    'bin/reconcile.py': r'''import os, csv
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        f = open(os.path.join(base, 'balances.csv'), 'w')
        f.write('invoice_id,outstanding_cents\n')
        for row in list(csv.reader(open(os.path.join(base, 'invoices.csv'))))[1:]:
            f.write(','.join(row) + '\n')
        f.close()
        '''})

add('timezone-log-merge', 'data-processing', '''
    The node1 incident timeline merges branch logs from different time zones and gets
    the event order wrong. Repair bin/timeline.py beneath /srv/legacy2/timezone-log-merge
    to write timeline.tsv in UTC chronological order from the supplied timestamped
    events. Honor each record's explicit numeric UTC offset, retain event IDs and
    messages, and use event ID as the tie-breaker. Preserve all source logs and put
    invalid timestamps in rejected.tsv instead of guessing their time zone.
    ''', 'Timestamp normalization across offsets, not configuring an NTP service or log forwarding.', {
    'logs/east.tsv': '2026-10-01T09:00:00-0400\tE1\tdoor opened\n2026-10-01T10:00:00-0400\tE3\ttruck departed\n',
    'logs/west.tsv': '2026-10-01T06:30:00-0700\tE2\ttruck arrived\ninvalid\tE4\tclock fault\n',
    'bin/timeline.py': r'''import sys
        lines = []
        for name in sys.argv[1:]:
            lines.extend(open(name).readlines())
        lines.sort()
        sys.stdout.writelines(lines)
        '''})

add('privacy-safe-support-export', 'data-processing', '''
    Repair the support-bundle exporter on node1. Its output should retain timestamps,
    event types, and ticket IDs while replacing every email address and auth_token
    value with [REDACTED]. Include logs in nested directories and reject symlinks
    that lead outside logs/. Source logs and the private sibling file under
    /srv/legacy2/privacy-safe-support-export must remain unchanged. The entry point
    bin/export takes the output directory as its argument.
    ''', 'Sensitive-field removal at a support export boundary, not file-integrity monitoring.', {
    'bin/export': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        mkdir -p "$1"
        cp -R "$base/logs/." "$1/"
        ''',
    'logs/app.log': '2026-10-01T12:00Z login ticket=T100 email=alex@branch.test auth_token=DEMO-ALPHA\n',
    'logs/archive/events.log': '2026-10-01T12:01Z update ticket=T101 user=sam@branch.test auth_token=DEMO-BETA\n',
    'private.txt': 'Private operational note outside the support export.\n'},
    links={'logs/private-link': '../private.txt'})

add('fixed-width-import-recovery', 'data-processing', '''
    The node1 warehouse importer drops records with leading-zero IDs and treats
    padded names incorrectly. Repair bin/import.py to convert the staged fixed-width
    records into CSV with id, name, and quantity columns. The layout is documented
    in layout.txt; preserve ID strings, trim only right-hand name padding, and reject
    wrong-length or nonnumeric quantity records into rejects.txt with their line
    number. Preserve the original input in /srv/legacy2/fixed-width-import-recovery.
    ''', 'Legacy fixed-width record parsing and recoverable rejects, not CSV merge ordering.', {
    'layout.txt': 'ASCII records, excluding LF: id 5 characters; name 12 characters; quantity 4 decimal digits. Total width 21.\n',
    'input.dat': '00007Paper       0042\n00100Tape        0008\n00009Labels      BAD!\nshort\n',
    'bin/import.py': r'''import sys
        sys.stdout.write('id,name,quantity\n')
        for line in open(sys.argv[1]):
            fields = line.split()
            sys.stdout.write(','.join(fields) + '\n')
        '''})

add('inherited-directory-acls', 'storage', '''
    The project handoff on node1 requires inherited access, not just a one-time
    permission repair. Under /srv/legacy2/inherited-directory-acls/projects, new
    subdirectories and documents created by designer must be readable and writable
    by reviewer, while visitor has no access. Keep designer as the owner of its
    new files and preserve the existing project contents. Provision the three local
    accounts and make the inheritance work without a periodic permission-fixing job.
    ''', 'Default POSIX ACL inheritance for future objects, not the existing fixed-tree ownership repair.', {
    'projects/brief.txt': 'Existing project handoff: refit the support room.\n',
    'roles.txt': 'designer creates; reviewer collaborates; visitor is outside the project.\n'})

add('deleted-open-file-recovery', 'processes', '''
    The node1 audit writer can hold disk space after its output file has been removed.
    Repair writer.py under /srv/legacy2/deleted-open-file-recovery so it can reopen
    audit.log on SIGHUP, release its old file descriptor, and continue writing to
    the current path without restarting the process. Preserve the existing archive
    records. The writer must also close its log and exit cleanly on SIGTERM.
    ''', 'Releasing an unlinked open inode through log reopen, not rotation retention policy.', {
    'writer.py': r'''import os, time
        base = os.path.dirname(os.path.abspath(__file__))
        log = open(os.path.join(base, 'audit.log'), 'a')
        while True:
            log.write('audit heartbeat\n')
            log.flush()
            time.sleep(1)
        ''',
    'archive/previous.log': 'Previously archived audit event A100.\n',
    'audit.log': 'Current audit event A101.\n'})

add('inode-cache-retention', 'storage', '''
    The node1 thumbnail cache contains hundreds of obsolete tiny files. Repair
    bin/prune so it removes only cache entries absent from active.txt and older than
    the cutoff epoch supplied as its argument. Keep active entries, newer inactive
    entries, non-cache files, and the source media unchanged; symbolic links should
    be handled as links rather than followed. The fixture and timestamp policy are
    in /srv/legacy2/inode-cache-retention.
    ''', 'Age-and-reference-aware inode reclamation, not disk quotas or log rotation.', {
    'bin/prune': r'''#!/bin/sh
        set -eu
        base=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
        find "$base/cache" -type f -mtime +7 -delete
        ''',
    'active.txt': 'keep-active.thumb\n',
    'cache/keep-active.thumb': 'Active old thumbnail.\n',
    'cache/keep-new.thumb': 'Inactive but recent thumbnail.\n',
    'cache/README': 'Cache metadata, not a thumbnail.\n',
    'media/original.txt': 'Original media is retained.\n',
    'policy.txt': 'Thumbnail suffix: .thumb\nOld epoch: 1700000000\nNew epoch: 1800000000\n'},
    links={'cache/media-link.thumb': '../media/original.txt'})

add('fifo-worker-reconnection', 'processes', '''
    The node1 FIFO consumer exits when its first producer disconnects. Repair
    consumer.py in /srv/legacy2/fifo-worker-reconnection so successive producers can
    submit newline-delimited job IDs through jobs.fifo without restarting the
    consumer. Record each complete line in received.txt, ignore empty lines, and
    avoid a busy loop when no producer is connected. Retain the previous records
    and provide a clean SIGTERM shutdown.
    ''', 'FIFO EOF and producer reconnection, not TCP services or scheduled jobs.', {
    'consumer.py': r'''import os
        base = os.path.dirname(os.path.abspath(__file__))
        source = open(os.path.join(base, 'jobs.fifo'))
        target = open(os.path.join(base, 'received.txt'), 'a')
        for line in source:
            target.write(line)
            target.flush()
        source.close()
        target.close()
        ''',
    'received.txt': 'previous-job\n'})

add('unix-socket-access-boundary', 'processes', '''
    The local status service on node1 should be available only to its service owner
    statusd and members of status-readers. Repair and operate server.py using the
    Unix-domain socket run/status.sock under /srv/legacy2/unix-socket-access-boundary.
    A client sending STATUS followed by a newline should receive the supplied status
    document; other requests should receive an error. Provision status-reader and
    outsider accounts to reflect those access roles. Preserve the status document.
    ''', 'Unix-domain socket access and request boundaries, not an HTTP daemon or SSH policy.', {
    'server.py': r'''import os, socket
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base, 'run/status.sock')
        if os.path.exists(path):
            os.unlink(path)
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(path)
        os.chmod(path, 438)
        s.listen(5)
        while True:
            c, address = s.accept()
            c.recv(1024)
            c.sendall(open(os.path.join(base, 'status.txt'), 'rb').read())
            c.close()
        ''',
    'status.txt': 'branch=west\nstate=ready\n', 'run/.keep': ''})

add('inetd-request-activation', 'network-services', '''
    A legacy client on node2 expects a one-request-per-connection service on node1,
    TCP port 9097. Deploy the supplied stdio handler through inetd or xinetd so each
    connection gets its own handler process. PING followed by a newline should
    return PONG; other lines should return ERROR. Multiple sequential and concurrent
    clients must finish without leaving handler processes behind. Preserve the
    protocol notes in /srv/legacy2/inetd-request-activation.
    ''', 'Socket-activated stdio handlers and process lifetime, not a persistent HTTP worker.', {
    'handler.py': r'''import sys
        request = sys.stdin.readline().strip()
        if request == 'PING':
            sys.stdout.write('PONG\n')
        else:
            sys.stdout.write('ERROR\n')
        sys.stdout.flush()
        ''',
    'protocol.txt': 'One line per connection: PING -> PONG; all other requests -> ERROR.\n'}, nodes=2)

add('udp-meter-ingestion', 'network-services', '''
    Branch meters on node2 send UDP datagrams to node1 port 9098 in the format
    meter_id,sequence,reading. Repair and run collector.py so valid datagrams append
    to readings.csv, duplicate meter/sequence pairs are ignored, and malformed
    datagrams are recorded separately without terminating collection. Sequence and
    reading are nonnegative decimal integers. Preserve the previously recorded
    reading under /srv/legacy2/udp-meter-ingestion, including across collector restarts.
    ''', 'UDP telemetry validation and durable duplicate suppression, not syslog forwarding.', {
    'collector.py': r'''import os, socket
        base = os.path.dirname(os.path.abspath(__file__))
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('', 9098))
        while True:
            data, address = s.recvfrom(4096)
            f = open(os.path.join(base, 'readings.csv'), 'ab')
            f.write(data + '\n'.encode('ascii'))
            f.close()
        ''',
    'readings.csv': 'meter_id,sequence,reading\nwest,1,42\n',
    'samples.txt': 'west,2,43\nwest,2,43\neast,1,11\nwest,bad,44\n'}, nodes=2)

add('ssh-forced-command-ingest', 'network-services', '''
    Give the uploader on node2 an SSH key that can submit a newline-delimited batch
    to node1's ingest account but cannot run arbitrary commands, obtain a shell, or
    establish forwarding. Submitted bytes should be stored as separate files under
    /srv/legacy2/ssh-forced-command-ingest/received on node1. Preserve existing receipts
    and the sample batch. This restricted application identity is separate from
    administrative access.
    ''', 'SSH forced-command capability restriction, not generic key login or host-key pinning.', {
    'sample-batch.txt': 'shipment=S100\ncartons=4\n',
    'received/prior.txt': 'shipment=S099\ncartons=2\n',
    'application-notes.txt': 'Each completed SSH submission is a separate batch receipt.\n'}, nodes=2)

add('ssh-local-service-tunnel', 'network-services', '''
    The inventory status endpoint on node1 is intentionally bound only to loopback
    on TCP port 9081. Give node2 a persistent SSH tunnel exposing that endpoint on
    node2's loopback port 9082. Other cluster hosts should not gain direct access to
    either application listener. Preserve the supplied status document and application
    under /srv/legacy2/ssh-local-service-tunnel. The tunnel should recover after a
    brief SSH connection interruption without manual recreation.
    ''', 'Loopback-only SSH forwarding and reconnection, not remote command access.', {
    'status/index.html': '<h1>Inventory status: ready</h1>\n',
    'serve.py': r'''import os
        try:
            import SimpleHTTPServer as http
            import SocketServer as server
        except ImportError:
            import http.server as http
            import socketserver as server
        os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'status'))
        server.TCPServer.allow_reuse_address = True
        server.TCPServer(('127.0.0.1', 9081), http.SimpleHTTPRequestHandler).serve_forever()
        '''}, nodes=2)

add('http-upload-size-boundary', 'web', '''
    Repair the upload endpoint on node1 so POST /upload on TCP port 8080 accepts raw
    request bodies up to 65536 bytes and rejects larger ones with HTTP 413 before
    publishing a receipt. Each accepted upload belongs in a separate file under
    received/ with identical bytes. An interrupted request should leave no completed
    receipt, and other paths should return HTTP 404. Preserve the existing receipt
    in /srv/legacy2/http-upload-size-boundary. Node2 is the application client.
    ''', 'HTTP request-body bounds and incomplete-upload publication, not routing or load balancing.', {
    'server.py': r'''import os
        try:
            import BaseHTTPServer as http
        except ImportError:
            import http.server as http
        base = os.path.dirname(os.path.abspath(__file__))
        class Handler(http.BaseHTTPRequestHandler):
            def do_POST(self):
                data = self.rfile.read(int(self.headers.get('Content-Length', '0')))
                f = open(os.path.join(base, 'received/latest.bin'), 'wb')
                f.write(data)
                f.close()
                self.send_response(200)
                self.end_headers()
        http.HTTPServer(('', 8080), Handler).serve_forever()
        ''',
    'received/prior.bin': 'Previously accepted upload.\n'}, nodes=2)
