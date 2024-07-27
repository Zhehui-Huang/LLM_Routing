from math import sqrt
import networkx as nx

# Euclidean distance function
def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define the cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Create a complete graph G
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Compute a minimum spanning tree (MST) of G
MST = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in MST
odd_degree_nodes = [node for node, degree in MST.degree() if degree % 2 == 1]

# Create subgraph of G induced by odd degree nodes
odd_graph = G.subgraph(odd_degree_nodes)
# Find a minimum weight perfect matching (MWPM) in the subgraph
MWPM = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add the edges of the MWPM to the MST
MST.add_edges_from(MWPM)

# Find an Eulerian circuit in the MST modified with added MWPM
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Convert the Eulerian circuit to a Hamiltonian circuit (simple path)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        visited.add(u)
        hamiltonian_circuit.append(u)

# Ensure route starts and ends at the depot
if hamiltonian_circuit[0] != 0:
    hamiltonian_circuit.insert(0, 0)
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculate the total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))

# Display the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)