import math
import itertools
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
from networkx import Graph, is_eulerian, eulerian_circuit, odd_degree_nodes, minimum_weight_full_matching

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates indexed by city number
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

num_cities = len(cities)

# Calculate all pairwise city distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)]
             for i in range(num_cities)]

# Convert distances to a CSR (Compressed Sparse Row) matrix for MST calculation
csr_dist_mat = csr_matrix(distances)

# Compute the minimum spanning tree (MST)
mst = minimum_spanning_tree(csr_dist_mat).toarray()

# Create the graph of MST
mst_graph = Graph()
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        if mst[i][j] > 0:
            mst_graph.add_edge(i, j, weight=mst[i][j])

# Find the nodes of odd degree to perform minimum-cost perfect matching
odd_degree_nodes_list = list(odd_degree_nodes(mst_graph))

# Identify subgraph induced on the odd degree vertices
subgraph = Graph(mst_graph.subgraph(odd_degree_nodes_list))

# Find minimum-cost perfect matching in the subgraph
matching = minimum_weight_full_matching(subgraph, weight='weight')
mst_graph.add_edges_from(matching.items())

# Verify if the new graph is Eulerian
assert is_eulerian(mst_graph)

# Generate an Eulerian circuit
circuit = list(eulerian_circuit(mst_graph))

# Convert the Eulerian circuit to a Hamiltonian cycle (visit each city once)
visited = set()
hamiltonian_cycle = [0]
total_cost = 0
last_city = 0
for u, v in circuit:
    if v not in visited:
        hamiltonian_cycle.append(v)
        total_cost += distances[last_city][v]
        last_city = v
        visited.add(v)

# Complete the tour by returning to the start city
total_cost += distances[last_city][0]
hamiltonian_cycle.append(0)

print(f"Tour: {hamiltonian_cycle}")
print(f"Total travel cost: {total_cost}")