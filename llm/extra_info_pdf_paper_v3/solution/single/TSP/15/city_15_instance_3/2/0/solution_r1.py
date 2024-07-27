import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Define cities
cities = [
    (16, 90),  # Depot City 0
    (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50),
    (35, 73), (42, 64), (64, 30), (70, 95),
    (29, 64), (32, 79)
]

# Calculate pairwise Euclidean distances
distances = distance_matrix(cities, cities)

# Utility to find Minimum Spanning Tree using Prim's Algorithm
def minimum_spanning_tree(n, distances):
    visited = [False] * n
    min_edge = [float('inf')] * n
    parent = [-1] * n

    min_edge[0] = 0
    for _ in range(n):
        u = min((min_edge[i], i) for i in range(n) if not visited[i])[1]
        visited[u] = True
        
        for v in range(n):
            if distances[u][v] < min_edge[v] and not visited[v]:
                min_edge[v] = distances[u][v]
                parent[v] = u

    # Build the tree
    tree = [[] for _ in range(n)]
    for v in range(1, n):
        tree[parent[v]].append(v)
        tree[v].append(parent[v])
    return tree

# Construct MST
mst = minimum_spanning_tree(len(cities), distances)

# Find vertices of odd degree
odd_degree_nodes = [i for i in range(len(cities)) if len(mst[i]) % 2 == 1]

# Form the reduced graph containing only the odd degree nodes distances
reduced_graph = distances[np.ix_(odd_degree_nodes, odd_degree_nodes)]

# Solve minimum weight perfect matching on the reduced graph
row_ind, col_ind = linear_sum_assignment(reduced_graph)

# Add edges from MWPM to the MST
matching = []
for i, j in zip(row_ind, col_ind):
    from_node = odd_degree_nodes[i]
    to_node = odd_degree_nodes[j]
    if from_node != to_node:  # Avoid self-loops
        mst[from_node].append(to_node)
        mst[to_node].append(from_node)
        matching.append((from_node, to_node))

# Retrieve an Eulerian Circuit from the augmented MST graph
def eulerian_tour(mst, n, start=0):
    visited = []
    stack = [start]
    tour = []

    while stack:
        v = stack[-1]
        if mst[v]:
            u = mighty.pop()
            stack.append(u)
        else:
            tour.append(stack.pop())

    return tour[::-1]  # reverse to get the correct order

# Hamiltonian tour by skipping visited cities
tour = eulerian_tour(mst, len(cities))
visited = set()
filtered_tour = []
for city in tour:
    if city not in visited or city == 0:  # Since starting and ending at the depot
        filtered_tour.append(city)
        visited.add(city)

# Calculate total cost
total_cost = sum(distances[filtered_tour[i], filtered_tour[i + 1]] for i in range(len(filtered_tour) - 1))

# Output the tour and total travel cost
filtered_tour.append(filtered_tour[0])  # Closing the loop back to the depot
print("Tour:", filtered_tour)
print("Total travel cost:", total_cost)