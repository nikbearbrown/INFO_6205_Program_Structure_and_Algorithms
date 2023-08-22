import itertools
import sys

# Function to calculate the total distance of a tour
def totalDistance(tour, distances):
    total = 0
    numCities = len(tour)
    for i in range(numCities):
        total += distances[tour[i]][tour[(i+1) % numCities]]
    return total

# Brute-force TSP solver
def tspBruteForce(distances):
    numCities = len(distances)
    if numCities <= 2:
        return list(range(numCities))
    minTour = None
    minDistance = sys.maxsize

    # Generate all possible permutations of cities
    for tour in itertools.permutations(range(1, numCities)):
        tour = (0,) + tour # start from city 0
        dist = totalDistance(tour, distances)
        if dist < minDistance:
            minDistance = dist
            minTour = tour
    return minTour, minDistance

# Driver Code
if __name__ == '__main__':
    # Define the distances between cities as a 2D matrix
    distances = [
        [0, 29, 20, 21],
        [29, 0, 15, 17],
        [20, 15, 0, 28],
        [21, 17, 28, 0]
    ]

    # Find the optimal tour and its distance
    optimalTour, optimalDistance = tspBruteForce(distances)

    print('Optimal Tour: ', optimalTour)
    print('Optimal Distance: ', optimalDistance)
