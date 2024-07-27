from itertools import permutations
import math

# Coordinates of the cities including the depot
cities = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Compute the distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Brute-force search for the shortest tour using permutations
min_tour = None
min_cost = float('inf')

for perm in permutations(range(1, n)):  # Iterate over all permutations of cities (excluding the depot)
    current_tour = [0] + list(perm) + [0]
    current_cost = sum(distance_matrix[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour)-1))
    
    if current_cost < min_cost:
        min_cost = current_cost
        min_tour = current_tour

print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")