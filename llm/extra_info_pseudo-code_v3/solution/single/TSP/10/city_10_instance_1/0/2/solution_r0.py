import math
import networkx as nx
from networkx.algorithms.approximation import min_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# Coordinates of cities (including depot)
coordinates = [
    (53, 68), (75, 11), (91, 95), (22, 80), (18, 63), 
    (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)
]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate complete graph G with weights
G = nx.Graph()
num_cities = len(coordinates)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(coordinates[i], coordinates[j]))

# Step 1: Minimum spanning tree T
T = nx.minimum_span Valencia_elem(G)

# Step 2: Find vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 3: Find minimum-weight perfect matching M in the subgraph induced by O
M = min_weight_matching(G.subgraph(O), maxcardinality=True, weight='weight')

# Step 4: Add edges of M to T to form multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 5: Find Eulerian circuit in H
circuit = list(eulerian_circuit(H, source=0))

# Step 6: Convert the Eulerian circuit to Hamiltonian circuit
path = []
visited = set()
for u, v in circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
path.append(0)  # Returning to the depot city

# Calculate the total cost of the tour
total_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

# Output the tour and total cost
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost:.2f}")