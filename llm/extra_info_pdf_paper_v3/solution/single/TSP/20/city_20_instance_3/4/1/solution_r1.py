import math
import networkx as nx

cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Construct a Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in the MST
odd_degree_vertices = [v for v, degree in mst.degree() if degree % 2 == 1]

# Create induced subgraph with odd degree vertices
odd_graph = G.subgraph(odd_degree_vertices)

# Find Minimum-Cost Perfect Matching in the induced subgraph
perfect_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True)

# Add matching edges to the MST
mst.add_edges_from(perfect_matching)

# Conversion to Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian to Hamiltonian path and calculate cost
visited = set()
hamiltonian_circuit = []
total_cost = 0
last_city = 0
for u, v in eulerian_circuit:
    if u not in visited:
        if len(hamiltonian_circuit) > 0:
            total_cost += euclidean_distance(cities[last_city], cities[u])
        hamiltonian_circuit.append(u)
        visited.add(u)
        last_city = u
    if v not in visited:
        total_cost += euclidean_distance(cities[last_city], cities[v])
        hamiltonian_circuit.append(v)
        visited.add(v)
        last_city = v
hamiltonian_circuit.append(0)  # return to the depot city
total_cost += euclidean for_distance(cities[last_city], cities[0])

print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")