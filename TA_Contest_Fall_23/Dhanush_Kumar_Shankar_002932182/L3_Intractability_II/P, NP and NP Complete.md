
## Why bother to learn?
Understanding the classes P, NP, and NP-complete is crucial because it helps us categorize problems based on their solvability and efficiency. These classes provide insights into the inherent difficulty of solving problems and have implications for various fields, such as cryptography, optimization, and algorithm design.

  
To illustrate the classification of problems in theoretical computer science, we can adopt a familiar "Easy-to-Hard" scale, akin to how we gauge problem complexity in real life. In this context, problem classifications are categorized into two main sets: **P**, representing problems solvable in "Polynomial" time, and **NP**, denoting problems solvable in "Non-deterministic Polynomial" time. Furthermore, we encounter the **NP-Hard** and **NP-Complete** sets, which encapsulate more intricate problems. This classification can be aligned with levels of difficulty:

- **Easy:** Corresponds to problems in the set **P**.
- **Medium:** Corresponds to problems in the set **NP**.
- **Hard:** Corresponds to problems in the set **NP-Complete**.
- **Hardest:** Corresponds to problems in the set **NP-Hard**.

![[complexity.png]]

Visualizing this relationship, we depict the hierarchical arrangement as: **Easy (P) -> Medium (NP) -> Hard (NP-Complete) -> Hardest (NP-Hard)**.

In this context, we operate under the widely held but as-yet unproven assumption that **P** is not equivalent to **NP**, which is symbolized by **P ≠ NP**. Additionally, our diagram reveals an interesting overlap between **NP** and **NP-Hard**, and when a problem belongs to both of these sets, it's labeled as **NP-Complete**.

However, the question remains: How do we determine the classification of a specific algorithm within each category? For this purpose, we move into a more formal approach in the subsequent section.

## Polynomial Algorithms
In the realm of algorithmic complexity, polynomial algorithms hold a significant place due to their efficiency and practicality. These algorithms are crucial in the **P (Polynomial Time)** class, implying that their execution time remains manageable even as the input size increases.

#### **Theory:**
A polynomial algorithm is characterized by its runtime being bounded by a polynomial function of the input size. Mathematically, if an algorithm runs in **O(n^k)** time, where **n** represents the input size and **k** is a constant exponent, then the algorithm is considered polynomial. The key insight here is that the running time grows at a reasonable rate as the input size grows.

