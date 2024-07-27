import math
from itertools import permutations

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
city_groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Function to calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Precompute the distance matrix
dist_matrix = {}
for i in cities:
    dist_matrix[i] = {}
    for j in cities:
        dist_matrix[i][j] = calc_distance(i, j)

# Generate all permutations of one city from each group
city_choices = []
for group, members in city_groups.items():
    city_choices.append(members)

all_routes = []
for perm in permutations(city_choices):
    all_routes.extend(permutations([item for sublist in perm for item in sublist]))

# Find the minimum cost route
min_cost = float('inf')
best_tour = None

for route in set(all_routes):
    if len(set(route)) == len(route):  # All cities in the route are unique
        cost = dist_matrix[0][route[0]]  # From depot to first city
        for i in range(len(route) - 1):
            cost += dist_matrix[route[i]][route[i + 1]]
        cost += dist_matrix[route[-1]][0]  # From last city back to depot
        if cost < min_cost:
            min_cost = cost
            best_tour = [0] + list(route) + [0]

# Print the results
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))