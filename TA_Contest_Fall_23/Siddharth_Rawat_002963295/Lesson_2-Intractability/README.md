# Intractability

## Traveling Salesman Problem (TSP)

The Traveling Salesman Problem (TSP) is a classic optimization problem in the field of computer science, operations research, and mathematics. It can be defined as follows:

Given a list of cities and the distances between each pair of cities, the Traveling Salesman Problem (TSP) seeks to find the shortest possible route that visits each city exactly once and returns to the starting city.

In other words, the problem involves finding a Hamiltonian cycle (a cycle that visits each vertex exactly once) in a weighted graph with the objective of minimizing the total weight or distance traveled.

Here are some key characteristics and points related to the TSP:

1. **Objective**: Minimize the total distance, cost, or time required to visit all cities exactly once and return to the starting city.

2. **Input**: The input consists of a set of cities and a distance matrix or a graph that provides the distances or costs between each pair of cities.

3. **Output**: The output is the optimal tour or route that specifies the order in which the cities should be visited to minimize the total distance.

4. **Complexity**: TSP is an NP-hard problem, meaning that there is no known algorithm that can find the optimal solution for all instances of the problem in polynomial time. As the number of cities increases, the number of possible tours grows factorial-ly, making it computationally expensive to find the exact solution for large instances.

5. **Applications**: The TSP has applications in various fields, including logistics, transportation, manufacturing, and circuit design. It is used to optimize routes for delivery vehicles, plan efficient manufacturing processes, design integrated circuits, and more.

6. **Variants**: There are several variations of the TSP, including the asymmetric TSP (where the distance from city A to city B may differ from the distance from B to A), the metric TSP (where distances satisfy the triangle inequality), and the time-dependent TSP (where travel times may vary with time of day).

Solving the TSP optimally for large instances is often impractical, and various approximation algorithms, heuristics, and meta-heuristics (such as genetic algorithms and simulated annealing) are employed to find good solutions quickly. Despite its computational challenges, the TSP remains a fundamental problem with real-world applications in route optimization and planning.

## How does TSP relate to NP type problems

The Traveling Salesman Problem (TSP) is closely related to the concept of NP-completeness, but it's important to clarify its specific status within the realm of computational complexity theory:

1. **NP (Nondeterministic Polynomial Time)**: TSP belongs to the class of NP problems. An NP problem is one for which, given a proposed solution, you can efficiently verify whether the solution is correct or not. In the context of TSP, if someone presents you with a tour that visits each city exactly once and returns to the starting city, you can easily verify that it's a valid tour and calculate its total distance in polynomial time.

2. **NP-Hardness**: TSP is also NP-hard. This means that it is as hard as the hardest problems in NP. In other words, if you could efficiently solve TSP, you could solve any problem in NP efficiently. This property makes TSP one of the most challenging problems in computational complexity theory.

So, to summarize:

- TSP is in NP because verifying a solution (checking if a proposed tour is valid) can be done in polynomial time.
- TSP is NP-hard because it is at least as hard as the hardest problems in NP, meaning that finding an exact solution for large instances of TSP is believed to be computationally infeasible in polynomial time.

In essence, the Traveling Salesman Problem serves as a key example of an NP-hard problem. While efficient algorithms and heuristics exist for solving small and moderately sized TSP instances, finding the optimal solution for large TSP instances is considered a computationally challenging task due to its NP-hardness. As a result, TSP is often used as a benchmark problem in the study of computational algorithms and optimization techniques.

## Pseudo code

### Brute force approach

A simplified pseudocode for solving the Traveling Salesman Problem (TSP) using a brute-force approach.

