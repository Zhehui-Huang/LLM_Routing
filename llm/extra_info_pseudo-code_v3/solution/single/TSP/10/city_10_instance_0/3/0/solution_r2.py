import math
import networkx as nx
from itertools import combinations
from networkx.algorithms.approximation import min_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# Coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Create a complete graph with given cities and Euclidean distance as weights.
def create_complete_graph(cities):
    G = nx.Graph()
    for (i, coord1), (j, coord2) in combinations(cities.items(), 2):
        dist = math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)
        G.add_edge(i, j, weight=dist)
    return G

# Step 1: Compute the Minimum Spanning Tree (MST) of the graph.
G = create_complete_graph(cities)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in MST
odd_vertices = [v for v, degree in mst.degree() if degree % 2 == 1]

# Step 3: Minimum weight perfect matching among odd degree vertices
subgraph = G.subgraph(odd_vertices)
matching = min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 4: Add matching to the MST
mst.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in the augmented graph
euler_circuit = list(eulerian_circuit(mst, source=0))

# Step 6: Create the Hamiltonian circuit by skipping visited nodes
hamiltonian_circuit = []
visited = set()
for u, _ in euler_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)
hamiltonian_circuit.append(0)  # return to the starting point

# Calculate total travel cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output the results
print('Tour:', hamiltonian_circuit)
print('Total travel cost:', total_cost)