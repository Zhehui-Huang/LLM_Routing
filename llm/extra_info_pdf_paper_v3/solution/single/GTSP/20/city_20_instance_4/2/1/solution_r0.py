import math
import itertools

# Coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Compute distances between all pairs using Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = {}
num_cities = len(coordinates)
for i in range(num_cities):
    for j in range(num_cities):
        distances[(i, j)] = calculate_distance(coordinates[i], coordinates[j])

# For each group, select a representative city to approximate GTSP with TSP
representatives = []

for group in groups:
    best_rep = None
    min_cost = float('inf')
    for city in group:
        cost = 0
        for other_group in groups:
            if group != other_group:
                min_cost_to_group = min(distances[city, other] for other in other_group)
                cost += min_cost_to_group
        if cost < min_cost:
            min_cost = cost
            best_rep = city
    representatives.append(best_rep)

# Include the depot
representatives.insert(0, 0)  # Starting and ending at the depot

# TSP Solver using a simple nearest neighbor heuristic
def tsp_nn_solver(cities):
    path = [cities[0]]
    unvisited = set(cities[1:])
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda city: distances[(last, city)])
        path.append(next_city)
        unvisited.remove(next_city)
    path.append(cities[0])  # Return to the depot
    return path

# Solve TSP with the selected representatives
tour = tsp_nn_solver(representatives)

# Calculate total travel cost of the tour
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)