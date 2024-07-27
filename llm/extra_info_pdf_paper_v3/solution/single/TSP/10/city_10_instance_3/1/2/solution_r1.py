import math
import networkx as nx

# Cities and their coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(c1, c2):
    """ Calculate the Euclidean distance between two points """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# 1. Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# 2. Find vertices with odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes if mst.degree(v) % 2 != 0]

# 3. Minimum weight perfect matching for odd degree nodes in the MST
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add the matching edges to the MST
mst.add_edges_from(min_weight_matching)

# 4. Form an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# 5. Convert this to a Hamiltonian path (shortcutting visited nodes)
visited = set()
hamiltonian_circuit = []
total_cost = 0
last_visited = None

for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
        if last_visited is not None:
            total_cost += euclidean_distance(cities[last_visited], cities[u])
        last_visited = u

# Close the circuit
hamiltonian_circuit.append(hamiltonian_circuit[0])
total_cost += euclidean_distance(cities[last_visited], cities[hamiltonian_circuit[0]])

# Print results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)