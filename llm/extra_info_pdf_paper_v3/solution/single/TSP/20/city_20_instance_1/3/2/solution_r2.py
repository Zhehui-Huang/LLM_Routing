import numpy as np
import networkx as nx

# Re-defining cities based on given coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def calc_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_distance_graph(cities):
    """Create a graph from the cities with distances as weights."""
    G = nx.Graph()
    for i, coord1 in cities.items():
        for j, coord2 in cities.items():
            if i != j:
                G.add_edge(i, j, weight=calc_distance(coord1, coord2))
    return G

# Create the complete graph
G = create_distance_graph(cities)

# Compute Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in MST
odd_degree_vertices = [v for v, d in mst.degree() if d % 2 != 0]

# Get subgraph induced by odd-degree vertices
odd_subgraph = nx.Graph(mst.subgraph(odd_degree_vertices))

# Compute min cost perfect matching
min_matching_graph = nx.algorithms.matching.min_weight_matching(odd_subgraph, weight='weight', maxcardinality=True)

# Create the union of MST and the matching
mst.add_edges_from(min_matching_graph)

# Form an Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian circuit into a Hamiltonian path using shortcutting
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)

# Close the cycle
hamiltonian_circuit.append(0)

# Calculate the total cost of the tour
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)