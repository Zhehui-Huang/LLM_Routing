import math
import networkx as nx
from itertools import combinations

# Defined cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initialize a complete graph
G = nx.complete_graph(len(cities))

# Setting weights (distances) for the edges in the graph
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = calcByDistance(u, v)

# Finding a Minimum Spanning Tree (MST)
MST = nx.minimum_spanning_tree(G)

# Finding vertices with odd degree in the MST
odd_degree_vertices = [v for v in MST.nodes() if MST.degree(v) % 2 == 1]

# Create a Minimum Weight Perfect Matching (MWPM) among the odd degree vertices in the original graph
subgraph = G.subgraph(odd_degree_vertices)
MWPM = nx.algorithms.min_weight_matching(subgraph, maxcardinality=True)

# Add edges from MWPM to MST to generate a multigraph
for edge in MWPM:
        MST.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]]['weight'])

# Eulerian circuit in the multigraph
eulerian_circuit = list(nx.eulerian_circuit(MST, source=0))

# Convert Eulerian circuit to Hamiltonian path by short-circuiting visited nodes
path = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
# Return to the start to complete the cycle
path.append(path[0])

# Calculate the total distance of the Hamiltonian cycle
total_cost = sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

# Outputting the result
print(f"Tour: {path}")
print(f"Total travel cost: {total_cost}")