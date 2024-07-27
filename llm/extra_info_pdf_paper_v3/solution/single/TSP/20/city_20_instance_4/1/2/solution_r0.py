import math
from scipy.spatial.distance import pdist, squareform
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Define coordinates of the cities including the depot
coordinates = [(26,60), (73,84), (89,36), (15,0), (11,10), (69,22), 
               (28,11), (70,2), (47,50), (60,29), (29,26), (85,68),
               (60,1), (71,73), (82,47), (19,25), (75,9), (52,54), 
               (64,72), (14,89)]

# Calculate the Euclidean distances between all pairs of cities
dist_matrix = squareform(pdist(coordinates))

# Convert the distance matrix to a graph
G = nx.from_numpy_array(dist_matrix)

# Compute the minimum spanning tree (MST) of the graph
mst = nx.minimum_spanning_tree(G)

# Find all vertices with odd degree in MST
odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 != 0]

# Subgraph of G induced by the odd degree vertices from the MST
subgraph = G.subgraph(odd_degree_nodes)

# Get the minimum cost perfect matching for the subgraph
min_cost_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Combine the edges of the MST and min_cost_matching to get a multigraph
multi_graph = nx.MultiGraph()
multi_graph.add_edges_from(mst.edges())
multi_graph.add_edges_from(min_cost_matching)

# Compute the Eulerian circuit from the constructed multigraph
eulerian_circuit = list(nx.eulerian_circuit(multi_graph, source=0))

# Convert Eulerian circuit to Hamiltonian path, visiting each vertex only once
visited = set()
hamiltonian_circuit = [0]
for u, v in eulerian_circuit:
    if v not in visited:
        visited.add(v)
        hamiltonian_circuit.append(v)
hamiltonian_circuit.append(0)  # Return to the depot

# Calculate the total cost of the Hamiltonian circuit
total_cost = sum(dist_matrix[hamiltonian_circuit[i]][hamiltonian_circuit[i+1]] for i in range(len(hamiltonian_circuit) - 1))

# Output the tour and the total travel cost
print(f"Tour: {hamiltonian_circuit}")
print(f"Total travel cost: {total_cost}")