import math
from itertools import permutations

# Define city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Utility function to calculate Euclidean distance between two points
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate the distance matrix
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Attempt to find the optimal tour using a simple approach focusing on minimizing the maximum leg distance
def find_minimal_max_distance_tour():
    min_max_distance = float('inf')
    best_tour = None
    
    # Try all permutations of the cities (except the starting city 0)
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_leg_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_leg_distance < min_max_distance:
            min_max_distance = max_leg_distance
            best_tour = tour
            best_total_distance = total_length
    
    return best_tour, best_total_distance, min_max_distance

# Run the function and obtain the outputs
tour, total_cost, max_distance = find_minimal_max_distance_tour()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")