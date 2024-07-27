import math
from itertools import permutations

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Distance matrix
distance_matrix = {}
for i in cities.keys():
    distance_matrix[i] = {}
    for j in cities.keys():
        distance_matrix[i][j] = calculate_distance(i, j)

# Heuristic TSP solver based on nearest neighbor algorithm as initial heuristic (greedy)
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next = min(unvisited, key=lambda city: distance_matrix[current][city])
        tour.append(next)
        unvisited.remove(next)
        current = next
    tour.append(start) # Returning to the depot
    return tour

# Calculate total travel cost of the tour
def calculate_total_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i+1]]
    return total_cost

# Compute the initial tour and cost using the nearest neighbor algorithm
initial_tour = nearest_neighbor_tour(0)
initial_cost = calculate_total_cost(initial_tour)

# Output the results
print("Tour:", initial_tour)
print("Total travel cost:", initial_cost)