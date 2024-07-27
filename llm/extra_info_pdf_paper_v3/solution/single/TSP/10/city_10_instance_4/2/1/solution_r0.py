import numpy as np
import networkx as nx

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

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create distance matrix
n = len(cities)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Creating a complete graph
G = nx.complete_graph(n, create_using=nx.Graph())

# Assign distances to edges in the graph
for i in range(n):
    for j in range(n):
        if i != j:
            G[i][j]['weight'] = dist_matrix[i][j]

# Finding the Minimum Spanning Tree (MST) of G
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices of odd degree in the MST
odd_vertices = [v for v, d in mst.degree() if d % 2 == 1]

# Create the minimum weight matching M on the subgraph induced by odd-degree vertices
subgraph = G.subgraph(odd_vertices)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the edges of the minimum weight matching to the MST
augmented_graph = nx.MultiGraph(mst)
augmented_graph.add_edges_from(min_weight_matching)

# Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(augmented_graph, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (shortcut method to avoid repeated nodes)
visit_order = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        visit_order.append(u)
        visited.add(u)
visit_order.append(visit_order[0])  # Return to the starting point

# Calculate the total travel cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[visit_order[i]][visit_order[i+1]] for i in range(len(visit_order)-1))

# Outputting the results
print("Tour:", visit_order)
print("Total travel cost:", total_cost)