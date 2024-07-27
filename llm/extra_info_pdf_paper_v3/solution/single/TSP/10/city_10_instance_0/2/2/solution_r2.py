import math
import numpy as np

# City coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
    4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
    8: (61, 90), 9: (42, 49)
}

# Number of cities
n = len(cities)

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create distance matrix
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            dist_matrix[i][j] = float('inf')

# Implementing nearest neighbor to find a reasonable initial solution for TSP
def nearest_neighbor(start=0):
    current = start
    path = [current]
    cost = 0
    visited = set(path)
    while len(visited) < n:
        next_dist = min((dist_matrix[current][j], j) for j in range(n) if j not in visited)
        next_city = next_dist[1]
        cost += next_dist[0]
        path.append(next_city)
        current = next_city
        visited.add(next_city)
    
    # close the tour
    path.append(start)
    cost += dist_matrix[current][start]
    return path, cost

# Compute the shortest tour and its cost
tour, total_cost = nearest_neighbor()

# Generating output
print("Tour:", tour)
print("Total travel cost:", total_cost)