from itertools import permutations, combinations
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
    (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

# Precompute distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_cost(cities[i], cities[j])

# Iterate over combinations of 9 cities (excluding depot)
min_distance = float('inf')
best_tour = None

for chosen_cities in combinations(range(1, 15), 9):
    # Include the depot city
    tour_cities = [0] + list(chosen_cities) + [0]
    
    # Iterate over all permutations of the selected cities
    for perm in permutations(tour_cities[1:-1]):
        perm_tour = [0] + list(perm) + [0]
        tour_cost = sum(distance_matrix[perm_tour[i]][perm_tour[i+1]] for i in range(len(perm_tour)-1))
        
        # Update the shortest tour found so far
        if tour_cost < min_distance:
            min_distance = tour_cost
            best_tour = perm_tour

# Output the best tour found and its total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")