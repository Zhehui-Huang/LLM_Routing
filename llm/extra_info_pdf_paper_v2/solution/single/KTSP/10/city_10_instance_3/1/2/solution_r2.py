import math
from itertools import permutations, combinations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute distance matrix (optional optimization for quicker look-ups)
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        if i != j:
            distance_matrix[i][j] = euclidean(des, j)
        else:
            distance_matrix[i][j] = 0

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance_matrix[tour[i - 1]][tour[i]]
    return total_cost

# Generate all possible combinations of cities that include the depot city 0 and 6 other cities
combinations_of_cities = combinations([i for i in cities.keys() if i != 0], 6)

min_cost = float('inf')
best_tour = None

# Evaluate all combinations and their permutations to find the optimal solution
for combination in combinations_of_cities:
    active_cities = [0] + list(combination)
    for perm in permutations(active_cities[1:]):
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the best tour found and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")