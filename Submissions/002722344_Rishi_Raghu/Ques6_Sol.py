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
    'A': {'B': 5},
    'B': {'A': 5, 'C': 5, 'D': 5},
    'C': {'B': 5, 'E': 5},
    'D': {'B': 5, 'E': 5},
    'E': {'C': 5, 'D': 5}
}

# Example usage:

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



result = shortest_path(graph, 'A', 'D')
print("Shortest path:", result)

result = maintenance_path(graph, 'A')
print("Maintenance Path:", result)

# print(safest_path(weighted_graph, 'A', 'E'))  # Output could be ['A', 'C', 'D', 'E']
# print(safest_path(weighted_graph, 'A', 'D'))  # Output could be ['A', 'C', 'D']
# print(safest_path(weighted_graph, 'A', 'B'))  # Output could be ['A', 'B']

result = min_charging_stops(graph, start, end, stations)
print(result)

# graph1 = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B', 'H'],
#     'E': ['B', 'H'],
#     'F': ['C', 'I'],
#     'G': ['C', 'I'],
#     'H': ['D', 'E', 'I'],
#     'I': ['F', 'G', 'H']
# }
# stations1 = ['B', 'E', 'G', 'I']
# start1 = 'A'
# end1 = 'I'
# path1, stops1 = min_charging_stops(graph1, start1, end1, stations1)
# print(f"Test Case 1:\nPath: {path1}\nCharging Stops: {stops1}")

# graph2 = {
#     'A': ['B', 'D'],
#     'B': ['A', 'C', 'E'],
#     'C': ['B', 'E'],
#     'D': ['A', 'E'],
#     'E': ['B', 'C', 'D'],
#     'F': ['E', 'G'],
#     'G': ['F', 'H'],
#     'H': ['G', 'I'],
#     'I': ['H']
# }
# stations2 = ['C', 'F', 'H']
# start2 = 'A'
# end2 = 'I'
# path2, stops2 = min_charging_stops(graph2, start2, end2, stations2)
# print(f"Test Case 2:\nPath: {path2}\nCharging Stops: {stops2}")

# graph3 = {
#     'A': ['B'],
#     'B': ['A', 'C'],
#     'C': ['B', 'D'],
#     'D': ['C']
# }
# stations3 = ['B']
# start3 = 'A'
# end3 = 'D'
# path3, stops3 = min_charging_stops(graph3, start3, end3, stations3)
# print(f"Test Case 3:\nPath: {path3}\nCharging Stops: {stops3}")
