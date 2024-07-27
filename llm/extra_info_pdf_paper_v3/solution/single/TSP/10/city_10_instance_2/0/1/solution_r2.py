import math
import networkx as nx

# Define coordinates for cities, including the depot as City 0
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Function to compute Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with cities as nodes
G = nx.Graph()
num_cities = len(cities)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Construct Minimum Spanning Tree (MST)
mst = nx.minimum_spanning_tree(G)

# Find nodes in MST with odd degree to create the Minimum Weight Perfect Matching (MWPM)
odd_degree_nodes = [node for node, degree in mst.degree() if degree % 2 == 1]
subgraph_odd = G.subgraph(odd_degree_nodes)
min_weight_matching = nx.algorithms.max_weight_matching(subgraph_odd, maxcardinality=True, weight='weight')

# Add edges from MWPM to MST to make it Eulerian
for edge in min_weight_matching:
    mst.add_edge(*edge, weight=G[edge[0]][edge[1]]['weight'])

# Compute the Eulerian circuit in the augmented graph
eulerian_path = list(nx.eulerian_circuit(mst, source=0))

# Convert the Eulerian circuit to a Hamiltonian path (TSP solution)
visited = set()
tsp_path = [0]
for u, v in eulerian_path:
    if v not in visited:
        tsp_path.append(v)
        visited.add(v)
tsp_path.append(0)  # Return to depot

# Calculate total distance of the TSP path
total_cost = sum(G[tsp_path[i]][tsp_path[i+1]]['weight'] for i in range(len(tsp_path) - 1))

# Display the Tour and Total Travel Cost
print("Tour:", tsp_path)
print("Total travel cost:", round(total_cost, 2))