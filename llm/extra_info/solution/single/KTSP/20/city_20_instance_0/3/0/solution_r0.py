import itertools
import math

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6),  # City 1
    (95, 33), # City 2
    (80, 60), # City 3
    (25, 18), # City 4
    (67, 23), # City 5
    (97, 32), # City 6
    (25, 71), # City 7
    (61, 16), # City 8
    (27, 91), # City 9
    (91, 46), # City 10
    (40, 87), # City 11
    (20, 97), # City 12
    (61, 25), # City 13
    (5, 59),  # City 14
    (62, 88), # City 15
    (13, 43), # City 16
    (61, 28), # City 17
    (60, 63), # City 18
    (93, 15)  # City 19
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all combinations of 3 cities (not including the depot city zero)
combos = itertools.combinations(range(1, 20), 3)

# Initialize the minimum cost and associated path
min_cost = float('inf')
best_tour = []

# Evaluate each combination
for combo in combos:
    perm_tours = itertools.permutations(combo)  # Permutations of the combo for finding shortest tour
    for tour in perm_tours:
        current_path_cost = distance(0, tour[0]) + distance(tour[0], tour[1]) + distance(tour[1], tour[2]) + distance(tour[2], 0)
        if current_path_cost < min_cost:
            min_cost = current_path_cost
            best_tour = [0, *tour, 0]

# Output results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {round(min_cost, 2)}")