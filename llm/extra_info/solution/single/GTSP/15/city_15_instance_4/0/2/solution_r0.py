import math
from itertools import permutations

# City coordinates
coordinates = [
    (35, 40),  # Depot
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

# City groups
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

def total_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distances[route[i]][route[i+1]]
    return total_cost

# Finding the best route that includes one city from each group
min_cost = float('inf')
best_tour = None

for perm in permutations(range(len(groups))):
    for choices in permutations([0, 1]):
        route = [0]  # Start from depot city 0
        valid = True
        for group_index in perm:
            if len(groups[group_index]) > 1:
                city_index = groups[group_index][choices[group_index]]
            else:
                city_index = groups[group_index][0]
            route.append(city_index)

        route.append(0)  # Return to depot
        cost = total_route_cost(route)
        if cost < min_request:
            min_cost = cost
            best_tour = route

# Output the best tour found and the minimum cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")