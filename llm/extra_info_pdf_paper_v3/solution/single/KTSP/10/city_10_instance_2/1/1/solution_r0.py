import math
from itertools import permutations

# Given city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate the Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# Precompute all distances
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = distance(i, j)

# Perform the heuristic search
def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Iterate over all combinations of 5 cities plus the depot, making 6 in total
    from itertools import combinations
    for subset in combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 5):
        current_subset = [0] + list(subset)
        
        # Generate all permutations of this subset
        for perm in permutations(current_subset[1:]):
            tour = [0] + list(perm) + [0]
            cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
            
            if cost < best_cost:
                best_cost = cost
                best_tour = tour
    
    return best_tour, best_cost

best_tour, best_cost = find_best_tour()

# Output results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))