#### **Examples:**
1. **Linear Search:** An example of a polynomial algorithm is the linear search. Given an array of **n** elements, linear search examines each element one by one until the desired item is found or the entire array has been traversed. The time complexity of linear search is **O(n)**, as the number of operations increases linearly with the input size.
2. **Matrix Multiplication (Strassen's Algorithm):** Another instance of a polynomial algorithm is the matrix multiplication algorithm known as Strassen's Algorithm. It reduces the number of multiplication operations required for matrix multiplication, resulting in a time complexity of approximately **O(n^2.81)**. Although this exceeds the traditional **O(n^3)** complexity of matrix multiplication, it still falls within the polynomial realm.
    
#### **Time Complexity:**
The general time complexity of polynomial algorithms can vary based on the specific polynomial function used. However, the crucial characteristic is that the complexity is bounded by a polynomial expression in terms of the input size. This generally implies that the algorithm's performance remains reasonable as the input size grows larger.

#### **Space Complexity:**
Polynomial algorithms' space complexity, both in terms of minimum and maximum bounds, typically follows a pattern similar to their time complexity. Most polynomial algorithms have a space complexity that's bounded by a polynomial function of the input size.

- **Minimum Bound:** Polynomial algorithms might have a minimum space complexity of **O(1)**, indicating that they use a constant amount of memory regardless of input size. This is often the case for algorithms that perform computations in place.
- **Maximum Bound:** The maximum space complexity of polynomial algorithms can vary based on the nature of the problem they solve. It can range from **O(n^k)**, where **k** is a constant exponent, to other polynomial expressions, reflecting the algorithm's memory requirements as the input size grows.


## Non-Deterministic Polynomial Algorithms (NP)
Non-Deterministic Polynomial algorithms, commonly referred to as **NP**, represent a class of problems that can be verified in polynomial time. Unlike polynomial algorithms that can be efficiently solved, NP problems may not have a known polynomial-time solution. Instead, these problems rely on a proposed solution that can be verified for correctness in a reasonable amount of time.

#### **Theory:**
A problem is considered to be in the **NP** class if a proposed solution can be verified in polynomial time. In other words, if a solution can be checked for its validity using an algorithm with a polynomial time complexity, then the problem belongs to **NP**. However, it's important to note that finding a solution itself might not be polynomial, and that's what differentiates **NP** problems from problems in the **P** class.

#### **Examples:**

1. **Traveling Salesman Problem (TSP):** The Traveling Salesman Problem is a classic example of an **NP** problem. Given a list of cities and their pairwise distances, the task is to find the shortest possible route that visits each city exactly once and returns to the starting city. While verifying a proposed solution's correctness is polynomial (you can check if the proposed route satisfies the constraints and has the claimed length), finding the optimal solution is not known to be polynomial.
2. **Subset Sum Problem:** In the Subset Sum Problem, you're given a set of integers and a target sum. The goal is to determine if there's a subset of the given integers that adds up to the target sum. Verifying a proposed subset's sum can be done in polynomial time, as you just need to add up the subset's elements. However, finding such a subset in the first place is not guaranteed to be polynomial.

#### **General Time Complexity:**
For NP problems, the general time complexity involves verifying a proposed solution in polynomial time. The verification process usually includes checking that the proposed solution meets the problem's constraints and requirements. The act of verification itself is what defines the NP class.
#### **Space Complexity:**
The space complexity of NP problems, similar to their time complexity, centers around the verification process. The space required for verifying a solution is typically polynomial in terms of the input size. However, as with time complexity, the focus is on verification rather than finding the solution itself.

## NP-Complete Problems
NP-Complete problems sit at the heart of computational complexity theory, embodying a set of challenges that are among the most intriguing and potentially difficult to solve. These problems share the attributes of both the **NP** and **NP-Hard** classes, presenting an exceptional combination of difficulty and verifiability.

#### **Theory:**
A problem is deemed **NP-Complete** if it belongs to the **NP** class and shares a unique connection with every problem in the **NP-Hard** class. In essence, **NP-Complete** problems are the most difficult problems in **NP**, as their solutions are believed to require non-polynomial time. However, their special property is that if a polynomial-time algorithm is discovered for just one **NP-Complete** problem, it would imply polynomial-time solutions for all problems in **NP**, making them incredibly significant in the field of computational complexity.

#### **Examples:**
1. **The Boolean Satisfiability Problem (SAT):** The Boolean Satisfiability Problem is a classic **NP-Complete** problem. Given a Boolean formula, the task is to determine if there exists an assignment of truth values to the variables that makes the entire formula true. Although verifying a proposed assignment's correctness is polynomial, finding such an assignment is generally considered to require exponential time. 
2. **The Knapsack Problem:** The Knapsack Problem involves selecting items from a set with given weights and values, aiming to maximize the value while staying within a certain weight limit. While verifying a proposed solution's adherence to the constraints can be done in polynomial time, finding the optimal solution efficiently is typically challenging.

#### **General Time Complexity:**
**NP-Complete** problems share their time complexity attributes with the **NP** class. Verifying a proposed solution's correctness remains polynomial, just like in **NP** problems. However, the distinction lies in the difficulty of finding the solutions, as they are suspected to require exponential or worse time.

#### **Space Complexity:**
The space complexity of **NP-Complete** problems aligns with the verification process. The space needed for verifying solutions is typically polynomial. Again, the focus is on the efficiency of verification, not the efficiency of solution discovery.


## P = NP??
![[P_NP.png]]
The question of whether **P** is equal to **NP** is one of the most famous and significant unsolved problems in the field of theoretical computer science. This question essentially asks whether problems for which a solution can be verified in polynomial time (i.e., problems in **NP**) can also be solved in polynomial time (i.e., problems in **P**).

**Real-World Implications:** The resolution of the **P = NP** question would be nothing short of revolutionary, with profound implications spanning across diverse fields. If it were proven that **P = NP**, it would signify a paradigm shift in computational possibilities. Let's explore both scenarios:

**P = NP:** Should this equality hold true, it would signify that any problem for which a proposed solution can be verified in polynomial time can also be efficiently solved in polynomial time. The ramifications are immense:

- **Cryptography:** One of the most significant areas that would be impacted is cryptography. If **P = NP**, it could render many cryptographic protocols vulnerable. Currently, encryption methods rely on the fact that certain mathematical problems are computationally hard to solve. A polynomial-time algorithm for **NP**-Complete problems could break these encryption schemes, leading to a revolution in data security strategies.
    
- **Optimization:** Fields like logistics, supply chain management, and resource allocation would experience a revolution. Many real-world optimization problems, which are currently deemed computationally intractable, could be solved efficiently. This would lead to more streamlined processes, cost savings, and enhanced resource utilization across industries.
    
- **Artificial Intelligence:** The advancement of artificial intelligence (AI) could take a giant leap forward. Solving **NP**-Complete problems efficiently would greatly impact machine learning, pattern recognition, and decision-making algorithms. Complex tasks that currently take considerable time could become nearly instantaneous, opening doors to innovative AI applications.
    

**P ≠ NP:** On the other hand, if it were proven that **P ≠ NP**, it would reinforce the inherent complexity of certain problems and validate the distinction between problems that are easy to verify and those that are difficult to solve. The challenges posed by this scenario are equally noteworthy:

- **Computational Intractability:** The fact that **NP** problems are inherently more difficult to solve than to verify would be underscored. This could have practical consequences in fields where finding optimal solutions is crucial, such as in combinatorial optimization problems encountered in operations research and logistics.
    
- **Algorithmic Development:** Researchers would need to continue their efforts in developing approximation algorithms, heuristics, and techniques to handle **NP**-Complete problems efficiently. Creative problem-solving strategies would be essential to navigate around the intrinsic computational barriers.
  
  
  
  
  
  ## 💡 Are you ready to test your knowledge?

1. The class NP is defined as the set of problems whose solutions can be... <br>
    a) found in polynomial time <br>
    b) verified in polynomial time <br>
    c) found in exponential time <br>
    d) both a and b <br>

