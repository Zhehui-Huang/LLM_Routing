import math
import itertools

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Coordinates of each city indexed by city number
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Groups of cities
groups = [
    [3, 6], # Group 0
    [5, 8], # Group 1
    [4, 9], # Group 2
    [1, 7], # Group 3
    [2]     # Group 4
]

# Create an adjacency matrix for the distances between the cities
num_cities = len(coordinates)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(i+1, num_cities):
        dist = euclidean_distance(coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1])
        distance_matrix[i][j] = distance_matrix[j][i] = dist

def shortest_group_tour():
    min_distance = float('inf')
    best_route = None

    # Generate all permutations of choices picking one city from each group
    for choices in itertools.product(*groups):
        # Include the depot as the start and end point
        route = [0] + list(choices) + [0]
        route_distance = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        if route_distance < min_distance:
            min_distance = route_distance
            best_route = route

    return best_route, min_distance

# Finding the best route and its cost
best_route, total_cost = shortest_group_tour()
print(f"Tour: {best_route}")
print(f"Total travel cost: {total_cost}")