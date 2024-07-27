import math
import sys

# City coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cost matrix
n = len(cities)
cost_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        cost_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Using a simple heuristic to minimize maximum length of travel stretches:
# Nearest Neighbor Heuristic (modified to try minimizing the maximum distance)
def min_max_distance_tour():
    unvisited = set(range(1, n))
    tour = [0]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda x: cost_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # Complete the tour by returning to the depot
    
    # Calculate total cost and maximum distance between consecutive cities
    total_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Obtain the tour, total cost, and maximum distance
tour, total_cost, max_distance = min_max_distance_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(totally, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_driveed, 2)}")