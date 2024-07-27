import math
from itertools import permutations

# Define the cities' coordinates
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

# Define a function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate distances between all pairs of cities
distances = {}

for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calc_distance(i, j)

# Solve the Traveling Salesman Problem using Held-Karp algorithm (brute-force for small number of cities)
min_cost = float('inf')
best_tour = None

for perm in permutations(range(1, 10)):  # Permutate over cities 1-9 (excluding depot which is 0)
    cost = distances[(0, perm[0])]  # Start the tour from the depot
    tour = [0] + list(perm) + [0]
    
    for i in range(len(perm) - 1):
        cost += distances[(perm[i], perm[i + 1])]
    cost += distances[(perm[-1], 0)]  # Return to the depot

    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output the best tour and the minimal travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")