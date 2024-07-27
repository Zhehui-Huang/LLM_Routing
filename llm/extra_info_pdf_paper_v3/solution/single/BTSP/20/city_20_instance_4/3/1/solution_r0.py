import math
from itertools import permutations

# Coordinates of the cities
coordinates = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
               (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
               (75, 9), (52, 54), (64, 72), (14, 89)]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the distance matrix
n = len(coordinates)
dist_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Implement the nearest neighbor heuristic for TSP
def nearest_neighbor_tsp(start=0):
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # return to the starting point
    return tour

# Compute the tour using the nearest neighbor heuristic
tour = nearest_neighbor_tsp()

# Calculate total travel cost and the maximum distance between consecutive cities
total_cost = 0
max_distance = 0

for i in range(len(tour) - 1):
    dist = dist_matrix[tour[i]][tour[i+1]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output the tour, total travel cost, and max consecutive distance
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")