import math
from itertools import permutations

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_distance(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# City coordinates
cities = [
    (84, 67),  # Depot 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Compute distances
distance_matrix = [[euclidean distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Find best representative for each group
best_rep = []
for group in groups:
    best_city = None
    min_distance = float('inf')
    for city1 in group:
        distance_to_depot = distance_matrix[city1][0] + distance_matrix[0][city1]
        if distance_to_depot < min_distance:
            min_distance = distance_to_depot
            best_city = city1
    best_rep.append(best_city)

# Include depot at the start and end
tour_options = [0] + best_rep + [0]

# Searching for the best tour
min_cost = float('inf')
best_tour = None
for perm in permutations(best_rep):
    current_tour = [0] + list(perm) + [0]
    cost = calculate_total_distance(current_tour, distance_matrix)
    if cost < min_cost:
        min_cost = cost
        best_tour = current_tour

# Print results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)