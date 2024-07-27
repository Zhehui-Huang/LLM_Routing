import math
import sys

# Define city coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Compute distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Find the tour using simplified nearest neighbor heuristic
def find_tour():
    unvisited = set(range(1, n))
    tour = [0]
    current = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(0)  # return to the depot
    return tour

tour = find_tour()

# Calculate total travel cost and max distance
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = distance_matrix[tour[i-1]][tour[i]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")