import math
import networkx as nx
from networkx.algorithms import matching, approximation

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# City coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62),
]

# Step 1: Construct complete graph G with Euclidean distances
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = euclidean_distance(cities[i], cities[j])
        G[j][i]['weight'] = G[i][j]['weight']  # Ensure the graph is undirected

# Step 2: Compute a minimum spanning tree (MST) T of G
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 3: Identify vertices with odd degree in T
odds = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# Step 4: Find a minimum-weight perfect matching M in the subgraph induced by odd-degree vertices
min_matching_subgraph = G.subgraph(odds)
min_weight_matching = matching.min_weight_matching(min_matching_subgraph, maxcardinality=True, weight='weight')

# Step 5: Combine edges of MST T and matching M to form multigraph H
H = nx.MultiGraph(mst)
H.add_edges_from(min_weight_matching)

# Step 6: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 7: Convert the Eulerian circuit to a Hamiltonian circuit (skipping repeated vertices)
visited = set()
hamiltonian_circuit = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
# Add the last city back explicitly to close the loop
hamiltonian_circuit.append(hamiltonian_circuit[0])

# Calculate total travel cost
total_cost = 0
for i in range(len(hamiltonian_circuit) - 1):
    total_cost += G[hamiltonian_circuit[i]][hamiltonian_circuit[i + 1]]['weight']

# Output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)