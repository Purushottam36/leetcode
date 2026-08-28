# 🧠 Algorithmic Engineering & Daily Problem Solving

> **A continuously evolving archive of my daily LeetCode practice — automatically synchronized to GitHub as I solve and submit problems.**

[![LeetCode](https://img.shields.io/badge/LeetCode-Purushottam36-FFA116?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/u/Purushottam36/)
[![GitHub](https://img.shields.io/badge/GitHub-Purushottam36-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/Purushottam36)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-SE-ED8B00?style=for-the-badge\&logo=openjdk\&logoColor=white)](https://www.java.com/)

---

## 📑 Table of Contents

* [🎯 About This Repository](#-about-this-repository)
* [🔄 From LeetCode to GitHub](#-from-leetcode-to-github)
* [🛠️ Technologies & Tools](#️-technologies--tools)
* [🧩 Problem-Solving Domains](#-problem-solving-domains)
* [📂 Repository Structure](#-repository-structure)
* [🧠 Engineering Principles](#-engineering-principles)
* [📈 Continuous Progress](#-continuous-progress)
* [🔗 Live Profiles](#-live-profiles)
* [🚀 Long-Term Goal](#-long-term-goal)
* [🤝 Contributing](#-contributing)
* [📜 License](#-license)
* [👨‍💻 Author](#-author)

---

## 🎯 About This Repository

This repository is a **living record of my algorithmic problem-solving journey on LeetCode**.

I practice consistently, solve problems across different algorithmic domains, and use automation to keep my accepted solutions synchronized with GitHub.

Rather than treating this repository as a manually maintained collection of solutions, I use it as a **growing engineering archive** where each solved problem becomes part of my long-term record of learning, experimentation, and improvement.

### What this repository represents

* 🧠 Continuous algorithmic practice
* 💻 Python and Java implementations
* 📚 Data structures and algorithms
* ⏱️ Time and space complexity analysis
* 🔍 Problem-solving and optimization techniques
* 🔄 Automated synchronization with GitHub
* 📈 Long-term technical growth

> **LeetCode is where I solve. GitHub is where the journey is preserved.**

---

## 🔄 From LeetCode to GitHub

The repository follows an automated workflow that connects daily problem-solving with version control.

```mermaid
flowchart LR
    A["🧑‍💻 Daily Practice"] --> B["🟠 LeetCode"]
    B --> C{"Accepted?"}
    C -->|Yes| D["⚙️ Automation"]
    C -->|No| A
    D --> E["🔄 LeetSync"]
    D --> F["🚀 LeetPush"]
    E --> G["🐙 GitHub Repository"]
    F --> G
    G --> H["📚 Growing Solution Archive"]
```

### 🔁 The workflow

**1. Solve**

I work on a problem directly on LeetCode.

**2. Submit**

The solution is tested against LeetCode's test cases.

**3. Accept**

Once the solution receives an **Accepted** verdict, it becomes part of the repository's evolving archive.

**4. Synchronize**

Automation tools help transfer the solution and its associated information into the GitHub repository.

**5. Preserve**

GitHub provides a persistent, version-controlled record of my daily algorithmic practice.

---

## 🛠️ Technologies & Tools

| Technology / Tool | Role                                           |
| ----------------- | ---------------------------------------------- |
| 🟠 **LeetCode**   | Problem-solving and solution validation        |
| 🐍 **Python 3**   | Algorithm implementations                      |
| ☕ **Java**        | Object-oriented algorithm implementations      |
| 🔄 **LeetSync**   | Synchronizing LeetCode solutions with GitHub   |
| 🚀 **LeetPush**   | Automating solution delivery to the repository |
| 🐙 **GitHub**     | Version-controlled solution archive            |
| 📝 **Markdown**   | Problem and repository documentation           |

---

## 🧩 Problem-Solving Domains

My practice covers a broad range of algorithmic concepts.

| Domain                        | Techniques & Concepts                                |
| ----------------------------- | ---------------------------------------------------- |
| 🔢 **Arrays & Strings**       | Traversal, Prefix/Suffix Techniques, Sliding Window  |
| 🎯 **Two-Pointer Techniques** | Convergence, Partitioning, In-place Processing       |
| 🗺️ **Hash-Based Structures** | Hash Maps, Hash Sets, Frequency Counting             |
| 📚 **Stacks & Queues**        | Monotonic Stacks, Sequence Processing                |
| 🔗 **Linked Lists**           | Traversal, Reversal, Pointer Manipulation            |
| 🌳 **Trees**                  | DFS, BFS, Recursion, Tree Traversal                  |
| 🕸️ **Graphs**                | DFS, BFS, Connectivity, Traversal                    |
| 🔤 **Tries**                  | Prefix Searching and String Structures               |
| 🔗 **Disjoint Sets**          | Union-Find and Connectivity                          |
| 🧮 **Dynamic Programming**    | Memoization, Tabulation, State Optimization          |
| 🧠 **Greedy Algorithms**      | Local Optimization and Decision Strategies           |
| 🔢 **Mathematics**            | Number Theory, Combinatorics, Mathematical Reasoning |
| ⚙️ **Bit Manipulation**       | Bitwise Operations, Masks and Binary Logic           |

> The repository evolves continuously, so the domains represented here may expand as new problems are solved.

---

## 📂 Repository Structure

The repository follows the structure generated and maintained through the synchronization workflow.

```text
leetcode/
│
├── 📁 [Problem_ID]_[Problem_Title]/
│   ├── solution.py
│   ├── Solution.java
│   └── README.md
│
└── 📄 README.md
```

### Problem Directory

Each problem can contain:

| File            | Purpose                                         |
| --------------- | ----------------------------------------------- |
| `solution.py`   | Python implementation                           |
| `Solution.java` | Java implementation                             |
| `README.md`     | Problem information and generated documentation |

The exact files available may vary from problem to problem depending on the languages and synchronization process used for that submission.

---

## 🧠 Engineering Principles

Although these are algorithmic practice problems, I approach them with software-engineering principles in mind.

### 1. ⏱️ Time Complexity

I try to identify efficient approaches rather than relying on brute-force solutions when better alternatives exist.

Typical targets include:

```text
O(1)
O(log N)
O(N)
O(N log N)
```

The appropriate complexity depends on the problem and its constraints.

---

### 2. 💾 Space Complexity

Solutions are also evaluated with respect to auxiliary memory.

When possible, I look for opportunities to reduce unnecessary allocations while maintaining clarity and correctness.

---

### 3. 📖 Readability

The objective is not simply to make a solution pass.

I aim for:

* Meaningful variable names
* Clear control flow
* Understandable function structure
* Appropriate use of data structures
* Minimal unnecessary complexity

---

### 4. 🔍 Problem Decomposition

For challenging problems, I break the problem into smaller components:

```text
Understand
   ↓
Identify Constraints
   ↓
Find Pattern
   ↓
Choose Data Structure
   ↓
Design Algorithm
   ↓
Analyze Complexity
   ↓
Implement
   ↓
Test
   ↓
Optimize
```

---

### 5. 🔄 Continuous Improvement

An accepted solution is not necessarily the end of the learning process.

I use problem solving to improve my ability to:

* Recognize algorithmic patterns
* Compare alternative approaches
* Optimize complexity
* Understand trade-offs
* Write cleaner implementations

---

## 📈 Continuous Progress

This repository is **actively maintained through ongoing LeetCode practice**.

Because the synchronization process updates the repository as new solutions are submitted and accepted, the repository should be viewed as a **continuously growing timeline of algorithmic practice**.

For current statistics such as:

* Problems solved
* Contest rating
* Global ranking
* Badges
* Daily streak
* Acceptance statistics

please refer to my live LeetCode profile.

### 🟠 Live LeetCode Profile

**[Visit my LeetCode Profile →](https://leetcode.com/u/Purushottam36/)**

This approach keeps the repository README from becoming outdated while allowing my actual LeetCode profile to provide the latest metrics.

---

## 🔗 Live Profiles

### 🟠 LeetCode

**[Purushottam36](https://leetcode.com/u/Purushottam36/)**

My primary platform for solving, submitting, and validating algorithmic problems.

### 🐙 GitHub

**[Purushottam36](https://github.com/Purushottam36)**

My development profile and home for this synchronized solution archive.

### 💼 LinkedIn

**[Kumar Purushottam](https://www.linkedin.com/in/kumar-purushottam6136)**

Connect with me professionally and follow my broader development journey.

---

## 🚀 Long-Term Goal

The goal of this repository extends beyond simply increasing the number of solved problems.

I want this archive to represent the gradual development of stronger skills in:

```text
Problem Solving
       ↓
Data Structures
       ↓
Algorithms
       ↓
Complexity Analysis
       ↓
Optimization
       ↓
Software Engineering
       ↓
Systematic Technical Thinking
```

Every problem is an opportunity to learn a new pattern, understand a trade-off, or improve an existing way of thinking.

### 🎯 The objective

> **Solve consistently. Understand deeply. Optimize thoughtfully. Build continuously.**

---

## 🤝 Contributing

This repository primarily documents my personal problem-solving journey, so the solutions themselves are not intended to be collaboratively modified.

However, if you notice:

* An incorrect explanation
* A bug in an implementation
* A better algorithmic approach
* An interesting optimization
* A useful alternative solution

feel free to open an **Issue** or start a **Discussion**.

Constructive technical feedback is always welcome.

---

## 📜 License

This repository is primarily intended for **educational and reference purposes**.

LeetCode problem statements, descriptions, examples, and associated content belong to **LeetCode** and their respective rights holders.

The original solution implementations in this repository are provided as part of my personal learning and problem-solving archive.

If you reuse any solution, I encourage you to first understand the underlying algorithm rather than simply copying the implementation.

---

## 👨‍💻 Author

### Purushottam Kumar

Developer • Problem Solver • Continuous Learner

🔗 **GitHub:** [Purushottam36](https://github.com/Purushottam36)

🧠 **LeetCode:** [Purushottam36](https://leetcode.com/u/Purushottam36/)

💼 **LinkedIn:** [Kumar Purushottam](https://www.linkedin.com/in/kumar-purushottam6136)

---

<div align="center">

### 🧠 Keep Solving. Keep Learning. Keep Building.

**This repository grows one accepted solution at a time.**

⭐ If you find the repository useful, consider giving it a star.

</div>
