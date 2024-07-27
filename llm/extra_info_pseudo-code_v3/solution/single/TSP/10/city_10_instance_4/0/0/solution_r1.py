import math
import networkx as nx
from itertools import combinations

# Coordinates for each city
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

# Helper function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Constructing the complete graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=calc_distance(cities[i], cities[j]))

# Step 1: Compute a minimum spanning tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 2: Identify the set O of vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 3: Find a minimum weight perfect matching M in the subgraph induced by O
O_subgraph = nx.Graph()
O_subgraph.add_nodes_from(O)
for u, v in combinations(O, 2):
    # Ensure each vertex pair in the odd degree subgraph has a correct distance value
    O_subgraph.add_edge(u, v, weight=calc_distance(cities[u], cities[v]))

M = nx.algorithms.matching.min_weight_matching(O_subgraph, maxcardinality=True)

# Step 4: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
for edge in M:
    H.add_edge(edge[0], edge[1])

# Step 5: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit into a Hamiltonian circuit
visited = set()
hamiltonian_circuit = [0]  # Reinitialize to start from depot

for u, v in eulerian_circuit:
    if v not in visited or v == 0:  # Allowing to return to depot
        visited.add(v)
        hamiltonian_circuit.append(v)

# To ensure the circuit ends at the starting depot
if hamiltonian_circuit[-1] != 0:
    hamiltonian_circuit.append(0)

# Calculating the total travel cost
total_cost = sum(calc_distance(cities[hamiltonian_circuit[i]], cities[hamiltonian_circuit[i + 1]]) for i in range(len(hamiltonian_circuit) - 1))

# Output the tour and the total travel cost
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", total_cost)