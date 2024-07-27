import math
import networkx as nx
from networkx.algorithms import matching, approximation

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Define city coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2), 
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), 
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Step 1: Create a complete graph G
n = len(cities)
G = nx.Graph()
for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 2: Compute a minimum spanning tree (MST) T of G
T = nx.minimum_spanning_tree(G)

# Step 3: Identify vertices with odd degree in T
odd_degree_nodes = [node for node, degree in T.degree() if degree % 2 == 1]

# Step 4: Minimum-weight perfect matching M in the subgraph induced by odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 5: Combine edges of T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 6: Find an Eulerian circuit in H
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 7: Convert Eulerian circuit to Hamiltonian circuit by skipping repeated nodes
path = []
visited = set()
for u, v in eulerian_circuit:
    if not visited or u not in visited:
        path.append(u)
        visited.add(u)
path.append(path[0])  # Closing the tour back to the depot

# Calculate the total travel cost of the tour
total_travel_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

print(f"Tour: {path}")
print(f"Total travel cost: {total_travel_cost:.2f}")