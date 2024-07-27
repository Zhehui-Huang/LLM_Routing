import networkx as nx
import math
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

# Coordinates of the cities
positions = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a graph with edges between all city pairs and their corresponding distances
G = nx.complete_graph(len(positions))
for i, j in combinations(positions, 2):
    G[i][j]['weight'] = distance(positions[i], positions[j])

# Step 3: Create Minimum Spanning Tree
MST = nx.minimum_spanning_tree(G)

# Step 4: Identify vertices with odd degree in MST
odd_degree_nodes = [v for v in MST.nodes if MST.degree(v) % 2 == 1]

# Step 5: Minimum Cost Perfect Matching on the induced subgraph by odd_degree_nodes
odd_graph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add edges of min_weight_matching to the MST to make it Eulerian
MST.add_edges_from(min_weight_matching)

# Step 6: Find Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Step 7: Convert to Hamiltonian circuit by skipping repeated nodes
visited = set()
hamiltonian_circuit = [0]

for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
    if len(visited) == len(positions) - 1:
        break

hamiltonian_circuit.append(0)  # return to the depot

# Step 8: Calculate the tour cost
tour_cost = 0
for i in range(len(hamiltonian_circuit) - 1):
    tour_cost += distance(positions[hamiltonian_circuit[i]], positions[hamiltonian_circuit[i+1]])

# Output the results
print("Tour:", hamiltonian_circuit)
print("Total travel cost:", tour_cost)