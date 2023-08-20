# Problem Statement

# Suppose you are given a set of cities and the distances between them. Your task is to find the shortest path between two cities using uniform cost search.

# Solution:

# We can represent the cities and their distances as a graph where the nodes are the cities and the edges are the distances between them. We can then use the uniform_cost_search function to find the shortest path between two cities.

import heapq

def uniform_cost_search(graph, start, goal):
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
    'New York': {'Chicago': 713, 'Boston': 215, 'Washington D.C.': 225},
    'Chicago': {'New York': 713, 'Denver': 1012, 'Los Angeles': 2015},
    'Boston': {'New York': 215, 'Washington D.C.': 442},
    'Washington D.C.': {'New York': 225, 'Boston': 442, 'Atlanta': 642},
    'Denver': {'Chicago': 1012, 'Los Angeles': 1015, 'Dallas': 799},
    'Los Angeles': {'Chicago': 2015, 'Denver': 1015, 'San Francisco': 383},
    'San Francisco': {'Los Angeles': 383, 'Seattle': 808},
    'Seattle': {'San Francisco': 808, 'Denver': 1306},
    'Dallas': {'Denver': 799, 'Atlanta': 721},
    'Atlanta': {'Washington D.C.': 642, 'Dallas': 721}
}

start = 'New York'
goal = 'San Francisco'

result = uniform_cost_search(graph, start, goal)

if result is not None:
    (path, cost) = result
    print('Shortest path from', start, 'to', goal, 'is', path, 'with a cost of', cost)
else:
    print('No path found from', start, 'to', goal)


# Output

# Shortest path from New York to San Francisco is ['New York', 'Chicago', 'Los Angeles', 'San Francisco'] with a cost of 3111

