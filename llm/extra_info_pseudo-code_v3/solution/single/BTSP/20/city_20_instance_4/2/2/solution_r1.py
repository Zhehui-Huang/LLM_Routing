import math
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree, connected_components
from scipy.sparse import csr_matrix

# Function to calculate Euclidean distance between two points
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define the cities coordinates
cities = [
    (26, 60),
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89)
]

n = len(cities)

# Prepare distance matrix and sorted edges by distance
dist_matrix = np.zeros((n, n))
edges = []

for i in range(n):
    for j in range(i + 1, n):
        dist = calculate_distance(cities[i], cities[j])
        dist_matrix[i][j] = dist
        dist_matrix[j][i] = dist
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

def find_valid_tour(max_weight):
    # Construct graph with edges having weight no greater than max_weight
    adj_matrix = np.zeros((n, n))

    for dist, i, j in edges:
        if dist <= max_dependent_dist:
            adj_matrix[i][j] = 1
            adj_matrix[j][i] = 1

    # Using MST to approximate a solution—minimum spanning tree ensures connectivity and minimization of path
    mst_matrix = minimum_spanning_tree(csr_matrix(adj_matrix))
    num_components, labels = connected_components(csgraph=mst_matrix, directed=False, return_labels=True)

    # Verify if we have exactly one connected component
    if num_components == 1:
        # Calculate the tour by a simple traversal of MST + back to depot
        tour = [0]
        current = 0
        visited = set([0])

        while len(visited) < n:
            for j in range(n):
                if mst_matrix[current, j] > 0 and j not in visited:
                    tour.append(j)
                    visited.add(j)
                    current = j
                    break

        tour.append(0)  # return to depot
        return tour

    return None

# Use binary search on edge weights to find the smallest max weight that allows a closed tour
left, right = 0, max(dist_matrix.flatten())
best_tour = None

while right - left > 1e-5:  # adjusting precision
    mid = (left + right) / 2
    tour = find_valid_tour(mid)
    if tour:
        best_tour = tour
        right = mid
    else:
        left = mid

if best_tour:
    max_dist = max(calculate_distance(cities[best_tour[i]], cities[best_tour[i + 1]]) for i in range(len(best_tour) - 1))
    total_cost = sum(calculate_distance(cities[best_tour[i]], cities[best_tour[i + 1]]) for i in range(len(best_tour) - 1))

    # Output results
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("No valid tour found.")