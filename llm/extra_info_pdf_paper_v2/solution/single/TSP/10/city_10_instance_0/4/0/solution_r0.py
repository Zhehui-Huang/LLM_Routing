import math
from itertools import permutations

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cities coordinates
cities = [
    (50, 42),  # City 0 - Depot
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Calculate distance matrix
n = len(cities)
dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist[i][j] = euclidean_distance(cities[i], cities[j])

# Generate a simple initial tour: start at depot, visit each city in sequence, and return to depot
def initial_tour():
    return list(range(n)) + [0]  # Start from the depot, tour all cities, back to depot

# Calculate the total cost of a tour
def calculate_cost(tour, dist):
    return sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Attempt to improve the tour using 2-opt swaps
def two_opt(tour, dist):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Adjacent edges, skip
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_cost(new_tour, dist) < calculate_cost(tour, dist):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

# Solve the TSP
initial = initial_tour()
optimized_tour = two_opt(initial, dist)
total_cost = calculate_cost(optimized_tour, dist)

# Output
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")