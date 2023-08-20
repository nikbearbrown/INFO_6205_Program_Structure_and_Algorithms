# You are given a list of cities in a country and a map of roads connecting them. The cost of traveling on each road is represented by a non-negative integer. You want to travel from city A to city B, but you have a strict budget that you cannot exceed. Write a Python function that finds the cheapest route from A to B within your budget, using uniform cost search.

# Function signature: def cheapest_route(start: str, end: str, budget: int, roads: List[Tuple[str, str, int]]) -> List[str]

# Input:

# start: A string representing the starting city.
# end: A string representing the destination city.
# budget: An integer representing the maximum cost you can afford.
# roads: A list of tuples representing the roads connecting the cities. Each tuple is of the form (city1, city2, cost) where city1 and city2 are strings representing the two cities connected by the road, and cost is the non-negative integer representing the cost of traveling on that road.
# Output:

# A list of strings representing the cities in the cheapest route from start to end within the given budget. If there is no route within the budget, return an empty list.

import heapq

def cheapest_route(start, end, budget, roads):
    graph = {}
    for city in set([start, end] + [c1 for c1, c2, _ in roads] + [c2 for c1, c2, _ in roads]):
        graph[city] = {}
    for c1, c2, cost in roads:
        graph[c1][c2] = cost
        graph[c2][c1] = cost
    
    current_cost = 0
    heap = [(0, [start])]
    
    while heap:
        (cost, path) = heapq.heappop(heap)
        current_city = path[-1]
        if current_city == end:
            return path
        for neighbor, road_cost in graph[current_city].items():
            new_cost = cost + road_cost
            if new_cost <= budget and neighbor not in path:
                new_path = path + [neighbor]
                heapq.heappush(heap, (new_cost, new_path))
    
    return []


cities = ['A', 'B', 'C', 'D', 'E']
roads = [('A', 'B', 5), ('A', 'C', 2), ('B', 'D', 7), ('C', 'D', 1), ('C', 'E', 3), ('D', 'E', 8)]

print(cheapest_route('A', 'E', 10, roads))
# Output ['A', 'C', 'E']

print(cheapest_route('A', 'E', 6, roads))
#Output []
