import math
import itertools

# City coordinates
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Compute distances matrix
n = len(coordinates)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        d = euclidean_distance(coordinates[i], coordinates[j])
        distances[i][j] = distances[j][i] = d

# Searching for the optimal route minimizing the max distance between any two consecutive cities

def find_optimal_tour():
    # We use permutations to try out every possible ordering
    # This approach is not feasible for large inputs but should work for n=15
    shortest_tour = None
    min_max_distance = float('inf')
    all_tours = itertools.permutations(range(1, n))
    
    for tour in all_tours:
        full_tour = [0] + list(tour) + [0]
        max_distance = max(distances[full_tour[i]][full_tour[i + 1]] for i in range(len(full_tour) - 1))
        total_distance = sum(distances[full_tour[i]][full_tour[i + 1]] for i in range(len(full_tour) - 1))
        
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            shortest_tour = full_tour
            best_total_distance = total = total_distance
            
    return shortest_tour, best_total_distance, min_max_distance

# Calculate the optimal tour
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")