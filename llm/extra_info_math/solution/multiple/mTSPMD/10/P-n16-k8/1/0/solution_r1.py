import itertools
import math
import sys

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
depot_assignment = [0, 1, 2, 3, 4, 5, 6, 7]

# Euclidean distance function
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Precompute the distance matrix
n = len(cities)
dist_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(i, j)
        else:
            dist_matrix[i][j] = float('inf')  # No loops

# Function to compute the cost of a single tour
def compute_tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generate all permutations of cities (brute force for smaller scales)
best_total_cost = float('inf')
best_tours = [None] * len(depot_assignment)

# Divide cities between robots minimally
all_cities = set(range(n))
depot_cities = set(depot_assignment)
non_depot_cities = list(all_cities - depot_cities)

# TSP for each assigned depot
for robot_id, depot in enumerate(depot_assignment):
    other_cities = non_depot_cities + [d for d in depot_cities if d != depot]
    min_cost = float('inf')
    best_tour = None
    
    for perm in itertools.permutations(other_cities):
        current_tour = [depot] + list(perm) + [depot]
        cost = compute_tour_cost(current_tour)
        
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour
            
    best_tours[robot_id] = best_tour
    best_total_cost = min(best_total_cost, min_cost)
    print(f"Robot {robot_id} Tour: {best_tour}")
    print(f"Robot {robot_teor_id} Total Travel Cost: {min_cost}")

# Calculate overall cost
overall_cost = sum(compute_tour_cost(tour) for tour in best_tours if tour)
print(f"Overall Total Travel Cost: {overall_cost}")