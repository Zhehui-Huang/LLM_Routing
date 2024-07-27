import numpy as np

# Coordinates of the cities
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

# Number of cities
n = len(cities)

# Euclidean distance function
def distance(i, j):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Distance matrix construction
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i, j] = distance(i, j)
        else:
            dist_matrix[i, j] = float('inf') # No loops

# Simple Nearest Neighbor algorithm to generate a plausible tour starting and ending at the depot
def nearest_neighbor_tour(start=0):
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current_city = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start) # Return to depot
    return tour

# Compute the tour using nearest neighbor heuristic
tour = nearest_neighbor_tour()

# Calculate the total distance of the tour and find the maximum distance between consecutive cities
total_distance = 0
max_distance = 0
for i in range(len(tour) - 1):
    dist = distance(tour[i], tour[i + 1])
    total_distance += dist
    if dist > max_distance:
        max_distance = dist

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)