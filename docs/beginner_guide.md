# Beginner's Guide to OARL

Welcome to the **Open Autonomous Research Lab (OARL)**! If you are new to the project or looking for a plain-language explanation of what this application does and how it works, you are in the right place.

This guide is written for non-technical stakeholders, beginners, and new contributors. We'll avoid heavy jargon where possible, and when we have to use technical terms, we'll explain them simply.

---

## 1. Overview

### What is OARL?
OARL is a platform that uses AI to act like an entire team of data scientists and researchers. 

Imagine you have a spreadsheet filled with data (like customer records or housing prices) and you want to know: *"Why are customers leaving our company?"*

Normally, you would have to hire a data engineer to clean the data, a data scientist to find patterns, a machine learning engineer to build a predictive model, and a researcher to write the final report. 

**OARL does all of this automatically.** You give it a dataset and a question, and it coordinates a team of specialized AI "Agents" to figure it out and hand you a finished, professional research report.

### Why does it exist?
The goal is to democratize data science. By automating the tedious parts of data analysis and machine learning, OARL allows anyone to discover insights without needing to write complex Python code or understand algorithms.

---

## 2. Core Concepts

Before we dive into how the system works, let’s define the key puzzle pieces that make up OARL.

- **Agents:** Think of an agent as a digital employee with a specific job title. Just like a real company, OARL has different agents for different tasks. There is a *Data Engineer Agent* that cleans data, an *ML Engineer Agent* that builds predictive models, and a *Research Analyst Agent* that writes the final report.
- **Multi-Agent System:** This simply means a system where multiple Agents work together. Instead of one giant AI trying to do everything (which often fails), OARL uses a multi-agent system so each agent can focus on what it does best.
- **Skills:** A Skill is a specific tool or ability an Agent can use. For example, the Data Engineer Agent has a "clean_missing_values" skill, and the Visualization Agent has a "create_bar_chart" skill. OARL has over 100 of these modular skills.
- **MCP (Model Context Protocol):** MCP is a set of rules that allows AI agents to securely connect to external tools—like your computer's file system, a database, or the internet. In OARL, "MCP Servers" act as bridges that let the AI safely read your datasets or search the web.
- **Spec (Specification):** A "spec" is a blueprint or design document. In this project, `platform_spec.md` is the blueprint that outlines exactly how the platform should be built and behave.
- **Backlog:** A backlog is a to-do list of tasks, bugs, or new features that the developers plan to work on in the future. 

---

## 3. Architecture (How it works end-to-end)

Let’s walk through what happens when you use OARL, step by step:

1. **The Request:** You upload a dataset and type a request, like: *"Analyze this sales data and predict next month's revenue."*
2. **The Boss (Orchestrator Agent):** Your request goes straight to the *Orchestrator Agent*. This is the boss. It looks at your request and says, *"Okay, we need to clean this data, analyze it, and build a prediction model."*
3. **The Project Manager (Planner Agent):** The Orchestrator hands the job to the *Planner Agent*, which writes a step-by-step to-do list for the rest of the team.
4. **The Workers (Specialist Agents):** The Planner hands the tasks to the specialists:
    * The **Data Engineer** cleans up the messy data.
    * The **Data Scientist** looks for trends and creates charts.
    * The **ML Engineer** builds a machine learning model to make the prediction.
    * The **Evaluation Agent** double-checks the ML Engineer's work to make sure the prediction is accurate and fair.
5. **The Writer (Research Analyst):** Once all the data is crunched, the *Research Analyst Agent* looks at all the numbers and writes a nicely formatted, human-readable report.
6. **The Librarian (Knowledge Manager):** Finally, the *Knowledge Manager Agent* saves the report and any important discoveries into the system's "memory" so it can learn for next time.
7. **The Result:** You receive the finished Research Report. 

Throughout this entire process, all of these agents are talking to each other behind the scenes!

---

## 4. Key Workflows

### How the Components Interact
- **The UI (Streamlit):** This is the screen you click on. It’s built using a tool called Streamlit, which makes it easy to create web apps for data science. 
- **The API (FastAPI):** When you click a button in the UI, it sends a message to the API (the backend waiter). The API then taps the Orchestrator Agent on the shoulder to start working.
- **The Reasoning Loop:** Every agent in OARL follows a strict thinking process: 
  1. **Plan:** Figure out what to do.
  2. **Execute:** Do the work using their Skills.
  3. **Evaluate:** Grade their own work.
  4. **Improve:** If the grade is bad, try again.

### Development Workflow
If a developer wants to add a new ability (Skill) or a new employee (Agent) to OARL, they follow a trunk-based workflow:
1. They create a "feature branch" (a safe workspace).
2. They write the code for the new Skill.
3. They use tools to check the code for syntax rules (`ruff check`) and make sure the code works (`pytest`).
4. Once perfect, they merge it into the `main` code branch. 

---

## 5. Glossary

Here is a quick dictionary of terms you might see in the project files:

| Term | Definition |
|------|------------|
| **Bug** | An error or flaw in the code that causes the app to behave unexpectedly. |
| **CI/CD** | Continuous Integration / Continuous Deployment. Automated robots that test the code every time a developer saves it. |
| **Dataset** | A collection of data, usually in the form of a spreadsheet (like a CSV or Excel file). |
| **Linting (Ruff)** | A spell-checker for code. It highlights formatting mistakes so all the code looks consistent. |
| **Testing (Pytest)** | Automated scripts that check if the code does what it is supposed to do. |
| **Open Source** | Software where the original source code is made freely available and may be redistributed and modified. |
| **Type Checking (Mypy)** | A tool that ensures developers are passing the right *type* of data around (e.g., passing a number when a number is expected, not a word). |
| **UI / API** | User Interface (what you see) / Application Programming Interface (how computers talk to the backend). |

---

## 6. FAQ for Beginners

**Q: Do I need to be a programmer to use OARL?**  
**A:** No! The goal of the Streamlit UI is to let anyone upload a dataset and ask questions in plain English. 

**Q: What is the difference between an Agent and a Skill?**  
**A:** An Agent is the "who" and the Skill is the "how". An Agent is the AI brain making decisions, while a Skill is the physical tool it uses (like a calculator or a graph-maker) to get the job done.

**Q: Where does the memory go?**  
**A:** OARL saves insights into a "Knowledge Base" (a simple text file system) and saves complex search data into a "Vector Store" (a special database that helps the AI remember context). 

**Q: What if the AI gets something wrong?**  
**A:** That is why we have the **Evaluation Agent**. Its entire job is to grade the other agents. If the ML Engineer builds a bad predictive model, the Evaluation Agent will catch it, score it poorly, and force the ML Engineer to try again (the "Improve" step).
