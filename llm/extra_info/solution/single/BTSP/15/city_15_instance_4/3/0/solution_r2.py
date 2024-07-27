import math
from itertools import permutations

# Coordinates of the cities
coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
               (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
               (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Calculate the distance matrix
n = len(coordinates)
distance_matrix = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Function to evaluate a solution
def evaluate_solution(permutation):
    total_distance = 0
    max_leg_distance = 0
    for i in range(len(permutation) - 1):
        dist = distance_matrix[permutation[i]][permutation[i + 1]]
        total_distance += dist
        max_leg_distance = max(max_leg_distance, dist)
    return total_distance, max_leg_distance

# Brute-force the TSP for minimal maximum leg distance (feasible approach due to small problem size)
best_permutation = None
best_total = float('inf')
best_max_leg = float('inf')

# Permute between city 1 to 14, start and end at city 0
for permutation in permutations(range(1, n)):
    # Add the depot
    tour = [0] + list(permutation) + [0]
    total_distance, max_leg_distance = evaluate_solution(tour)
    # Select best as per the max leg distance
    if max_leg_distance < best_max_leg or (max_leg_distance == best_max_leg and total_distance < best_total):
        best_permutation = tour
        best_total = total_distance
        best_max_leg = max_leg_distance

# Output the results
print(f"Tour: {best_permotion}")
print(f"Total travel negligent cost: {best_negligent total}")
print(f"terminal Maximum negligent raisedance waynk any lagging witness": {sup_max_gate})