```
function travelingSalesmanProblem(graph):
    # Initialize variables
    numCities = number of cities in the graph
    bestTour = []  # Stores the best tour found so far
    bestDistance = INFINITY  # A large value

    # Helper function to generate permutations of cities
    function generatePermutations(currentTour):
        if length(currentTour) == numCities:
            distance = calculateTourDistance(currentTour, graph)
            if distance < bestDistance:
                bestDistance = distance
                bestTour = currentTour.copy()
        else:
            for each unvisited city:
                add city to currentTour
                generatePermutations(currentTour)
                remove city from currentTour

    # Start with the first city as the starting point
    startingCity = 0
    currentTour = [startingCity]

    # Generate all possible permutations of cities
    generatePermutations(currentTour)

    return bestTour, bestDistance

function calculateTourDistance(tour, graph):
    distance = 0
    numCities = length(tour)

    for i from 0 to numCities - 1:
        fromCity = tour[i]
        toCity = tour[(i + 1) % numCities]  # Loop back to the first city
        distance += graph[fromCity][toCity]

    return distance

# Example usage
graph = adjacency matrix or distance matrix of cities
bestTour, bestDistance = travelingSalesmanProblem(graph)
```

> NOTE: Please note that this pseudocode outlines a brute-force approach to solving the TSP, where all possible permutations of cities are generated and the total distance of each tour is calculated. This approach works for small instances of the problem but becomes impractical for large numbers of cities due to its exponential time complexity. More efficient algorithms, such as dynamic programming, branch and bound, or heuristic methods, are typically used for solving larger TSP instances.

## [Python implementation](./greedy-tsp.py)

## Quiz

Q1: What is the primary objective of the Traveling Salesman Problem (TSP)?

a. To find the fastest route between two cities. <br>
b. To find the shortest path between a set of cities. <br>
c. To determine the most scenic route for traveling. <br>
d. To calculate the distance between multiple cities.

<details>
<summary>Answer</summary>
    b. To find the shortest path between a set of cities
</details>
<br>

Q2: In the context of the TSP, what does a "tour" refer to?

a. A guided sightseeing trip in a city. <br>
b. A sequence of cities visited in a specific order. <br>
c. A map showing the locations of all cities. <br>
d. A list of tourist attractions in a city.

<details>
<summary>Answer</summary>
    b. A sequence of cities visited in a specific order
</details>
<br>

Q3: Which complexity class does the Traveling Salesman Problem belong to?

a. P <br>
b. NP <br>
c. NP-Hard <br>
d. Polynomial Time

<details>
<summary>Answer</summary>
    c. NP-Hard
</details>
<br>

Q4: In the TSP, what is the primary decision that needs to be made?

a. Selecting the optimal route for a given city. <br>
b. Determining the total number of cities to visit. <br>
c. Choosing the starting city for the tour. <br>
d. Deciding the order in which to visit cities.

<details>
<summary>Answer</summary>
    d. Choosing the starting city for the tour
</details>
<br>

Q5: What is the time complexity of finding the exact solution to the TSP for N cities using a brute-force approach?

a. O(N) <br>
b. O(N log N) <br>
c. O(2^N) <br>
d. O(N^2)

<details>
<summary>Answer</summary>
    c. O(2^N)
</details>
<br>

Q6: Which type of TSP variant allows for different distances or travel times between cities in different directions?

a. Metric TSP <br>
b. Asymmetric TSP <br>
c. Euclidean TSP <br>
d. Symmetric TSP

<details>
<summary>Answer</summary>
    b. Asymmetric TSP
</details>
<br>

Q7: Which famous optimization algorithm is often used to find approximate solutions to the Traveling Salesman Problem?

a. Bubble Sort <br>
b. Genetic Algorithm <br>
c. Breadth-First Search <br>
d. Depth-First Search

<details>
<summary>Answer</summary>
    b. Genetic Algorithm
</details>
<br>

Q8: What does the term "NP-hard" imply about the Traveling Salesman Problem?

a. It is an easy problem that can be solved quickly. <br>
b. It is computationally infeasible to find exact solutions. <br>
c. It has a straightforward, polynomial-time algorithm. <br>
d. It requires minimal computational resources to solve.

<details>
<summary>Answer</summary>
    b. It is computationally infeasible to find exact solutions
</details>
<br>
