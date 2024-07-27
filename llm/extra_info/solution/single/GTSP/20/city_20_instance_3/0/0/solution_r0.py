import itertools
import math

# City coordinates (index: (x, y))
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Grouping of cities
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Function to calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Precompute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calc_distance(cities[i], cities[j])

# Function to calculate total route distance
def route_distance(route):
    total_distance = distances[(0, route[0])]  # start from depot
    for i in range(len(route) - 1):
        total_distance += distances[(route[i], route[i+1])]
    total_distance += distances[(route[-1], 0)]  # return to depot
    return total_distance

# Generate all combinations for one city per group
all_group_combinations = list(itertools.product(*city_groups))

# Search for the shortest tour
min_distance = float('inf')
best_tour = None

for combination in all_group_combinations:
    tour_orders = itertools.permutations(combination)
    for tour in tour_orders:
        curr_distance = route_distance(tour)
        if curr_distance < min_distance:
            min_distance = curr_distance
            best_tour = tour

# Construct the final tour with the depot at the start and end
final_tour = [0] + list(best_tour) + [0]

print(f"Tour: {final_tour}")
print(f"Total travel cost: {min_distance}")