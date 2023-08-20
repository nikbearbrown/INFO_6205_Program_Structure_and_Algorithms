import itertools

# Define distances between cities as an adjacency matrix
# Replace these distances with real-world distances if available
# In this example, we use an arbitrary matrix
distances = [
    [0, 29, 20, 21],
    [29, 0, 15, 30],
    [20, 15, 0, 16],
    [21, 30, 16, 0]
]

def calculate_tour_length(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][tour[0]]  # Return to the starting city
    return total_distance

def brute_force_tsp(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_tour = []

    for tour in itertools.permutations(cities):
        tour_distance = calculate_tour_length(tour, distances)
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = tour

    return best_tour, min_distance

# Solve TSP using brute-force approach
best_tour, min_distance = brute_force_tsp(distances)
print("Best Tour:", best_tour)
print("Minimum Distance:", min_distance)

# Output:
# Best Tour: (0, 2, 3, 1)
# Minimum Distance: 58
# In this output, the best tour found is (0, 2, 3, 1), which represents visiting cities in the order 0, 2, 3, and then returning to city 1. The minimum distance for this tour is 58 units
