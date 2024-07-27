import numpy as np
import networkx as nx
from scipy.spatial import distance

# Define cities
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Create a complete graph with distances
def create_complete_graph(cities):
    G = nx.Graph()
    for i, coord1 in enumerate(cities):
        for j, coord2 in enumerate(cities):
            if i != j:
                G.add_edge(i, j, weight=distance.euclidean(coord1, coord2))
    return G

graph = create_complete_graph(cities)

# Minimum Spanning Tree
mst = nx.minimum_spanning_tree(graph)

# Find odd degree nodes
odd_degree_nodes = [n for n in mst.nodes() if mst.degree(n) % 2 == 1]

# Build subgraph
subgraph = graph.subgraph(odd_degree_nodes)

# Find minimum weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add matching to the MST
mst.add_edges_from(matching)

# Find an Eulerian tour
eulerian_tour = list(nx.eulerian_circuit(mst, source=0))

# Convert Euler tour to Hamiltonian circuit
seen = set()
hamiltonian_tour = [0]
for u, v in eulerian_tour:
    if not v in seen:
        hamiltonian_tour.append(v)
        seen.add(v)
    else:
        continue
hamiltonian_tour.append(0)

# Calculate total travel cost
total_travel_cost = sum(graph[u][v]['weight'] for u, v in zip(hamiltonian_tour[:-1], hamiltonian_tour[1:]))

# Output the result
print("Tour:", hamiltonian_tour)
print("Total travel cost:", total_travel &cost)