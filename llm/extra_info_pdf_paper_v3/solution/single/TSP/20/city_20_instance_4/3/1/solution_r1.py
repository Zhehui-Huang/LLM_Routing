import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
import networkx as nx

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Calculating the distance matrix
def euclidean_distance(cities):
    coords = np.array(list(cities.values()))
    return squareform(pdist(coords, metric='euclidean'))

distance_matrix = euclidean_distance(cities)

# Create the minimum spanning tree (MST)
mst = minimum_spanning_tree(csr_matrix(distance_matrix))
mst = mst.toarray().astype(float)
mst[mst == 0] = np.inf

# Construct the graph from MST
G = nx.Graph()
for i in range(len(mst)):
    for j in range(len(mst)):
        if mst[i, j] < np.inf:
            G.add_edge(i, j, weight=mst[i, j])

# Find vertices of odd degree in the MST
odd_degree_nodes = [v for v, d in G.degree() if d % 2 == 1]

# Matching on subgraph induced by odd degree vertices
subgraph = G.subgraph(odd_degree_nodes)
min_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Adding minimum matching to the MST
G.add_edges_from(min_matching)

# Make sure it's Eulerian (should be already from construction)
assert nx.is_eulerian(G)

# Find the Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(G))

# Forming the Hamiltonian circuit by skipping repeated nodes
# Start and end at the depot city 0
visited = set()
path = []
for u, v in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
    if v not in visited:
        path.append(v)
        visited.add(v)
        
# Ensuring to start at node 0 and close the tour
if path[0] != 0:
    start_index = path.index(0)
    path = path[start_index:] + path[:start_index]

path.append(0)  # Closing the tour back at the depot

# Calculating the total distance of the tour
total_distance = 0
for i in range(1, len(path)):
    total_distance += distance_matrix[path[i-1], path[i]]

print("Tour:", path)
print("Total travel cost:", total_distance)