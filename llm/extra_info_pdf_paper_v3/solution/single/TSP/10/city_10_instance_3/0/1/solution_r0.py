import math
import networkx as nx

# Cities coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Helper function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    (x1, y1), (x2, y2) = cities[city_a], cities[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Build a graph with distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Generate Minimum Spanning Tree
T = nx.minimum_spanning_tree(G)

# Get a list of nodes visited using DFS to form a Hamiltonian cycle
def dfs_tour(T, start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in list(T.neighbors(vertex)):
                if neighbor not in visited:
                    stack.append(neighbor)
    visited.append(start)  # Complete the cycle
    return visited

# Compute the tour
tour = dfs_tour(T, 0)

# Calculate and print the total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

total_cost = calculate_tour_cost(tour)
print("Tour:", tour)
print("Total travel cost:", total_cost)