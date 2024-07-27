import math
import networkx as nx

# Coordinates of cities indexed from the depot (0) to city (14)
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(a, b):
    """ Calculate Euclidean distance between two points """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Compute the graph with nodes and weighted edges based on the Euclidean distance
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Construct Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices with odd degree in the MST
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# Create the subgraph from G involving only the odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)

# Calculate Minimum Weight Perfect Matching (MWPM) on the subgraph
mwpm = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Add MWPM edges to MST to make it Eulerian
for edge in mwpm:
    mst.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]['weight'])

# Create an Eulerian circuit from the MST+MWPM graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path (visit each city once)
hamiltonian_path = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_path.append(u)
        visited.add(u)
hamiltonian_path.append(0)  # Return to depot city

# Compute the total cost of the Hamiltonian path
total_cost = sum(G[hamiltonian_path[i]][hamiltonian_path[i+1]]['weight'] for i in range(len(hamiltonian_path) - 1))

print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_cost:.2f}")