import math
from itertools import permutations

# Cities given as (index, (x, y))
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Construct a distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Simple heuristic: explore possible permutations and choose the one with the smallest longest distance
# Only feasible because of the small number of cities
def find_best_bottleneck_tour(cities):
    indices = list(cities.keys())
    best_distance = float('inf')
    best_tour = None
    
    for perm in permutations(indices):
        if perm[0] == 0:  # ensure the tour starts and ends at the depot
            perm += (0,) # return to the starting city
            
            max_leg_distance = max(distance_matrix[perm[i]][perm[i+1]] for i in range(len(perm) - 1))
            if max_leg_distance < best_distance:
                best_distance = max_leg_distance
                best_tour = perm
    
    # Calculate total cost of best tour
    total_cost = sum(distance_matrix[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour) - 1))
    
    return best_tour, total_cost, best_distance

# Find the best tour based on the bottleneck heuristic
tour, total_cost, max_dist = find_best_bottleneck_tour(cities)

# Output the results in the specified format
print(f"Tour: {list(tour)}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")