# Uniform Cost Search Algorithm

Uniform Cost Search (UCS) is a widely used graph search algorithm. The goal of UCS is to find the path from a starting node to a goal node with the most minor cost. Uniform-Cost Search is similar to Dijkstra’s algorithm

![Map with Cities](https://cdn.discordapp.com/attachments/1105610567454052406/1142853926522191922/skunks.ai_np-complete_algorithm_cities_dd7a2e51-fb62-4e4d-8d62-2892e3c751da.png)

## **Table of Contents**

| **Section** | **Link**              |
|-------------|-----------------------|
| Video       | [Video Link](#)       |
| Theory      | [Theory.pdf](#)      |
| Quiz        | [Quiz.pdf](#)        |
| Slides      | [Slides.pdf](#)      |

## **Step-by-Step Breakdown of the UCS Algorithm** 

1. **Initialize the starting node:** Set the distance of the starting node to 0 and insert it into the priority queue.
2. **Repeat until the priority queue is empty:**
   a. Select the node with the lowest priority (smallest cumulative cost) from the priority queue.
   b. If the selected node is the target node, stop the search and return the path.
   c. For each neighbor of the selected node:
      - Calculate the cumulative cost of the path to the neighbor.
      - If the neighbor has not been visited or the new cumulative cost is lower, update the neighbor's cumulative cost and insert it into the priority queue.
3. **If the target node was not found, return "target not found".**

## **Pseudocode for the UCS Algorithm** 💻

```bash
function uniform_cost_search(start, goal)
    initialize the priority queue with the start node
    initialize an empty set of visited nodes
    while the priority queue is not empty:
        dequeue the node with the lowest priority from the queue
        if the dequeued node is the goal node:
            return the path to the goal node
        if the dequeued node is not in the visited set:
            add the dequeued node to the visited set
            for each neighbor of the dequeued node:
                calculate the cumulative cost of the path to the neighbor
                if the neighbor has not been visited or if the new cumulative cost is lower:
                    update the neighbor's cumulative cost and insert it into the priority queue
    return "target not found"
```

## **Complexity Analysis** 

The time and space complexity of the Uniform Cost Search algorithm can be summarized as follows:

- **Time Complexity:** The time complexity of the UCS algorithm is determined by the number of nodes expanded during the search. In the worst case, where all paths need to be explored, the algorithm has a time complexity of O(b^d), where "b" is the branching factor of the graph and "d" is the depth of the solution.

- **Space Complexity:** The space complexity of the UCS algorithm is determined by the maximum number of nodes stored in memory at any given time. In the worst case, the algorithm needs to store all nodes in the priority queue, resulting in a space complexity of O(b^d).

## **Real-world Applications of UCS Algorithm** 🏭

The Uniform Cost Search algorithm finds applications in various domains:
1. Route Planning
2. Game AI
3. Robotics
4. Natural Language Processing
5. Supply Chain Optimization
6. Network Routing
7. Medical Diagnosis
