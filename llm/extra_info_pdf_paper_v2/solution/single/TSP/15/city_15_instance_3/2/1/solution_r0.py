import math
from itertools import permutations

# Coordinates of cities including the depot city
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Function to calculate the Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Matrix to hold distances between each pair of cities
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_sanity(coordinates[i], coordinates[j])
        distance_matrix[i][j] = distance_matrix[j][i] = dist

# Function to calculate the total distance of a tour
def total_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Simple example of a nearest neighbor heuristic to find an initial solution
def nearest_neighbor(start=0):
    unvisited = set(range(1, n))
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # Return to depot
    return tour

# Starting from a naive nearest neighbor solution
initial_tour = nearest_neighbor()
min_tour_cost = total_distance(initial_tour)
best_tour = initial_tour[:]

# Attempt to improve the tour by permuting segments (2-opt like approach)
for _ in range(1000):  # Set a reasonable number of iterations
    for i in range(1, len(best_tour) - 3):
        for j in range(i + 2, len(best_tour) - 1):
            new_tour = best_tour[:]
            new_tour[i:j+1] = reversed(new_tour[i:j+1])  # Reversing a segment
            new_cost = total_distance(new_tour)
            if new_cost < min_tour_cost:
                min_tour_cost = new_cost
                best_tour = new_tour[:]

print("Tour:", best_tour)
print("Total travel cost:", min_tour_cost)