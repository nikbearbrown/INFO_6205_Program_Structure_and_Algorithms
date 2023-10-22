In the process of completing this assignment, I learnt several key concepts related to 
         which I would like to mention here. Through various tasks and questions, I gained 
a deeper understanding of the following topics:

**Prim’s Algorithm:**
 
+ Prim’s Algorithm is a famous greedy algorithm.
+ It is used for finding the Minimum Spanning Tree (MST) of a given graph.
+ To apply Prim’s algorithm, the given graph must be weighted, connected and undirected.

**Prim’s Algorithm Implementation:**
 
The implementation of Prim’s Algorithm is explained in the following steps-

Step-01:

+ Randomly choose any vertex.
+ The vertex connecting to the edge having least weight is usually selected.
 
Step-02:
 
+ Find all the edges that connect the tree to new vertices.
+ Find the least weight edge among those edges and include it in the existing tree.
If including that edge creates a cycle, then reject that edge and look for the next least weight edge.
 
Step-03:
 
+ Keep repeating step-02 until all the vertices are included and Minimum Spanning Tree (MST) is obtained.
 
**Prim’s Algorithm Time Complexity:**
 
Worst case time complexity of Prim’s Algorithm is-

+ O(ElogV) using binary heap
+ O(E + VlogV) using Fibonacci heap

**Kruskal’s Algorithm:**

+ Kruskal’s Algorithm is a famous greedy algorithm.
+ It is used for finding the Minimum Spanning Tree (MST) of a given graph.
+ To apply Kruskal’s algorithm, the given graph must be weighted, connected and undirected.
 
**Kruskal’s Algorithm Implementation:**
 
The implementation of Kruskal’s Algorithm is explained in the following steps-

Step-01:
 
+ Sort all the edges from low weight to high weight.
 
Step-02:
 
+ Take the edge with the lowest weight and use it to connect the vertices of graph.
+ If adding an edge creates a cycle, then reject that edge and go for the next least weight edge.
 
Step-03:
 
+ Keep adding edges until all the vertices are connected and a Minimum Spanning Tree (MST) is obtained.

**Kruskal’s Algorithm Time Complexity:**

Worst case time complexity of Kruskal’s Algorithm is O(ElogV) or O(ElogE)

**Difference between Prim’s Algorithm and Kruskal’s Algorithm:**
 
|                       | Prim’s Algorithm                                      | Kruskal’s Algorithm                                |
|-----------------------|-------------------------------------------------------|-----------------------------------------------------|
| Property              | The tree remains connected during construction.       | The tree usually remains disconnected during construction. |
| Growth                | Grows a solution from a random vertex by adding the next cheapest vertex. | Grows a solution from the cheapest edge by adding the next cheapest edge. |
| Efficiency            | Faster for dense graphs.                             | Faster for sparse graphs.                           |

**Masters Theorm**

The Master Theorem applies to recurrences of the following form:

                  T (n) = aT(n/b) + f(n)
where a ≥ 1 and b > 1 are constants and f(n) is an asymptotically positive function.
There are 3 cases:
1. If f(n) = O(n<sup>log<sub>b</sub><sup>a−&epsilon;</sup></sup>) for some constant &epsilon; > 0, then T (n) = Θ(n<sup>log<sub>b</sub><sup>a</sup></sup>).
2. If f(n) = Θ(n<sup>log<sub>b</sub><sup>a</sup></sup>log<sup>k</sup>n) with k ≥ 0, then T (n) = Θ(n<sup>log<sub>b</sub><sup>a</sup></sup>log<sup>k+1</sup>n).
3. If f(n) = Ω(n<sup>log<sub>b</sub><sup>a+&epsilon;</sup></sup>) with &epsilon; > 0, and f(n) satisfies the regularity condition, then T (n) = Θ(f(n)).
Regularity condition: af(n/b) ≤ cf(n) for some constant c < 1 and all sufficiently large n.

**Prim’s Algorithm Implementation**
 
The implementation of Prim’s Algorithm is explained in the following steps-

 Step-01:
 
+ Randomly choose any vertex.
+ The vertex connecting to the edge having least weight is usually selected.
 
Step-02:
 
+ Find all the edges that connect the tree to new vertices.
+ Find the least weight edge among those edges and include it in the existing tree.
+ If including that edge creates a cycle, then reject that edge and look for the next least weight edge.

Step-03:
 
+ Keep repeating step-02 until all the vertices are included and Minimum Spanning Tree (MST) is obtained.