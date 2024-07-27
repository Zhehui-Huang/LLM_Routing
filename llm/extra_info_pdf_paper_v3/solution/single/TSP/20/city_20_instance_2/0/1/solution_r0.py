import math
import networkx as nx

# City coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 6: (2, 65),
    7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53), 12: (11, 14), 
    13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58),  
    19: (30, 48)
}

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create a complete graph with cities as nodes and distances as edge weights
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(cities[i], cities[j]))

# Compute the Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find vertices of odd degree in the MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]

# Create subgraph induced by vertices of odd degree
subgraph = G.subgraph(odd_degree_nodes)

# Find Minimum-Cost Perfect Matching (MCPM)
perfect_matching = nx.algorithms.max_weight_matching(subgraph, maxcardinality=True, weight="weight")

# Add edges from MCPM to the MST to form an Eulerian graph
mst.add_edges_from(perfect_matching)

# Form a Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian circuit to a Hamiltonian path
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
        
# Ensure the tour begins and ends at the depot
hamiltonian_circuit.append(0)

# Compute the total travel cost
total_cost = 0
for i in range(1, len(hamiltonian_circuit)):
    total_cost += distance(cities[hamiltonian_circuit[i-1]], cities[hamiltonian_circuit[i]])

# Output the results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost:.2f}")