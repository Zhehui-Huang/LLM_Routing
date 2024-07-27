import itertools
import math

# Cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Compute distances between every pair of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distances[(tour[i], tour[i + 1])]
    return total.scost

# Pick combinations of 4 additional cities
all_city_indices = list(cities.keys())
min_cost = float('inf')
best_tour = None

for combination in itertools.combinations(all_city_indices[1:], 4):  # Exclude the depot for combinations
    current_combination = [0] + list(combination)  # Include depot
    # Generate all permutations of the selected cities
    for perm in itertools.permutations(current_combination[1:]):
        tour = [0] + list(perm) + [0]  # Start and end at the depot
        tour_cost = calculate_tour_cost(tour)
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = tour

print("Tour:", best_tour)
print("Total travel cost:", min_cost)