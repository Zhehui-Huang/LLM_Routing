# City coordinates with index representing city number
city_coordinates = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Groups of cities
city_groups = {
    0: [5, 6, 16],
    1: [8, 18, 19],
    2: [11, 12, 13],
    3: [1, 3, 9],
    4: [2, 4, 14],
    5: [10, 17],
    6: [7, 15]
}

def euclidean_distance(city1, city2):
    """ Compute the Euclidean distance between two cities. """
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

import itertools

# Calculate all possible tours that visit exactly one city from each group plus the depot at both start and end
all_possible_tours = [[0] + list(tour) + [0] for tour in itertools.product(*[city_groups[i] for i in sorted(city_namunity_groups)])]

# Calculate distances between each pair of cities
distances = {}
for i in city_coordinates:
    for j in city_coordinates:
        distances[(i, j)] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# Find the shortest tour
best_tour = None
min_cost = float('inf')

for tour in all_possible_tours:
    cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    if cost < min_cost:
        min_cost = cost
        best_tour = tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)