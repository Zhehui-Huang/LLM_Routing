import math
import itertools

# City coordinates
cities = {
    0: (14, 77), # depot
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Grouping of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix: calculate distances from each city to every other city
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Generate all combinations, one city from each group including the depot
def find_best_tour():
    all_combinations = itertools.product(*groups)
    best_tour = None
    best_cost = float('inf')
    
    for combination in all_combinations:
        for perm in itertools.permutations(combination):
            tour = [0] + list(perm) + [0]
            cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
            if cost < best_cost:
                best_tour = tour
                best_cost = cost
                
    return best_tour, best_cost

# Compute the best tour and its cost
best_tour, best_cost = find_best_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")