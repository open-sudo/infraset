# What I learned running 52k sysadmin commands across 2k VMs using LLMs

Teams are already using LLMs to operate systems, with or without a human in the loop. Yet there's very little public data on the full impact of these agents on infrastructure. So I recorded traces across 804 tasks and started mining the data.

Each task execution (aka run) got a disposable cluster and a plain-language objective. 839 clusters, 2,104 full virtual machines, 52,027 recorded commands. The harness, built on [Harbor](https://github.com/harbor-framework/harbor), kept the whole timeline: what was issued, what came back, and what state was left behind. Tasks cover single-host, multi-node services, stateful clusters, and four network operating systems: VyOS, OpenWrt, SONiC and OPNsense. In another category, VyOS and OPNSense are combined in more complex networking scenario such as IPsec tunnel between a VyOS LAN and an OPNsense LAN. Clusters and network devices are provisioned through [Antrieb](https://antrieb.sh), a testbed creator I built to faclitate my experiments around LLM and Infra.

The raw data is on [GitHub](https://github.com/open-sudo/infraset) and [Hugging Face](https://huggingface.co/datasets/infraset/infraset). We welcome new tasks, runs, or mining of traces. Here's what I found, including a couple of things I had wrong going in.

*The 2,104 VMs were never running at the same time. Clusters are provisioned in small batches, on the order of 50 machines at once, and torn down when the run finishes.*

**Commands** 52,027 · **Runs scored** 804 · **VMs booted** 2,104 · **Left residue** 98.8% · **Linux distros** 8 · **Network OSes** 4 · **Cluster size** 1–4 · **VM launch** 848 ms

## Seven findings

### 01. LLMs almost always complete the job successfully

In the table below, 759 of 804 runs came back with a perfect score: every requirement met and checked against captured evidence. While the perfect-score rate varies from 100% to 86%, the success rate is 99%. A run counts as successful if it met 80% of the task's functional requirements.

**Perfect-score rate by category**

| Category | Runs | Perfect | Rate |
|---|---:|---:|---:|
| multi-node-os-comparison | 78 | 78 | 100% |
| single-node-os-comparison | 235 | 231 | 98% |
| vyos-networking | 79 | 77 | 97% |
| opnsense-networking | 78 | 74 | 95% |
| sonic-networking | 80 | 73 | 91% |
| clustered-services | 104 | 94 | 90% |
| vyos-opnsense (cross-vendor) | 79 | 71 | 90% |
| openwrt-networking | 71 | 61 | 86% |

### 02. LLM-friendliness varies by release

Fail rate is the ratio of failed commands to all commands run on that release. Note that the fail rate here refers to command fail rate as opposed to task fail rate. It is not uncommon to see high command fail rate with equally high task success rate.

![Command fail rate by release](https://raw.githubusercontent.com/open-sudo/infraset/main/docs/images/fail-rate-by-release.png)

We observe three times as many commands fail on RHEL 7.9 as on RHEL 9.8, running the same 29 tasks with the same wording. Ubuntu shows the same pattern across its two releases.

We suspect that an important factor of this fail rate is how much material about a release exists publicly, and how long that material has stood before a newer version supersedes it. RHEL 9 superseded RHEL 7, so most of what the model has read about RHEL describes 9 rather than 7. RHEL 10 is newer than RHEL 9, but it has not superseded RHEL 9 in the written record yet, which would explain why it fails more often than the release it replaces.

*These numbers exclude `file-integrity-baseline`, where one run distorted a column; the open question below covers it.*

### 03. The Leftovers: 98.8% of Runs Leave Residue

In this experiment, every run carries an operational-hygiene score. It asks whether the run mutated things the task never called for, left residue behind, or broke something unrelated. When the model leaves absolutely no residue behind, the run scores a perfect 1.000.

**Operational hygiene across 804 runs**

| | |
|---|---:|
| Total number of runs | 804 |
| Runs that achieved a perfect score | 10 (1.2%) |
| Mean hygiene across all runs | 0.829 |

### 04. Configuration is cheap. Coordination is expensive.

As we suspected, cost climbs wherever two or more nodes have to agree on replication, quorum, state transfer or failover, because the result has to be demonstrated through a real state transition instead of read out of a config file. The table shows the mean completion time in 3 different scenarios.

**Mean completion by task shape**

| Shape | Typical run |
|---|---:|
| Single-host administration | 🟢 3–4 min |
| Routed / firewalled networks | 🟠 6–13 min |
| Stateful clusters (replication, quorum) | 🔴 **10–25 min** |

A PostgreSQL failover on Ubuntu 24.04 ran for 36 minutes and hit the wall. Same model, same fleet, same day as three-minute single-host tasks that scored clean.

### 05. The model reaches for force as a first resort

An engineer who is stuck usually knows it. They slow down as the system gets harder to read, they get careful around the parts they do not understand, and past a certain point they stop and ask someone. The model has none of those habits. It resorts to forceful options, and it does so even on runs that are otherwise going fine.

865 commands in the dataset stop a service, kill a process, delete a directory or flush a network configuration. 254 of the 804 runs contain at least one of them, so roughly one run in three used force somewhere.

**Forceful commands by kind**

| Kind | Commands | Runs |
|---|---:|---:|
| Flush network state (`iptables -F`, `ip addr flush`) | 327 | 100 |
| `rm -rf` | 241 | 75 |
| Stop or kill a service | 201 | 117 |
| `kill -9` / SIGKILL | 91 | 37 |
| Truncate or zero a file | 5 | 4 |

177 of those commands remove a live database or cluster state directory, such as `/var/lib/pgsql/14/data`, `/var/lib/etcd` or `/var/lib/postgresql/16/main`. They are spread across 55 runs.

### 06. LLMs hallucinate download URLs

Installing packages sometimes requires the agent to download binaries. Such is the case for instance when the package is 
located outside of the distro repos. We have observed that the LLM proceeds to stich together a URL with hallucinated hostnames.

I pulled every hostname the model tried to reach out of the command logs and looked each one up in DNS. There were 71 of them. Four do not resolve at all, so the model made them up. In every one of those cases it was setting up a third-party package repository.

**Invented hostnames and the real ones**

| Hostname the model used | Commands | Real hostname for that content |
|---|---:|---|
| **el9.rabbitmq.com** | 14 | ppa1.novemberain.com |
| **ppa1.rabbitmq.com** | 12 | ppa1.novemberain.com |
| **dl.almalinux.org** | 2 | repo.almalinux.org |
| **yum-eu-west.packagecloud.io** | 1 | packagecloud.io |

> **A supply-chain problem**
>
> The model reaches these hostnames with a `curl` that fetches an unauthenticated file and writes it straight into `/etc/yum.repos.d/`. Nothing answered at the four above, so the fetch failed quietly. If something *had* answered, the package manager would treat whatever came back as a trusted source, gpgcheck and all, and the next `dnf install` would pull binaries from it. One silent curl converts a guessed hostname into a package source with root reach.

### 07. One kernel config change in eight is transient

In one run out of eight the model leaves a change that dies at the next reboot. It reports success, the port answers when you test it, and the failure re-appears weeks later during an unrelated reboot with nothing connecting the two.

**firewall-cmd runs that never used --permanent**

| Image | Runs | Left transient | Rate |
|---|---:|---:|---:|
| RHEL 10.0 | 39 | **5** | **13%** |
| CentOS Stream 10 | 53 | **7** | **13%** |
| AlmaLinux 9 | 57 | **7** | **12%** |
| RHEL 9.8 | 44 | **5** | **11%** |
| RHEL 7.9 | 44 | **3** | **7%** |

It is important to note that our prompt asks the model to reboot the machine and prove the services came back. It is possible that including this guides the model towards persistence, and that a request with no mention of a reboot would do worse.

We suspect models are trained in sandboxes that are inherently transient. As a result, making changes persistent is not a first-class behavior.

## Open Questions

### 01. Ubuntu puts the LLM to sleep

Every task in `clustered-services` installs and configures software, so a polling loop has plenty of chances to kick in. The Red Hat images finish in about five minutes. The Ubuntu ones take three to four times longer, and a third of that time is spent asleep.

![Time spent working versus asleep, clustered-services](https://raw.githubusercontent.com/open-sudo/infraset/main/docs/images/clustered-sleep.png)

The extreme case was `file-integrity-baseline`, which ran 32 minutes on Ubuntu 24.04 against 9 minutes on Ubuntu 16.04, with 24 of those minutes spent in 19 separate sleep commands.

Sleeping explains about half the gap. Take it away and Ubuntu is still twice as slow, and we have not worked out why. It may yet turn out to be something in our own platform rather than the model, which is why this sits here rather than among the findings. It was a surprise either way, because Ubuntu and Debian are the distributions the big AI labs run in their own sandboxes.

### 02. An LLM analyzed the work of an LLM

Every run here was scored by an LLM verifier, and the findings on this page come from an LLM reading the command logs. That is not a rigorous method, and it is fair to hold the conclusions loosely because of it.

Some of it does not depend on that judgment. This is precisely why we are publishing the dataset: to invite the community to mine it.

### 03. One model, one setting

Every run here was executed by Claude Sonnet 5 at medium reasoning effort. Nothing in the dataset says whether a different model, or the same model at a different effort, behaves the same way.

We believe most of these observations apply to current models generally. That is a belief, and it needs validating.

## The lab

![Five machines on a basement shelf: four mini PCs with add-on cooling fans and an HPE switch above, an HPE ProLiant tower and a UPS on the floor below.](https://raw.githubusercontent.com/open-sudo/infraset/main/docs/images/lab.jpg)

*The Antrieb testbed cluster running in my basement. USB fans keep the mini PCs from melting while spinning up disposable VM chains.*

All of it ran in a basement on five machines. The ProLiant is `server1`, which hosts the MCP server; the four mini PCs carry the virtual machines. An HPE OfficeConnect 1620 switch ties them together, and a UPS keeps the fleet up through the short outages that would otherwise kill a campaign halfway through.

**The fleet**

| Host | Machine | CPU | Threads | RAM | Storage |
|---|---|---|---:|---:|---:|
| server1 | HPE ProLiant ML10 Gen9 | Xeon E3-1225 v5 | 4 | 62 GB | 1 TB HDD |
| server2 | GMKtec NucBox K10 | Core i9-13900HK | 20 | 62 GB | 2 × 1 TB NVMe |
| server3 | GMKtec NucBox EVO-T1 | Core Ultra 9 285H | 16 | 62 GB | 1 TB NVMe |
| server4 | Mini PC | Core i9-13900HK | 20 | 62 GB | 2 TB NVMe |
| server5 | Mini PC | Core i9-13900HK | 20 | 62 GB | 2 TB NVMe |
| Total |  |  | 80 | 310 GB | 8 TB |

## What I take from this

Using the traditional definition of completing a system administration task, the LLM succeeds 99% of the time. We tested on eight releases across five distributions, spanning ten years, on jobs ranging from a one-line sysctl change to a three-node quorum. This level of success was surprising.

More surprises were waiting past that definition, starting with how much gets left behind. Almost every run leaves something on the box, and in many tasks that something was a private key left in `/tmp`, once the signing key of the cluster's own certificate authority. About a third of runs reach for force somewhere, and nine times out of ten it happens on a run that goes on to score perfectly. Four hostnames in the whole dataset were invented, and all four were package repositories going into the package manager's configuration.

I suspect even more surprises are lurking in the data. Please join the mining, and reach out if you have any questions. Everything is on [GitHub](https://github.com/open-sudo/infraset) and [Hugging Face](https://huggingface.co/datasets/infraset/infraset): every task, every command timeline, every score.
