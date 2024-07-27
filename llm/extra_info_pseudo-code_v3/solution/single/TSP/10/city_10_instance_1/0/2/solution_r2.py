import math
import networkx as nx
from networkx.algorithms.approximation import min_weight_matching
from networkx.algorithms import minimum_spanning_edges
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
G = nx.complete_graph(len(coordinates))
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        G[i][j]['weight'] = euclidean_distance(coordinates[i], coordinates[j])

# Step 1: Minimum spanning tree T
T = nx.Graph(list(minimum_spanning_edges(G, data=False)))

# Step 2: Find vertices with odd degree in T
O = [v for v in T.nodes() if T.degree(v) % 2 != 0]

# Step 3: Minimum-weight perfect matching M on vertices in O
subgraph = G.subgraph(O)
M = min_weight_matching(subgraph, maxcardinality=True)

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
path.append(0)  # Complete the tour by returning to the depot city

# Calculate the total cost of the tour
total_cost = sum(G[path[i]][path[i+1]]['weight'] for i in range(len(path) - 1))

# Output the tour and total cost
output_tour = f"Tour: {path}"
output_cost = f"Total travel cost: {total_cost:.2f}"
print(output_tour)
print(output_cost)