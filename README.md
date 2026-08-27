# Testing LLMs on Infrastructure Work

**InfraSet** is a corpus of LLM execution traces from infrastructure work. I created **InfraSet** to share my experience using LLMs for infrastructure work and to help answer questions such as:

- How do LLMs behave on end-of-life Linux distributions, such as Ubuntu 16.04?
- How do they perform on full-system VMs rather than container-only environments or microVMs?
- How do they handle distributed environments?
- How do they operate in brownfield environments?
- How do they handle networks, routers, firewalls, and switches?
- How do they handle migrations between versions or from one Linux distribution to another?

These questions matter to anyone considering LLMs for real infrastructure work.

InfraSet starts with 40 tasks, and we hope the community will help expand it.

## What makes InfraSet different

Three things:

- **It is not a leaderboard.** InfraSet does not focus on comparing LLMs with one another. Instead, it uses the LLM to explore a infrastructure scenarios.
- **A rich testbed.** It includes multiple Linux distributions, full-system VMs, multi-node clusters, and networked infrastructure.
- **Rich execution data.** InfraSet does not publish only scores or final answers. It also publishes execution traces, including what the LLM attempted, what happened, and whether the result worked.

## Testbed

Tasks run on disposable VMs, clusters, and networks provisioned through [Antrieb](https://antrieb.sh/). No access to your infrastructure is required.

The environments can include:

- Current and end-of-life Linux distributions, including RHEL 7 through 10, AlmaLinux 9, Alpine, Arch, Debian 13, Ubuntu 16.04, and Ubuntu 24.04
- Single-node and multi-node systems
- Brownfield configurations and pre-existing state
- Routers, firewalls, and switches, including VyOS, OPNsense, OpenWrt, and SONiC
- Multi-network topologies
- Real services and application dependencies

## Execution Traces

Every published run includes the full observable agent trajectory, including:

- Agent messages
- Tool calls
- Commands
- Command output
- Errors
- Failed attempts
- Recovery attempts
- Final response
- Evaluator result

Each task is evaluated against the resulting infrastructure state—not merely the LLM’s final answer.

Clone the repository, point your preferred analysis tool at the traces, and begin investigating the runs immediately.

## Running a task

InfraSet tasks are executed through the InfraSet-enabled Harbor engine. Clone the Harbor fork containing the InfraSet engine:

```bash
git clone https://github.com/open-sudo/harbor.git
cd harbor
```

Sign in to the [Antrieb dashboard](https://antrieb.sh/dash) using GitHub or Google. Generate an API key and copy it.

Export the API key in your terminal:

```bash
export ANTRIEB_TOKEN=ant_XXXXXX
```

Run a task:

```bash
./tasks/run-task.sh greenfield/haproxy-nodejs-ubuntu16
```

## Creating a task

InfraSet includes a task-builder skill that allows a coding agent to turn a task idea into a complete executable InfraSet task.

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

You do not need to write the environment or verification logic manually, and you do not need to worry about creating the cluster in Antrieb. Copy the generated task name and run it:

```bash
./tasks/run-task.sh <generated-task-name>
```

## Exploring the logs

The task definitions are available in the `tasks/` folder of this repository. Execution logs are available in the `jobs/` folder.

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
- Analysis of existing execution traces
