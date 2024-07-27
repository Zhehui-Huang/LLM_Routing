from math import sqrt
from itertools import permutations

def compute_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Compute the distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        if i != j:
            distance_matrix[i][j] = compute_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])

# Finding a path minimizing the maximum distance between any two consecutive cities
best_tour = None
best_max_distance = float('inf')
best_total_cost = float('inf')

# Generate all permutations of cities dropped the depot city
for perm in permutations(range(1, 15)):
    # Complete Tour
    tour = [0] + list(perm) + [0]
    total_cost = 0
    max_distance = 0
    valid_tour = True
    
    for i in range(len(tour) - 1):
        cost = distance_matrix[tour[i]][tour[i + 1]]
        total_cost += cost
        if cost > max_distance:
            max_distance = cost
        # Early stop if current max distance already larger than best found
        if max_distance > best_max_distance:
            valid_tour = False
            break
        
    if valid_tour and (max_distance < best_max_distance or (max_distance == best_max_distance and total_cost < best_total_cost)):
        best_tour = tour
        best_max_distance = max_distance
        best_total_cost = total_cost

# Print the best tour found
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_total_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")