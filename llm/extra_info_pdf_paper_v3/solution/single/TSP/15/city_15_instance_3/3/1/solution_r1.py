import math
import networkx as nx

# Coordinates of cities indexed from the depot (0) to city (14)
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(a, b):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Initialize a graph
G = nx.Graph()

# Add edges with weights to the graph
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Calculate Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Extract nodes with odd degree to perform Minimum Weight Perfect Matching (MWPM)
odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]

# Induce subgraph of G with the odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)

# Find MWPM by returning the pairs with the shortest paths to pair up all odd degree nodes
mwpm = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Add MWPM edges to the MST
mst.add_edges_from(mwpm)

# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path (visiting each node only once)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)  # Return to the starting city

# Calculate the total cost of the tour
total_cost = sum(euclidean_distance(cities[hamiltonian_circuit[i]], cities[hamiltonian_circuit[i+1]]) 
                 for i in range(len(hamiltonian_circuit) - 1))

print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)