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

# Step 1: Create a complete graph G
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Step 2: Compute a minimum spanning tree (MST)
MST = nx.minimum_spanning_tree(G)

# Step 3: Identify vertices with odd degree in MST
odd_degree_nodes = [v for v, d in MST.degree() if d % 2 == 1]

# Step 4 + 5: Minimum-weight perfect matching in the induced subgraph on odd_degree_nodes
odd_graph = G.subgraph(odd_subgraph_indices)
min_perfect_matching = nx.algorithms.matching.min_weight_matching(odd_graph, True)

# Add matching edges to MST
MST.add_edges_from(min_perfect_matching)

# Step 6: Find an Eulerian circuit in MST + matching
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Step 7: Convert the Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)

# Ensure starting at the depot city 0 and ending at the depot city 0
hamiltonian_circuit.append(0)

# Calculate total travel cost
total_cost = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit, hamiltonian_circuit[1:]))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)