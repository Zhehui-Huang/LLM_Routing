import math
import itertools

# Define cities
cities = [
    (53, 68),  # depot city 0
    (75, 11),  # city 1
    (91, 95),  # city 2
    (22, 80),  # city 3
    (18, 63),  # city 4
    (54, 91),  # city 5
    (70, 14),  # city 6
    (97, 44),  # city 7
    (17, 69),  # city 8
    (95, 89)   # city 9
]

# Function for calculating Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate the distance matrix
n = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Utilizing a simplified approximation: Minimum Spanning Tree (MST) + nearest neighbor
from scipy.sparse.csgraph import minimum_spanning_tree

# Create the MST
mst = minimum_spanning_tree(distances).toarray()

# Use a DFS to create an approximate Hamiltonian path from the MST
def dfs(mst, start):
    visited = set()
    stack = [start]
    path = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            stack.extend(reversed([i for i in range(n) if mst[node][i] > 0 and i not in visited]))
    return path

# Create a tour based on MST
tour = dfs(mst, 0)
tour.append(0)  # Return to the starting city

# Calculate the total travel cost and maximum edge cost in the tour
total_cost = 0
max_distance = 0

for i in range(1, len(tour)):
    distance = distances[tour[i - 1]][tour[i]]
    total_cost += distance
    max_distance = max(max_distance, distance)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")