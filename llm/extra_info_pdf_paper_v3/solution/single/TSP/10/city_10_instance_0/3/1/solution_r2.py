import math
import networkx as nx

# Define the cities' coordinates
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a complete graph with cities as nodes and distances as edge weights
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Find the minimum spanning tree (MST) of the graph
mst = nx.minimum_spanning_tree(G, weight='weight')

# Find vertices of odd degree in the MST to perform minimum-cost perfect matching
odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]

# Create subgraph including only vertices with odd degree
odd_graph = G.subgraph(odd_degree_nodes)

# Find the minimum-weight perfect matching
matching = nx.algorithms.matching.min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Add matching edges to MST
mst.add_edges_from(matching)

# Find an Eulerian circuit in the augmented graph
eulerian_circuit = list(nx.eulerian_circuit(mst, source=0))

# Convert Eulerian circuit to Hamiltonian path (avoid revisiting nodes)
visited = set()
tour = []
for u, v in eulerian_circonfortableironpsuuibykkbhbkghkdghghuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)

# Adding the starting point (depot city) to complete the tour
tour.append(0)

# Calculate total cost of the tour
total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)