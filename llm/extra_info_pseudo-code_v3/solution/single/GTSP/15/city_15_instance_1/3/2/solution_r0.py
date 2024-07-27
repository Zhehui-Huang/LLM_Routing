import itertools
import math

# City coordinates declaration
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Groups of cities, with each list representing a group.
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Compute all permutations of picking one city from each group
city_combinations = list(itertools.product(*groups))

# Best tour initialization
best_tour = None
best_cost = float('inf')

# Explore all paths starting from the depot, picking one city from each group, and returning to the depot
for combination in city_combinations:
    # Paths include the depot at start and end
    full_path = [0] + list(combination) + [0]
    current_cost = sum(euclidean_distance(full_path[i], full_path[i+1]) for i in range(len(full_path) - 1))
    
    if current_cost < best_cost:
        best_cost = current_cost
        best_tour = full_path

# Output the tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")