<details>
   <summary>Click to reveal answer</summary>
   a) found in polynomial time
</details>

2. P = NP problem asks whether every problem whose solution can be quickly verified by a computer can also be quickly... <br>
    a) solved by a computer <br>
    b) explained by a computer <br>
    c) ignored by a computer <br>
    d) misunderstood by a computer <br>

<details>
   <summary>Click to reveal answer</summary>
   a) solved by a computer
</details>

3. Deciding whether a graph can be colored using 2 colors is a problem that belongs to... <br>
    a) P <br>
    b) NP <br>
    c) NP-Complete <br>
    d) None of the above <br>

<details>
   <summary>Click to reveal answer</summary>
   a) P
</details>

4. The clique problem, determining whether a graph has a complete subgraph of a given size, is an example of a... <br>
    a) Feasible problem <br>
    b) P problem <br>
    c) NP problem <br>
    d) NP-complete problem <br>

<details>
   <summary>Click to reveal answer</summary>
   d) NP-complete problem
</details>

5. Which of the following problem is not NP hard?
    a) Travelling Salesman Problem <br>
    b) Knapsack Problem <br>
    c) Linear Programming Problem <br>
    d) Hamiltonian Cycle Problem <br>

<details>
    <summary>Click to reveal answer</summary>
    c) Linear Programming Problem
</details>

6. NP-Hard is the set of problems that are... <br>
    a) At least as hard as the easiest problems in NP <br>
    b) At least as hard as the hardest problems in NP <br>
    c) No harder than the hardest problems in NP <br>
    d) Easier than the easiest problems in NP <br>

<details>
    <summary>Click to reveal answer</summary>
    b) At least as hard as the hardest problems in NP
</details>

7. If P ≠ NP, then... <br>
    a) no problem in NP is solvable in polynomial time <br>
    b) no problem in NP is verifiable in polynomial time <br>
    c) some problems in NP cannot be solved in polynomial time <br>
    d) all problems in NP can be solved in polynomial time <br>

<details>
    <summary>Click to reveal answer</summary>
    c) some problems in NP cannot be solved in polynomial time
</details>
