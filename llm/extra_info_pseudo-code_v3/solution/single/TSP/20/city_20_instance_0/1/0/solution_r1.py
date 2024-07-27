import math
import networkx as nx

# Define the robot's cities with coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Initialize a complete graph
G = nx.Graph()
for u in cities.keys():
    for v in cities.keys():
        if u != v:
            dist = math.sqrt((cities[u][0] - cities[v][0])**2 + (cities[u][1] - cities[v][1])**2)
            G.add_edge(u, v, weight=dist)

# Step 1: Compute a minimum spanning tree of the graph
T = nx.minimum_spanning_tree(G, weight='weight')

# Step 2: Find vertices of odd degree in T
odd_degree_nodes = [node for node in T.nodes() if T.degree(node) % 2 == 1]

# Step 3: Minimum weight perfect matching on the subgraph induced by odd-degree vertices
odd_subgraph = G.subgraph(odd_degree_nodes)
matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a new graph
multi_graph = T.copy()
multi_graph.add_edges_from(matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(multi_graph))

# Step 6: Make the Eulerian circuit into a Hamiltonian circuit (shortcutting)
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

# Make sure to return to the start point
hamiltonian_circuit.append(0)

# Calculate total tour cost
total_cost = 0
for i in range(len(hamiltonian_circuit)-1):
    total_cost += G[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]]['weight']

# Output the tour and total travel cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")