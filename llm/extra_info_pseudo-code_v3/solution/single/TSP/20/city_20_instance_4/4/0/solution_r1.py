import numpy as np
import networkx as nx

# Define the cities coordinates
cities = [
    (26, 60), 
    (73, 84), 
    (89, 36), 
    (15, 0), 
    (11, 10), 
    (69, 22), 
    (28, 11), 
    (70, 2), 
    (47, 50), 
    (60, 29), 
    (29, 26), 
    (85, 68), 
    (60, 1), 
    (71, 73), 
    (82, 47),
    (19, 25), 
    (75, 9),  
    (52, 54),
    (64, 72),
    (14, 89)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Form graph (Complete graph)
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G.edges[i, j]['weight'] = euclidean_distance(cities[i], cities[j])

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Identify set O of vertices with odd degree in T
O = [v for v, d in T.degree() if d % 2 == 1]

# Step 3: Find a minimum-weight perfect matching in the subgraph induced by O
G_odd = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(G_odd, maxcardinality=True, weight='weight')

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 6: Convert the Eulerian circuit to a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]
visited.add(0)
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)

hamiltonian_circuit.append(0)  # complete the tour by returning to the depot

# Calculate the total travel cost
total_travel_cost = sum(G.edges[hamiltonian_circuit[i], hamiltonian_circuit[i+1]]['weight'] for i in range(len(hamiltonian_circuit) - 1))

# Print results
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_travel_cost:.2f}")