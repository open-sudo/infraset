# Testing LLMs on Infrastructure Work 

**InfraSet** is a corpus of LLM traces doing infrastructure work. I created **InfraSet** to share my experience using LLM on infra work and to help answer questions such as:

- How do LLMs behave on end-of-life Linux distributions (e.g. Ubuntu 16)?
- How do they perform on full-system VMs rather than container-only or MicroVMs?
- How do they handle distribued environments?
- How do they operate in brownfield environments?
- How do they handle networks, routers, firewalls, and switches?
- How do they handle migrations from version to version or from a distro to distro?

I was thinking these questions matter to anyone considering LLM for infrastructure.

## What makes InfraSet different

Three things:
- InfraSet is not a leaderboard where LLMs are compared withe ach other. Instead, we take one LLM and test various Infra scenarios. 
- Richness of the testbed: multiple Linux distros,  multi-node clusters, and support for networking.
- Richness of the data: InfraSet does not just publish scores. We also publish complete execution traces.
  
## Testbed

Tasks run on disposable VMs, clusters, and networks provisioned through [Antrieb](https://antrieb.sh/).
The environments can include:

- Variety of current and end-of-life Linux distributions: RHEL 7 to 10, Alma 9, Alpine, Arch, Debian 13, Ubuntu 24, Ubuntu 16
- Single-node and multi-node systems
- Brownfield configurations and existing state
- Routers, firewalls, and switches:  VyOS, OPNSense, OpenWRT, SONiC
- Multi-network topologies

## Execution Traces

Every published run includes the full observable agent trajectory, including:

- Agent messages
- Tool calls
- Commands
- Command output
- Errors
- Failed attempts
- Recovery attempts
- Final results

Clone the repository, point your preferred analysis tool at the logs, and begin investigating the runs immediately.

## Running a task

InfraSet tasks are executed through the InfraSet-enabled Harbor engine. Clone the Harbor fork containing the InfraSet engine:
```bash
git clone https://github.com/open-sudo/harbor.git
cd harbor
```

Sign in to the [Antrieb dashboard](https://antrieb.sh/dash) using GitHub or Google and generate and copy an API key.

Export the API key in your terminal or add it to your examples/run-task.sh script:

```bash
export ANTRIEB_TOKEN=ant_XXXXXX
```

Run a task:

```bash
./tasks/run-task.sh greenfield/haproxy-nodejs-ubuntu16
```

## Creating a task

InfraSet includes a task-builder skill that allows a coding agent to turn a task idea into a complete executable benchmark task.

1. Copy `./skills/infraset-task-builder` into a skills directory your coding agent can access.
2. Load the skill into your coding agent and describe the task you want to create.

For example:

> Create an OpenLDAP task with 50 service accounts that have been used at various times during the past eight months. Identify service accounts that have not been used for 90 or more days and disable them.

The coding agent uses the skill to generate the complete task, including:

- `instruction.md`
- `task.toml`
- Environment information
- Setup files
- Verification code
- The task name

You do not need to write the environment or verification logic manually, neither do you need to worry about creating the cluster in Antrieb. Copy the generated task name and run it:

```bash
./tasks/run-task.sh <generated-task-name>
```

## Exploring the logs

The task definitions are available in the tasks folder in this exact repo:
Execution logs are available ```jobs```

Use your preferred LLM or analysis tool to explore questions such as:

- What did the LLM try first?
- Which assumptions were incorrect?
- Where did it recover successfully?
- Which failures were caused by the operating system or infrastructure state?
- Did the final change actually solve the problem?
- What would a human SRE need to verify before applying the fix?

## Contributing

InfraSet currently contains 40 tasks. Contributions are welcome, including:

- New operating systems
- New network topologies
- New clustered environments
- Brownfield scenarios
- Troubleshooting tasks
- Evaluation improvements
- Analysis of existing execution logs
