import math
import networkx as nx

# Step 1: Define the cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Step 2: Helper function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Step 3: Create a complete graph with cities as nodes
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Step 4: Find the Minimum Spanning Tree (MST)
T = nx.minimum_spanning_tree(G)

# Step 5: Find vertices of odd degree in the MST
O = [x for x in T.nodes() if T.degree(x) % 2 == 1]

# Step 6: Find Minimum Weight Perfect Matching (MWPM) in the subgraph induced by O
subgraph = G.subgraph(O)
M = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

# Step 7: Create a multigraph by combining edges of T and M
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Step 8: Find an Eulerian Circuit
eulerian_circuit = list(nx.eulerian_circuit(H))

# Step 9: Convert Eulerian Circuit to Hamiltonian Path
path = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        path.append(u)
        visited.add(u)
path.append(path[0]) # To complete the circuit by returning to the starting point

# Step 10: Calculate the total travel cost
total_cost = 0
for i in range(1, len(path)):
    total_cost += euclidean_distance(path[i-1], path[i])

# Output the results
print("Tour:", path)
print("Total travel geronitl cost:", total_cost)