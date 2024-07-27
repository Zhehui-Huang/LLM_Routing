import math
from itertools import permutations

# City Coordinates
cities = {
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

# Groups of cities
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Compute all possible routes that choose one city from each group plus the depot
possible_routes = []
for cities_group0 in groups[0]:
    for cities_group1 in groups[1]:
        for cities_group2 in groups[2]:
            possible_routes.append([0, cities_group0, cities_group1, cities_group2, 0])
            
# Determine the shortest route based on total travel cost
min_cost = float('inf')
best_tour = None

for route in possible_routes:
    current_cost = 0
    for i in range(len(route) - 1):
        current_cost += euclidean_distance(route[i], route[i+1])
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = route

print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")