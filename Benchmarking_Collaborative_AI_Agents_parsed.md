
Beyond Tool Use: Benchmarking Agents for Real-World Collaboration

# The evolution from t-bench to t2-bench in the quest for realistic agent evaluation.

| Al Agent       | User       |
| -------------- | ---------- |
| Tools/Database | NotebookLM |






# Today's Agent Benchmarks Are Missing What Matters: Users and Rules

Most benchmarks feature simplified instruction-following setups, ignoring three critical desiderata for deploying agents in the wild:

1. Human Interaction: Agents must incrementally gather information and resolve intents through dynamic, multi-turn conversations.
2. Rule Adherence: Agents must accurately adhere to complex policies and rules specific to a task or domain.
3. Consistency: Agents must maintain reliability at scale across millions of stochastic interactions.

| Typical Benchmark | Real World   |
| ----------------- | ------------ |
| O                 | Tool         |
| Agent             | I            |
| O                 | Database     |
| O                 | Conversation |
| Agent             | 7            |
| Tool              | User         |
| Policy            | Database     |
| Document          | NotebookLM   |





# T-bench Simulates Real-World Dynamics: Users, Tools, and Policies

# Domain Policy

| Consults          | Rules                   |       |           |                |          |
| ----------------- | ----------------------- | ----- | --------- | -------------- | -------- |
| LM-Simulated User | Multi-turn Conversation | Agent | API Tools | Reads & Writes | Database |

# LM-Simulated User

An LLM simulates a human user, creating stochastic, multi-turn conversations to test the agent's interactive capabilities.

# Stateful Evaluation

Success is measured by comparing the final database state to the ground truth, allowing varied conversational paths to the same correct outcome.

NotebookLM



# The First Revelation: State-of-the-Art Models Are Strikingly Inconsistent

On τ-bench, even top models like GPT-4o achieve low task success rates (~61% on τ-retail and ~35% on τ-airline).

# Reliability Plummets Over Multiple Trials (passk on τ-retail)

|               | 100     | 80                 | 60 | 40 | 20 |
| ------------- | ------- | ------------------ | -- | -- | -- |
| GPT-4o        |         |                    |    |    |    |
| GPT-4-turbo   | (pass8) | drops to below 25% |    |    |    |
| Claude-3-opus |         |                    |    |    |    |
| GPT-3.5-turbo |         |                    |    |    |    |

passk is the chance that all k i.i.d. trials of a task are successful. It measures the agent's robustness to conversational variations.

Takeaway: High average success (pass²) is not enough for real-world deployment; agents must be consistent.

k = # of trials

NotebookLM



# But t-bench Has a Limitation: What If the User Needs to Act?

|          | Single-Control: t-bench                                                                         | Dual-Control: Real World |                                                                                                      |
| -------- | ----------------------------------------------------------------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| Dialogue | Dialogue                                                                                        |                          |                                                                                                      |
| Agent    | User                                                                                            | Agent                    | User                                                                                                 |
| World/DB | The agent is the sole actor. The user is a passive information source (e.g., booking a flight). | World/DB                 | Both agent and user must act to solve the problem, requiring coordination (e.g., technical support). |

How can we evaluate an agent's ability to not just act but to guide a user to act correctly?

NotebookLM



# T2-bench introduces a Dual-Control Environment for Collaborative Tasks

| Core Innovation                                                                                                                                                             | Communication Channel |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Modeled as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP), where both agent and user have distinct tools to act on a shared, dynamic environment. | BOT                   |

| Agent Tools           | User Tools             |
| --------------------- | ---------------------- |
| get\_customer\_by\_id | toggle\_airplane\_mode |
| enable\_roaming       | get\_status\_bar       |

# Customer

# Mocked Device

# New Domain: Telecom Troubleshooting

The Scenario: An agent helps a user diagnose and fix a phone issue (e.g., no mobile data).

Agent Tools: Access and modify customer CRM data (e.g., 'get_customer_by_id', 'enable_roaming').

User Tools: Interact with a mocked phone device (e.g., 'toggle_airplane_mode', 'get_status_bar').

The Challenge: The agent must successfully diagnose the issue and guide the user to perform the correct sequence of actions on their end.

NotebookLM



# The Second Revelation: Guiding a User Is Harder Than Acting Alone

| Performance | Dual-Control Mode ('pass^1'on Telecom) | No-User Mode (Reasoning Only) | Default Mode (Reasoning + Communication) |      |      |
| ----------- | -------------------------------------- | ----------------------------- | ---------------------------------------- | ---- | ---- |
| 1.0         | 0.8                                    | 0.6                           | 0.52                                     | 0.67 | 0.42 |
|             | \*\*18-25% Performance Drop\*\*        |                               |                                          |      |      |

This gap isolates the failure rate caused by the communication and coordination bottleneck. It's not just about knowing what to do, but successfully guiding a user to do it.

0.2

0.4

0.34

GPT-4.1

o4-mini

NotebookLM



# Diagnosis: Task Complexity and User Persona

# Amplify the Challenge

More Sub-Tasks = Lower Success

User Persona Matters

| 20 | 20 | 52% | 38%                 |
| -- | -- | --- | ------------------- |
| 2  | 5  | 9   | Number of Sub-Tasks |

Easy Persona

Hard Persona

τ2-bench's compositional tasks and user personas enable fine-grained diagnosis, moving beyond a single success score to understand why agents fail.

NotebookLM



# The Quest for Realism: An Evolutionary View

| Traditional              | Increasing Realism |                       |                            |       |       |       |      |
| ------------------------ | ------------------ | --------------------- | -------------------------- | ----- | ----- | ----- | ---- |
| Benchmarks               | τ-bench            |                       | τ2-bench                   |       |       |       |      |
|                          |                    | World                 | Agent                      | World | Agent | World | User |
| Instruction Following    |                    | Single-Control        | Dual-Control               |       |       |       |      |
| No user interaction, no  |                    | Exposed the critical  | Isolated the communication |       |       |       |      |
| domain rules, no measure |                    | inconsistency of SOTA | bottleneck as a major      |       |       |       |      |
| of consistency.          |                    | models via 'pass^k    | failure point.             |       |       |       |      |

NotebookLM



# The Forward: Building Agents Path That Truly Collaborate

The journey to t2-bench reveals that the next generation of agents must master collaborative problem-solving. The critical, unsolved challenges are:

1. Consistency: Achieving reliable performance over many trials (passk).
2. Rule-Following: Faithfully adhering to complex, domain-specific policies.
3. User Guidance: Effectively communicating with and coordinating an active user in a shared-control environment.

The t-bench family provides the necessary testbeds to measure what truly matters and build agents ready for the real world.

NotebookLM