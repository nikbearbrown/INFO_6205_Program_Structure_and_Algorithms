# Problem statement: Given a weighted graph, find the shortest path between a source node and a destination node using the Uniform Cost Search algorithm.

# Solution:

# We can solve this problem using the Uniform Cost Search algorithm with a priority queue to store the fringe. The priority of each node in the fringe will be its path cost from the source node. We will expand nodes in the fringe in increasing order of their path cost until we reach the destination node or we have expanded all nodes in the graph.


# The uniform_cost_search function takes as input a graph represented as a dictionary of dictionaries, where each key-value pair represents a weighted edge between two nodes and its cost. The function also takes the start and goal nodes as input.

# We initialize the fringe with the start node and its path cost of 0. We use a priority queue implemented as a heap to keep track of the nodes in the fringe, with the priority of each node being its path cost from the start node. We also keep track of the visited nodes in a set.

# We then enter a loop where we pop the node with the lowest path cost from the fringe. If we have already visited this node, we skip it. Otherwise, we add it to the visited set and append it to the current path.

# If we have reached the goal node, we return the path and its cost. Otherwise, we expand the current node by adding its neighbors to the fringe with their respective path costs. We use the heap to maintain the order of nodes in the fringe by their path costs.

# If we have expanded all nodes in the graph without reaching the goal, we return None to indicate that there is no path.

# Here is an example of how to use the uniform_cost_search function to find the shortest path between nodes in a graph:


import heapq

def uniform_cost_search(graph, start, goal):
    # Initialize the fringe with the start node and its path cost
    fringe = [(0, start, [])]
    visited = set()
    
    while fringe:
        (cost, node, path) = heapq.heappop(fringe)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        path = path + [node]
        
        if node == goal:
            return (path, cost)
        
        for neighbor, neighbor_cost in graph[node].items():
            if neighbor not in visited:
                new_cost = cost + neighbor_cost
                heapq.heappush(fringe, (new_cost, neighbor, path))
    
    return None


graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 2},
    'D': {'G': 1},
    'E': {'G': 3},
    'F': {'H': 5},
    'G': {'H': 2},
    'H': {}
}

start = 'A'
goal = 'H'

result = uniform_cost_search(graph, start, goal)
if result is not None:
    (path, cost) = result
    print('Shortest path from', start, 'to', goal, 'is', path, 'with a cost of', cost)
else:
    print('No path found from', start, 'to', goal)


# Output
# Shortest path from A to H is ['A', 'B', 'D', 'G', 'H'] with a cost of 8
