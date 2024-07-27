import numpy as np

# Coordinates of cities, index corresponds to city number
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
    (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
    (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

# Generate distance matrix
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Approximate the solution using a greedy heuristic
def find_tour():
    unvisited = list(range(1, n))
    tour = [0]
    while unvisited:
        last_city = tour[-1]
        # Next city is the one that minimizes the max distance to the last city in the tour
        next_city = min(unvisited, key=lambda x: distance_matrix[last_city][x])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # returning to the depot

    return tour

tour = find_tour()

# Calculate total travel cost and max distance between consecutive cities
total_cost = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = distance_matrix[tour[i]][tour[i+1]]
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)