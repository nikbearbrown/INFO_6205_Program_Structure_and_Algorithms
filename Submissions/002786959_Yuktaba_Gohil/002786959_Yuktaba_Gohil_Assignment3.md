In the process of completing this assignment, I learnt several key concepts related to which I would like to mention here. Through various tasks and questions, I gained 
a deeper understanding of the following topics:

**<u>Bellman-Ford's Algorithm:</u>**

+ Bellman-Ford is a single source shortest path algorithm that determines the shortest path between a given source vertex and every other vertex in a graph. This algorithm can be used on both weighted and unweighted graphs.
+ Although Bellman-Ford is slower than Dijkstra’s algorithm, it is capable of handling graphs with negative edge weights, which makes it more versatile.
+ The shortest path cannot be found if there exists a negative cycle in the graph.Bellman-Ford is also capable of detecting negative cycles, which is an important feature.

***The idea behind Bellman Ford Algorithm:***

+ The Bellman-Ford algorithm’s primary principle is that it starts with a single source and calculates the distance to each node. The distance is initially unknown and assumed to be infinite, but as time goes on, the algorithm relaxes those paths by identifying a few shorter paths. Hence it is said that Bellman-Ford is based on “Principle of Relaxation“.

***Principle of Relaxation of Edges for Bellman-Ford:***

+ It states that for the graph having N vertices, all the edges should be relaxed N-1 times to compute the single source shortest path.
+ In order to detect whether a negative cycle exists or not, relax all the edge one more time and if the shortest distance for any node reduces then we can say that a negative cycle exists. In short if we relax the edges N times, and there is any change in the shortest distance of any node between the N-1th and Nth relaxation than a negative cycle exists, otherwise not exist.

***Drawback of Bellman Ford’s Algorithm:***
+ Bellman-Ford algorithm will fail if the graph contains any negative edge cycle.

**Ford-Fulkerson Algorithm:**

+ The Ford-Fulkerson algorithm is a widely used algorithm to solve the maximum flow problem in a flow network. 
+ The maximum flow problem involves determining the maximum amount of flow that can be sent from a source vertex to a sink vertex in a directed weighted graph, subject to capacity constraints on the edges.
+ The algorithm works by iteratively finding an augmenting path, which is a path from the source to the sink in the residual graph, i.e., the graph obtained by subtracting the current flow from the capacity of each edge. 
+  The algorithm then increases the flow along this path by the maximum possible amount, which is the minimum capacity of the edges along the path.

The following is simple idea of Ford-Fulkerson algorithm:

1. Start with initial flow as 0.
2. While there exists an augmenting path from the source to the sink:  
   + Find an augmenting path using any path-finding algorithm, such as breadth-first search or depth-first search.
   + Determine the amount of flow that can be sent along the augmenting path, which is the minimum residual capacity along the edges of the path.
   + Increase the flow along the augmenting path by the determined amount.
3. Return the maximum flow.

**Push-Relabel Algorithm**

The Push-Relabel algorithm is a widely used algorithm for solving the maximum flow problem in a flow network. This algorithm is more efficient than the Ford-Fulkerson method, particularly when dealing with dense networks. It was developed to improve the worst-case time complexity of maximum flow algorithms.

Here's an overview of how the Push-Relabel algorithm works:

+ Initialization: Initially, the algorithm sets the flow to zero for all edges and computes initial preflows (a preliminary assignment of flow values) with excess flow at the source node (pushing flow from the source).

+ Push Operation: The algorithm iteratively performs a "push" operation on nodes with excess flow, trying to send excess flow to adjacent nodes. The push operation selects a node with excess flow (excluding the source and sink) and pushes as much flow as possible to its neighbors.

To do this, it selects an adjacent node and pushes flow from the source to the sink, while respecting the capacity constraints of the edges. The push operation continues until the selected node no longer has excess flow or there are no valid neighbors to push flow to.

+ Relabel Operation: If a node has excess flow and cannot push it to any neighbor, it is "re-labeled." This means its height (distance from the sink) is increased to allow the flow to be pushed towards the sink. This step helps to avoid excessive back-and-forth pushing.

+ Termination: The algorithm continues pushing and relabeling until there are no nodes with excess flow left. At this point, the algorithm has found the maximum flow, and it terminates.

+ Final Max Flow: The final result is the maximum flow found in the network.

Key features and concepts of the Push-Relabel algorithm:

+ Height: The algorithm maintains a "height" for each node, representing its distance from the sink. The height of the source is set to the number of nodes in the network.

+ Relabeling: The algorithm increases the height of a node to ensure that it pushes flow towards the sink. This step avoids excessive pushing between nodes.

+ Selection of Active Nodes: The algorithm selects nodes with excess flow (excluding the source and sink) and pushes flow from these nodes. This choice is guided by the "highest label first" rule, which ensures that the algorithm operates efficiently.

+ Capacity Scaling: To further improve efficiency, a variation called "capacity scaling" can be applied. This method starts with a small scaling factor and gradually increases it as the algorithm progresses, reducing the number of iterations.

The Push-Relabel algorithm is known for its efficient performance in practice and has several optimizations and variations to improve its efficiency further. It has been widely used in various applications, including network flow problems, transportation planning, and computer network routing.
