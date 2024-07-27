import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Coordinates of each city indexed by city number
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Groups of cities
groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

# Create an adjacency matrix for the distances between the cities
num_cities = len(coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(
                coordinates[i][0], coordinates[i][1],
                coordinates[j][0], coordinates[j][1]
            )

# We need to consider all permutations of choosing one city from each group, plus the depot city
from itertools import permutations

# Find shortest route that visits one city from each group
def shortest_group_tour():
    depot = 0
    min_distance = float('inf')
    best_route = []

    for group_permutation in permutations(groups):
        # Generate all selections of cities one from each group
        for city_combination in itertools.product(*(group_permutation)):
            # Make sure to start and end at the depot
            route = [depot] + list(city_combination) + [depot]
            # Calculate the route distance
            route_distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

            if route_distance < min_distance:
                min_distance = route_distance
                best_route = route

    return best_route, min_distance

# Find and print the shortest tour and its cost
best_route, total_cost = shortest_group_tour()
print(f"Tour: {best_route}")
print(f"Total travel cost: {total_cost}")