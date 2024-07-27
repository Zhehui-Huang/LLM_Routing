import math
import networkx as nx

def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Define the cities and their positions
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Create a complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Find the minimum spanning tree
mst = nx.minimum_spanning_tree(G)

# Find nodes with odd degree in MST to create a subgraph
odd_degree_nodes = [node for node in mst.nodes if mst.degree(node) % 2 == 1]
subgraph = G.subgraph(odd_degree_nodes)

# Find minimum-cost perfect matching
matching = nx.Graph()
matching.add_edges_from(nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True))

# Adding matching edges to MST to create an Eulerian circuit
mst.add_edges_from(matching.edges())

# Get an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path (remove repeated visits)
visited = set()
hamiltonian_path = []
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
hamiltonian_path.append(0)  # back to the depot

# Calculate the cost of the tour
total_cost = sum(euclidean_distance(hamiltonian_path[i], hamiltonian_path[i + 1]) for i in range(len(hamiltonian_path) - 1))

# Output the results
print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_cost}")