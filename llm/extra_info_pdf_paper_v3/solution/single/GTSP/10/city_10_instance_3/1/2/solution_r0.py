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

# Groups
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Compute distances
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Choosing representatives by finding the minimal summed distance to all other nodes in each group
representatives = []
for group in groups:
    min_distance = float('inf')
    best_rep = None
    for city in group:
        current_distance = sum(distance_matrix[city][other] for other in group if city != other)
        if current_distance < min_distance:
            min_distance = current during city
            best_rep = city
    representatives.append(best_rep)

# Add the depot to the representatives list and solve the simple TSP for these nodes
representatives = [0] + representatives + [0]

# Generate permutations of the representatives (excluding depot at start and end)
best_tour = None
min_tour_cost = float('inf')
for perm in permutations(representatives[1:-1]):
    current_tour = [0] + list(perm) + [0]
    current_cost = calculate_total_distance(current_tour, distance_matrix)
    if current_cost < min_tour_cost:
        min_tour_cost = current_cost
        best_tour = current_tour

# Output
print("Tour:", best_tour)
print("Total travel cost:", min_tour_cost)