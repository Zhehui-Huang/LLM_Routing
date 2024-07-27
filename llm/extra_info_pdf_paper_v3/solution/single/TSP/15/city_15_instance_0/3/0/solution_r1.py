import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from itertools import combinations
import matplotlib.pyplot as plt
from networkx.algorithms.matching import max_weight_matching
from networkx.algorithms.euler import eulerian_circuit

# City coordinates
coords = np.array([
    (9, 93),  # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
])

# Calculate the distance matrix
dist_matrix = distance_matrix(coords, coords)

# Create a complete graph with cities as nodes and distances as weights
G = nx.complete_graph(len(coords))
for i, j in combinations(range(len(coords)), 2):
    G[i][j]['weight'] = dist_matrix[i][j]

# Step 1: Construct MST
mst = nx.minimum_spanning_tree(G)

# Step 2: Find nodes of odd degree in the MST
odd_degree_nodes = [n for n, deg in dict(mst.degree()).items() if deg % 2 == 1]

# Subgraph of G induced by the odd degree nodes
subgraph = G.subgraph(odd_degree_nodes)

# Step 3: Find Minimum-Cost Perfect Matching in the induced subgraph
matches = max_weight_matching(subgraph, maxcardinality=True, weight='weight')
new_edges = [(u, v, dist_matrix[u][v]) for u, v in matches]

# Add the new edges to the MST
mst.add_edges_from(new_edges)

# Step 4: Convert the MST to a Hamiltonian Circuit
# Since MST with added edges may not be immediately Hamiltonian (contains cycles), convert it to a Eulerian circuit and make Hamiltonian
eulerian_circuit = list(eulerian_circuit(mst, source=0))
tour = [u for u, v in eulerian_circuit] + [0]  # Add starting point to end for a complete tour

# Convert to a simple tour
seen = set()
simple_tour = [x for x in tour if not (x in seen or seen.add(x))]

# Calculating tour cost
tour_cost = sum(dist_matrix[simple_tour[i]][simple_tour[i + 1]] for i in range(len(simple_tour) - 1))
tour_cost += dist_matrix[simple_tour[-1]][simple_tour[0]]  # Add cost to return to the depot

# Output the tour and the total travel cost
print("Tour:", simple_tour + [simple_tour[0]])
print("Total travel cost:", tour_cost)