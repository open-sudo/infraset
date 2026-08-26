# InfraSet, Testing LLMs as enterprise system administrators

I created InfraSet because I could not find answers to questions that kept arising as I worked with LLMs on IT infrastructure:

- How do LLMs behave on end-of-life Linux distributions (e.g. Ubuntu 16)?
- How do they perform on full-system VMs rather than container-only or MicroVMs?
- How do they handle or setup clustered environments?
- How do they operate in brownfield enterprise environments?
- How do they handle networks, routers, firewalls, and switches?

I figure, these questions matter to anyone considering AI agents for real infra. InfraSet starts with 40 tasks, and we hope the community will help expand it.

## What makes InfraSet different

Enterprise IT infrastructure is diverse. It includes different operating systems, software versions, existing configurations, multi-node clusters, and complex networks. InfraSet uses a capable LLM as an instrument for exploring this diversity. Each task places the LLM in a realistic infrastructure environment and asks it to set it up, investigate a problem, make changes, and verify the result. The goal is to understand:

- What infra work the LLM can complete
- Where and how it fails
- How it handles unfamiliar or legacy infrastructure state
- How it responds to failed commands and incorrect assumptions
- Whether its proposed solution actually works when executed

Each task is evaluated against the resulting infrastructure state, not merely the LLM’s final answer.

## Task environments

Tasks run on disposable VMs, clusters, and networks provisioned through [Antrieb](https://antrieb.sh/).
The environments can include:

- Variety of current and end-of-life Linux distributions
- Single-node and multi-node systems
- Brownfield configurations and existing state
- Routers, firewalls, and switches
- Multi-network topologies
- Real services and application dependencies

No access to your own infrastructure or credentials is required.

## Execution logs

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
./packages/infraset/run-task.sh <generated-task-name>
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
