import math
import networkx as nx

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Compute Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate the complete graph with distances as weights
G = nx.Graph()
for c1 in cities:
    for c2 in cities:
        if c1 != c2:
            weight = euclidean_distance(c1, c2)
            G.add_edge(c1, c2, weight=weight)

# Utilize Minimum Spanning Tree for biconnected subgraph and tour approximation
mst = nx.minimum_spanning_tree(G)
mst_edges = list(mst.edges(data=True))

# Ensuring the graph is biconnected by adding necessary edges
while not nx.is_biconnected(mst):
    additional_edges = [(u, v, G[u][v]['weight']) for u, v in combinations(mst.nodes, 2) if not mst.has_edge(u, v)]
    additional_edges_sorted = sorted(additional_edges, key=lambda x: x[2])
    mst.add_edge(additional_edges_sorted[0][0], additional_edges_sorted[0][1], weight=additional_edges_sorted[0][2])

# Finding the approximate tour using 2-approximation from MST
tour = list(nx.eulerian_circuit(nx.eulerize(mst), source=0))
tour_path = [tour[0][0]]
visited = set(tour_path)
for edge in tour:
    if edge[1] not in visited:
        tour_path.append(edge[1])
        visited.add(edge[1])

# Close the tour back to the origin
tour_path.append(tour_path[0])

# Calculate the total cost and maximum consecutive city distance
total_travel_cost = 0
max_consecutive_distance = 0
for i in range(len(tour_path) - 1):
    distance = G[tour_path[i]][tour_path[i + 1]]['weight']
    total_travel_cost += distance
    max_consecutive_distance = max(max_consecutive_distance, distance)

# Results
print("Tour:", tour_path)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_consecutive distance)