import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

# Define coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Graph edges (distance matrix)
num_cities = len(cities)
dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create a minimum spanning tree
mst = minimum_spanning_tree(csr_matrix(dist_matrix))

# Convert MST to a graph format to traverse
graph = {i: set() for i in range(num_cities)}
for i in range(num_cities):
    for j in range(num_cities):
        if mst[i, j] > 0:
            graph[i].add(j)
            graph[j].add(i)

# Find an Euler tour
def find_euler_tour(u, graph):
    tour = []
    stack = [u]
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            stack.append(v)
        else:
            tour.append(u)
            stack.pop()
    return tour[::-1]

euler_tour = find_euler_tour(0, graph)

# Convert the Euler tour to a valid TSP solution by skipping repeated nodes (shortcutting)
visited = set()
final_tour = []
for city in euler_tour:
    if city not in visited or city == 0:
        final_tour.append(city)
        visited.add(city)
final_tour.append(0)  # Return to the depot city

# Calculate the total travel cost of the tour
total_cost = sum(dist_matrix[final_tour[i]][final_tour[i+1]] for i in range(len(final_tour) - 1))

# Output the tour and the total travel cost
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")