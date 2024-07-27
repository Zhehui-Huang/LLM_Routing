import math
import networkx as nx

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Coordinates of the cities
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69),
    (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Creating a complete graph
G = nx.Graph()
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Compute the MST of the graph
MST = nx.minimum_spanning_tree(G)

# Find vertices of odd degree in the MST
odd_degree_nodes = [v for v, degree in MST.degree() if degree % 2 == 1]

# Create a subgraph including only nodes of odd degree
subgraph = G.subgraph(odd_degree_nodes)
# Calculate minimum weight matching on the subgraph
odd_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add the edges from the minimum weight matching to the MST
MST.add_edges_from(odd_matching)

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Create a hamiltonian circuit by skipping visited nodes
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
# Append start city to complete the circuit
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate the tour distance
total_distance = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_distance)