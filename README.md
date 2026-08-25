# InfraSet

**InfraSet explores what happens when a capable LLM is asked to perform real infrastruture work across heterogeneous enterprise environments.**

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
git clone https://github.com/<your-account>/harbor.git
cd harbor
```

Sign in to the [Antrieb dashboard](https://antrieb.sh/dash) using GitHub or Google and generate an API key.

Export the API key:

```bash
export ANTRIEB_TOKEN=ant_XXXXXX
```

Run a task:

```bash
./packages/infraset/run-task.sh haproxy-nodejs-ubuntu16
```

## Exploring the logs

The task definitions are available under:

```text
examples/infraset/
```

Execution logs are available under:
```text
jobs/
```

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
