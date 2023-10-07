from collections import deque

def shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_intersection, path = queue.popleft()
        if current_intersection == end:
            return path
        visited.add(current_intersection)
        
        for neighbor in graph[current_intersection]:
            if neighbor not in visited:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append((neighbor, new_path))


def maintenance_path(graph, start):
    visited = set()
    path = []

    def dfs(current_intersection):
        visited.add(current_intersection)
        path.append(current_intersection)
        for neighbor in graph[current_intersection]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return path

def safest_path(graph, start, end):
    candidates = [(0, start, [])]
    visited = set()
    
    while candidates:
        candidates.sort(reverse=True)  # Sort by safety, descending
        safety_sum, current, path = candidates.pop(0)  # Get the safest route
        
        if current in visited:
            continue
        visited.add(current)
        
        path = path + [current]
        
        if current == end:
            return path
        
        for neighbor, safety in graph[current].items():
            if neighbor not in visited:
                new_safety_sum = safety_sum + safety
                candidates.append((new_safety_sum, neighbor, path))
                
    return "Not possible"

def min_charging_stops(graph, start, end, stations):
    visited = set()
    queue = deque([(start, [start], 0)])  # Node, Path, Stops

    while queue:
        current_node, path, stops = queue.popleft()
        visited.add(current_node)

        # If we reach the destination, return the path
        if current_node == end:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                new_stops = stops
                # If there is a charging station at the neighbor, reset the stops counter
                if neighbor in stations:
                    new_stops += 1
                # Add the neighbor node to the queue for future processing
                queue.append((neighbor, path + [neighbor], new_stops))

    # If a path is not found
    return None

# Test the function
weighted_graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'D': 4},
    'C': {'A': 2, 'D': 1, 'E': 5},
    'D': {'B': 4, 'C': 1, 'E': 2},
    'E': {'C': 5, 'D': 2}
}

# Example usage:

maintenance_path_graph = {
    'A': ['B', 'F'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['A', 'E', 'G'],
    'G': ['F']
}

graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E'],
    'C': ['F'],
    'D': ['E', 'G'],
    'E': ['F', 'H'],
    'F': ['I'],
    'G': ['H'],
    'H': ['I'],
    'I': []
}

start = 'A'
end = 'I'
stations = ['B', 'D', 'F', 'H']

result = shortest_path(graph, 'A', 'H')
print("Shortest path:", result)

result = maintenance_path(maintenance_path_graph, 'A')
print("Maintenance Path:", result)

print(safest_path(weighted_graph, 'A', 'E'))  
print(safest_path(weighted_graph, 'A', 'D')) 
print(safest_path(weighted_graph, 'A', 'B')) 

result = min_charging_stops(graph, start, end, stations)
print(result)

