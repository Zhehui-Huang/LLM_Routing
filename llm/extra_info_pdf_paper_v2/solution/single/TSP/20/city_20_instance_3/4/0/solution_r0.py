import math
from itertools import permutations

# Coordinates of the cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Creating the distance matrix
distance_matrix = [[0]*20 for _ in range(20)]
for i in range(20):
    for j in range(20):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = 0

def calculate_total_distance(tour):
    total_distance = 0
    for k in range(len(tour)-1):
        total_distance += distance_matrix[tour[k]][tour[k+1]]
    return total_distance

def get_initial_tour():
    return list(range(20)) + [0]

def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if j-i == 1: continue  # Do not swap consecutive nodes
                new_tour = tour[:]
                new_tour[i:j+1] = tour[j:i-1:-1]
                if calculate_total_distance(new_tour) < calculate_total_distance(best):
                    best = new_tour
                    improved = True
        tour = best
    return tour

# Get initial feasible solution
initial_tour = get_initial_tour()
# Improve initial solution using Two-opt
opt_tour = two_opt(initial_tour)
total_cost = calculate_total_distance(opt_tour)

# Print out the resulting tour and its total cost
print(f"Tour: {opt_tour}")
print(f"Total travel cost: {total_cost:.2f}")