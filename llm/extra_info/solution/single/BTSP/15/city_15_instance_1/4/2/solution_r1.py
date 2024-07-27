import itertools
import math

# City coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20),
          (18, 61), (40, 57), (57, 30), (36, 12),
          (93, 43), (17, 36), (4, 60), (78, 82),
          (83, 96), (60, 50), (98, 1)]

# Calculate Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

# Generate the distance matrix
distances = [
    [euclidean_distance(cities[i], cities[j]) for j in range(len(cities))]
    for i in range(len(cities))
]

# Greedy strategy to determine the best route minimizing the longest single travel between two consecutive cities
def greedy_minmax_tour(cities, distances):
    n = len(cities)
    unvisited = set(range(1, n))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: distances[last][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # return to the depot
    return tour

# Calculate tour by greedy strategy
tour = greedy_minmax_tour(cities, distances)

# Calculate the total cost and maximum distance between consecutive cities in the tour
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Display results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")