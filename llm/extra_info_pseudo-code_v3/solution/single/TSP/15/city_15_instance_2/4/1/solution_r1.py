import networkx as nx
import numpy as np
from scipy.spatial import distance
from networkx.algorithms import approximation as approx
from networkx.algorithms import euler as euler

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# City coordinates
coords = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Creating a complete graph with weights based on Euclidean distance
G = nx.Graph()
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        distance = euclidean_distance(coords[i], coords[j])
        G.add_edge(i, j, weight=distance)

# Step 1: Find a minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Step 2: Find vertices with odd degree in the MST
vertices_odd_degree = [v for v, d in mst.degree() if d % 2 == 1]

# Step 3: Find minimum-weight perfect matching among the odd degree vertices
odd_subgraph = G.subgraph(vertices_odd_degree)
min_weight_matching = approx.min_weight_matching(odd_subgraph, maxcardinality=True)

# Step 4: Add the matching edges to the MST to get an Eulerian graph
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(min_weight_matching)

# Step 5: Find an Eulerian circuit
eulerian_circuit = list(euler.eulerian_circuit(multi_graph))

# Step 6: Construct Hamiltonian cycle from Eulerian circuit
seen = set()
hamiltonian_path = []
path_cost = 0
last = None

for u, v in eulerian_circuit:
    if u not in seen:
        hamiltonian_path.append(u)
        seen.add(u)
        if last is not None:
            path_cost += euclidean_distance(coords[last], coords[u])
        last = u

# Close the loop to return to the starting point (depot)
hamiltonian_path.append(hamiltonian_path[0])
path_cost += euclidean_distance(coords[hamiltonian_path[-2]], coords[hamiltonian_path[0]])

# Output results
print("Tour:", hamiltonian_path)
print("Total travel cost:", np.round(path_cost, 2))