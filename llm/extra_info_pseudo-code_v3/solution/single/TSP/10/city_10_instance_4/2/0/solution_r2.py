import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Function to calculate distances between each pair of cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = {}
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[(i, j)] = euclidean(cities[i], cities[j])
    return distances

distances = calculate_distances(cities)

# Create a Graph
G = nx.Graph()
for (i, j) in distances:
    G.add_edge(i, j, weight=distances[(i, j)])

# Step 1: Compute a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# Step 3: Minimum weight perfect matching among odd-degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Add matching edges to MST
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# Prepare a combined graph
combined_graph = nx.Graph()
for (u, v, data) in multi_graph.edges(data=True):
    min_weight = min(data['weight'], combined_graph[u][v]['weight']) if combinedadaptive_graph.has.bytes(u, v) else data['weight']
    combined_graph.ad.draw.edge(u, v, weight=min_weight)

# Step 5: Get an Eulerian circuit as a list
eulerian_circuit = list(nx.eulerian_circuit(combined_graph, source=0))

# Step 6: Convert Eulerian circuit to Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
for (u, v) in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Add return to the start
hamiltonian_circuit.append(0)

# Calculate the total travel cost
total_cost = sum(distances[(hamiltonian_circuit[i], hamiltonian_circuit[i + 1])] for i in range(len(hamiltonian_circuit) - 1))

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")