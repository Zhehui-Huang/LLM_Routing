import math
import networkx as nx

# Euclidean distance calculation function
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cities coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Building the graph
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            dist = euclidean_distance(cities[i], cities[j])
            G.add_edge(i, j, weight=dist)

# Minimum Spanning Tree (MST) using Kruskal's algorithm
mst_tree = nx.minimum_spanning_tree(G)

# Finding the odd degree vertices in MST
odd_degree_nodes = [node for node in mst_tree.nodes() if mst_tree.degree(node) % 2 != 0]

# Inducing a subgraph on the odd degree vertices in the MST
odd_degree_subgraph = G.subgraph(odd_degree_nodes)

# Minimum Cost Perfect Matching in the induced subgraph
matching = nx.algorithms.min_weight_matching(odd_degree_subgraph, maxcardinality=True, weight='weight')

# Adding the matching edges to the MST to make it Eulerian
mst_tree.add_edges_from(matching)

# Starting from a tour using the Eulerian circuit
eulerian_tour = list(nx.eulerian_circuit(mst_tree, source=0))

# Making the tour Hamiltonian by skipping visited nodes (shortcutting)
current_city = 0
visited = [False]*len(cities)
tour = [current_city]
visited[current_city] = True
total_cost = 0

for edge in eulerian_tour:
    if not visited[edge[1]]:
        tour.append(edge[1])
        total_cost += G[edge[0]][edge[1]]['weight']
        visited[edge[1]] = True
    current_city = edge[1]

# Adding the return to the starting city (Depot)
tour.append(0)
total_cost += G[current_city][0]['weight']

# Printing the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")