# Clustered service tasks

This matrix runs the same 10 clustered-service requests on 8 general-purpose
Linux operating systems. Every member of a cluster runs the same image, and the
public instruction for a task family is identical on every operating system, so
the comparison stays focused on how the executor adapts the same clustering job
to each distribution's packages, service manager, and defaults.

Unlike `multi-node-os-comparison`, which covers generic administration spread
across several systems, every task here is a named stateful service where the
hard part is cluster formation, quorum, and replication: losing a member risks
data, not just capacity.

| Task | Nodes | Shape |
|---|---:|---|
| `mariadb-galera-cluster` | 3 | Form the cluster; stays writable when a member drops and resyncs on return |
| `mariadb-galera-cold-restart` | 3 | Full shutdown for maintenance, then back with every committed write intact |
| `mariadb-galera-scale-out` | 4 | Add a fourth member to a running cluster carrying existing data |
| `postgresql-streaming-replication` | 3 | Primary plus two read-only standbys |
| `postgresql-failover` | 3 | Standby takes over when the primary is lost; old primary returns as a standby |
| `postgresql-replication-tls` | 3 | Replication over TLS from a cluster-local certificate authority |
| `rabbitmq-cluster` | 3 | Cluster with a virtual host and account; durable queue survives a node loss |
| `rabbitmq-tls` | 3 | AMQP over TLS with client certificates, management interface kept internal |
| `etcd-cluster` | 3 | Three-member cluster serving through a member outage |
| `etcd-member-replacement` | 3 | A permanently lost member is replaced and quorum restored |

Six of the ten are behavioral rather than configuration-only: the requirement is
that the cluster survives losing a member, comes back from a full shutdown,
grows, fails over, or is repaired. Those outcomes have to be demonstrated rather
than asserted from a configuration file.

Clusters use the provider's default network, since the members need to reach
each other and the internet and nothing here depends on network segmentation.

| Directory | Environment image |
|---|---|
| `almalinux9` | AlmaLinux 9 |
| `alpine` | Alpine Linux |
| `centos-stream10` | CentOS Stream 10 |
| `rhel7` | RHEL 7.9 |
| `rhel9` | RHEL 9.8 |
| `rhel10` | RHEL 10.0 |
| `ubuntu16` | Ubuntu 16.04 |
| `ubuntu24` | Ubuntu 24.04 |

MariaDB, PostgreSQL, and etcd should be reachable on every image in the matrix;
etcd in particular ships as a static binary, so it carries no libc constraint.
RabbitMQ depends on the Erlang version available to each distribution, which is
the least certain part of the matrix on the end-of-life images — an outcome
worth recording rather than designing around.

Run all 10 tasks for one operating system from the repository root:

```bash
./run-task.sh ./tasks/clustered-services/ubuntu24
```

`catalog.toml` is the source of truth for the operating systems and task
families. Regenerate the concrete task directories after editing it:

```bash
uv run --no-project --with tomli python ./scripts/generate_clustered_services_tasks.py
```
