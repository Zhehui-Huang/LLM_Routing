import math
import networkx as nx

# Define the coordinates for the cities
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Create a complete graph
G = nx.complete_graph(len(cities))

# Assign weights based on Euclidean distance
for u in range(len(cities)):
    for v in range(len(cities)):
        if u != v:
            dist = math.hypot(cities[u][0] - cities[v][0], cities[u][1] - cities[v][1])
            G[u][v]['weight'] = dist

# Step 1: Find a minimum spanning tree
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Vertices with odd degree
odd_degree_nodes = [v for v in T.nodes() if T.degree(v) % 2 == 1]

# Step 3: Find minimum weight perfect matching for odd degree vertices
M = nx.Graph()
M.add_nodes_from(odd_degree_nodes)
for u in odd_degree_nodes:
    for v in odd_degree_nodes:
        if u != v:
            M.add_edge(u, v, weight=G[u][v]['weight'])

min_weight_matching = nx.algorithms.matching.min_weight_matching(M, maxcardinality=True, weight='weight')

# Step 4: Union of edges in T and min_weight_matching
T.add_edges_from(min_weight_matching)

# Step 5: Create Eulerian circuit
euler_circuit = list(nx.eulerian_circuit(T, source=0))

# Step 6: Convert to Hamiltonian path
visited = set()
hamiltonian_circuit = [0]
for u, v in euler_circuit:
    if v not in visited:
        hamiltonian_circuit.append(v)
        visited.add(v)
hamiltonian_circuit.append(0)

# Compute total travel cost
total_cost = sum(G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit)-1))

# Output:
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)