import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

# City coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate the distances (Euclidean)
def euclidean_distances(coords):
    return distance_matrix(coords, coords)

distances = euclidean_distances(cities)

# Creating a graph from the distance matrix
def create_graph(distances):
    G = nx.Graph()
    n = len(distances)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=distances[i][j])
    return G

G = create_graph(distances)

# Utilize MST to find spanning tree, use Prim's Algorithm (implemented in NetworkX)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Construct double tree tour: First double the edges in MST
def double_tree_tour(mst, start_node=0):
    # Create an Eulerian circuit by doubling edges (implicitly done by visiting each node twice)
    eulerian_circuit = list(nx.eulerian_circuit(nx.MultiGraph(mst), source=start_node))
    visited = set()
    path = [start_node]  # start at the depot
    visited.add(start_node)
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(start_node)  # return to the depot
    return path

tour = double_tree_tour(mst)

# Calculate the tour cost
def calculate_cost(tour, distances):
    cost = 0
    for i in range(1, len(tour)):
        cost += distances[tour[i-1]][tour[i]]
    return cost

total_cost = calculate_cost(tour, distances)

# Printing results explicitly
print("Tour:", tour)
print("Total travel cost:", total_cost)