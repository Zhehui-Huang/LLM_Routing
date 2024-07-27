import math
from itertools import combinations, permutations

# City coordinates
coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance between two cities
def euclidean_dist(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generating all possible city trip combinations including the depot
possible_tours = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)  # choose 3 cities besides the depot

best_tour = None
min_cost = float('inf')

# Evaluate each possible city combination
for cities in possible_tours:
    full_tour = [0] + list(cities) + [0]  # complete loop
    for tour_permutation in permutations(full_tour[1:-1]):  # permute the middle cities
        current_tour = [0] + list(tour_permutation) + [0]
        current_cost = sum(euclidean_dist(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))

        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the best tour and the associated travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))