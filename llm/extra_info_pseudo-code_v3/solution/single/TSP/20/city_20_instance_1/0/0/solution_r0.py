import numpy as np
from scipy.spatial.distance import euclidean
from networkx import Graph, minimum_spanning_tree, complete_graph, eulerian_circuit
from networkx.algorithms.matching import min_weight_matching

# Define the list of cities and their coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate all distances between the cities
def calculate_distances(cities):
    num_cities = len(cities)
    dist_matrix = {}
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i, j] = euclidean(cities[i], cities[j])
    return dist_matrix

distances = calculate_distances(cities)

# Create a complete graph with the distances
def create_graph(num_cities, distances):
    G = complete_graph(num_cities)
    for (i, j), d in distances.items():
        G[i][j]['weight'] = d
    return G

graph = create_graph(len(cities), distances)

# Step 1: Compute a minimum spanning tree (MST) of the graph
mst = minimum_spanning_tree(graph)

# Step 2: Identify vertices with odd degree in the MST
odd_degree_nodes = [n for n in mst.nodes() if mst.degree(n) % 2 != 0]

# Create subgraph induced by odd degree vertices
odd_graph = graph.subgraph(odd_degree_nodes)

# Step 3: Find a minimum-weight perfect matching in the subgraph
matching = min_weight_matching(odd_graph, weight='weight', maxcardinality=True)

# Step 4: Add the matching edges to the MST
mst.add_edges_from(matching)

# Step 5: Find an Eulerian circuit in the multigraph
euler_circuit = list(eulerian_circuit(mst, source=0))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit by skipping repeated vertices
visited = set()
hamiltonian_circuit = []
for u, v in euler_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)

# Ensure to add the start node at the end to complete the tour
hamiltonian_circuit.append(0)

# Calculate the total travel cost
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_cost += distances[hamiltonian_circuit[i - 1], hamiltonian_circuit[i]]

# Print the output
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)