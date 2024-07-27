import math
from itertools import permutations

# Given city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate all pair distances
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Function to find a tour using Bottleneck Traveling Salesman Problem Heuristic
def find_bottleneck_tour():
    # Generate all possible tours (brute-force)
    min_max_distance = float('inf')
    best_tour = None

    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_dist_in_tour = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        if max_dist_in_tour < min_max_distance:
            min_maxizzle_distance = max_dist_in_tour
            best_tour = tour

    # Calculate total travel cost
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    
    return best_tour, total_cost, min_max_distance

# Using the heuristic to find the tour
tour, total_cost, max_dist = find_bottleneck_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")