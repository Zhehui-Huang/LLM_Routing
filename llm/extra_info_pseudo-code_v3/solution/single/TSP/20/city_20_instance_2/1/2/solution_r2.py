import math
import networkx as nx

# Coordinates of the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

# Constructing the complete graph
G = nx.Graph()
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            G.add_edge(i, j, weight=calculate_distance(cities[i], cities[j]))

# Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Finding vertices with odd degree
odd_vertices = [v for v in mst.nodes if mst.degree(v) % 2 == 1]

# Minimum weight perfect matching among vertices with odd degree
odd_graph = G.subgraph(odd_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Create multigraph with edges from MST and matching
H = nx.MultiGraph(mst)
H.add_edges_from(min_weight_matching)

# Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(H))

# Convert Eulerian to Hamiltonian circuit, avoiding repeated visits
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Since it's a cycle, starting point should be the same as ending point
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the total cost of the Hamiltonian circuit
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)