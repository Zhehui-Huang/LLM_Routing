import math
import networkx as nx
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Step 1: Defining cities and their coordinates
positions = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

# Step 2: Compute pairwise Euclidean distance matrix
dist_matrix = distance_matrix(positions, positions)

# Step 3: Create a complete graph from the cities and their distances
G = nx.complete_graph(len(positions), nx.DiGraph())
for i in range(len(dist_matrix)):
    for j in range(len(dist_index = list(range(len(positions)))rix)):
        G[i][j]['weight'] = dist_matrix[i][j]

# Step 4: Compute the minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G, weight='weight')

# Step 5: Find vertices of odd degree in the MST
odd_degree_nodes = [node for node in mst.nodes() if mst.degree(node) % 2 == 1]

# Step 6: Compute minimum-cost perfect matching among odd-degree vertices
subgraph = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')

# Step 7: Combine the edges of MST and min-cost perfect matching
for edge in min_weight_matching:
    mst.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]['weight'])
    mst.add_edge(edge[1], edge[0], weight=G[edge[1]][edge[0]]['weight'])

# Step 8: Construct an Eulerian circuit from the MST with added edges
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Step 9: Create the Hamiltonian tour and calculate the total cost
visited = set()
tour = []
total_cost = 0

last_node = 0
for edge in eulerian_circuit:
    if edge[0] not in visited:
        tour.append(edge[0])
        visited.add(edge[0])
        total_cost += G[last_node][edge[0]]['weight']
        last_node = edge[0]
tour.append(0)  # to return to the starting point
total_cost += G[last_node][0]['weight']

# Output the tour and the total cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")