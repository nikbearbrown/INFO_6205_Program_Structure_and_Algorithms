In the process of completing this assignment, I learnt several key concepts related to 
algorithm analysis and computational complexity which I would like to mention here. Through various tasks and questions, I gained a deeper understanding of the following topics:

**Order of Growth:**

The "Order of Growth" of a function refers to how the resource requirements (such as time 
or space) of a function increase as the size of the input to that function increases.

Commonly used notations for describing the order of growth include:

1. Big O Notation (O): This notation provides an upper bound on the growth rate of a 
function. It describes the worst-case scenario for an algorithm's resource usage.

2. Theta Notation (Θ): This notation provides a tight bound on the growth rate of a 
function. It describes precise estimate of an algorithm's behavior.

3. Omega Notation (Ω): This notation provides a lower bound on the growth rate of a 
function. It describes the best-case scenario for an algorithm's resource usage.

Here is the order of growth in increasing order:

| Order of Growth | Description        |
|-----------------|--------------------|
| 1               | Constant           |
| log(n)          | Logarithmic        |
| √(n)            | Square Root        |
| N               | Linear             |
| N log(n)        | Linear Logarithmic |
| N^2             | Square             |
| N^3             | Cube               |
| N^k             | Polynomial         |
| 2^n             | Exponential        |
| N!              | Factorial          |

**Dynamic Programming:**

Dynamic programming is a powerful technique used to solve problems by breaking them down 
into smaller overlapping subproblems and storing the solutions to these subproblems in a 
table (usually an array or matrix) to avoid redundant calculations. It's particularly 
useful for optimization problems where you want to find the best solution among a set of 
possibilities.

**Gale-Shapley Algorithm:**

The Gale-Shapley algorithm, also known as the Stable Marriage Problem algorithm, is a 
mechanism for finding a stable matching between two sets of agents, such as men and women, 
students and schools, or any other two groups with preferences over each other.

The main goal of the algorithm is to find a stable matching, where no two agents from different groups would both prefer each other over their current partners.

The result of the Gale-Shapley algorithm is a stable matching in which every agent is paired with a partner, and there are no blocking pairs. A blocking pair is a situation where two agents (one from each group) would both prefer each other over their current partners, which would make them leave their current partners to form a new couple.

The properties of Gale-Shapley Algorithm is given below:

1. The Gale-Shapley algorithm always produces a stable matching, meaning there are no blocking pairs.
2. The solution may not be unique, as different orderings of proposals can lead to different stable matchings.
3. In practice, the proposing group has an advantage in terms of getting their most preferred partners.

The Gale-Shapley algorithm is used in various real-world scenarios, including college admissions, job markets, and online dating platforms, where individuals have preferences over potential partners or schools.
