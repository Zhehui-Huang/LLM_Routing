import math
from itertools import permutations

# List of city coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance between two cities
def euclidean_dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Number of cities
n = len(cities)

# Compute the distance matrix
dist_matrix = [[euclidean_dist(i, j) for j in range(n)] for i in range(n)]

def find_tour():
    # Simple heuristic to find an initial solution (Nearest Neighbor starting from the depot)
    remaining_cities = set(range(1, n))
    tour = [0]
    while remaining_cities:
        last_city = tour[-1]
        next_city = min(remaining_cities, key=lambda x: dist_matrix[last_city][x])
        tour.append(next_city)
        remaining_cities.remove(next_city)
    tour.append(0)  # return to the depot
    
    # Find max distance between consecutive cities
    max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    # Total travel cost
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return tour, total_cost, max_distance

# Get the tour, cost and maximum edge length
tour, total_cost, max_distance = find_tour()

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")