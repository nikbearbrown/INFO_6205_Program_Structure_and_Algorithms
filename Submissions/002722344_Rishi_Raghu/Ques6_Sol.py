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
    visited = set()
    queue = deque([(start, [start], 0)])  # Node, path, safety_sum
    
    safest_route = None
    max_safety = float('-inf')
    
    while queue:
        current, path, safety_sum = queue.popleft()
        if current == end:
            if safety_sum > max_safety:
                max_safety = safety_sum
                safest_route = path
            continue
          
        visited.add(current)
        
        for neighbor, safety in graph[current].items():
            if neighbor not in visited:
                new_safety_sum = safety_sum + safety
                queue.append((neighbor, path + [neighbor], new_safety_sum))
                
    return safest_route

def find_loops(graph, start):
    visited = set()
    stack = []
    
    def dfs(current, stack):
        if current in stack:
            return stack[stack.index(current):]
        
        if current in visited:
            return []
        
        visited.add(current)
        stack.append(current)
        
        for neighbor in graph[current]:
            loop = dfs(neighbor, stack)
            if loop:
                return loop
        
        stack.pop()
        return []
    
    return dfs(start, stack)




# Test the function
weighted_graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'D': 4},
    'C': {'A': 2, 'D': 1},
    'D': {'B': 4, 'C': 1}
}

# Example usage:

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D', 'F', 'G'],
    'F': ['E', 'G'],
    'G': ['E', 'F']
}

graph_new = {
    'W': ['X', 'Z'],
    'X': ['W', 'Y'],
    'Y': ['Z', 'X'],
    'Z': ['W', 'Y']
}



result = maintenance_path(graph, 'A')
print("Maintenance Path:", result)

result = shortest_path(graph, 'A', 'H')
print("Shortest path from A to H:", result)

print(safest_path(weighted_graph, 'A', 'D'))  # Output could be ['A', 'B', 'D']

print(find_loops(graph_new, 'W'))  # Output should be ['A', 'B', 'C']
