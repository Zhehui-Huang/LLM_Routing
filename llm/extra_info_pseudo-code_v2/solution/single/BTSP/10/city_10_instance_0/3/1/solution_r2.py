import math
import networkx as nx
from itertools import combinations

# Coordinates of each city
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98),
    (51, 69), (47, 39), (62, 26), (79, 31),
    (61, 90), (42, 49)
]

# Compute Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Initialize graph
G = nx.Graph()

# Adding nodes and weighted edges to the graph
for i, coord1 in enumerate(coordinates):
    for j, coord2 in enumerate(coordinates):
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(coord1, coord2))

# Function to find approximate tour minimizing the maximum edge length
def approximate_minmax_tour(graph):
    # Minimum Spanning Tree (MST)
    mst = nx.minimum_spanning_tree(graph, weight='weight')
    # Double the tree to ensure all degrees are even (Eulerian)
    doubled_mst = nx.MultiGraph(mst)
    doubled_mst.add_edges_from(mst.edges(data=True))
    # Find an Eulerian circuit in the doubled graph
    eulerian_circuit = list(nx.eulerian_circuit(doubled_mst))
    # Convert Eulerian circuit to a valid tour by skipping repeated nodes
    tour = []
    visited = set()
    for u, v in eulerian_circuit:
        if len(visited) == len(graph):
            break
        if u not in visited:
            tour.append(u)
            visited.add(u)
    tour.append(tour[0])  # complete the tour by returning to the start node

    # Calculate metrics
    max_edge_length = max(graph[u][v]['weight'] for u, v in zip(tour, tour[1:]))
    total_cost = sum(graph[u][v]['weight'] for u, v in zip(tour, tour[1:]))
    
    return tour, total_cost, max_edge_length

# Calculate the tour and metrics
tour, total_cost, max_edge_length = approximate_minmax_tour(G)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_edge_length:.2f}")