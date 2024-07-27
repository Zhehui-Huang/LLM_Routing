import numpy as np
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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of cities
num_cities = len(cities)

# Create a complete graph with cities as nodes and distances as edge weights
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=distance(i, j))

# Helper function: Checks if adding an edge forms a cycle
def forms_cycle(edges, n):
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
    for u, v in edges:
        if find(u) == find(v):
            return True
        union(u, v)
    return False

# STEP 1: Bottleneck-optimal Biconnected Subgraph
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
edges_BB = []
for edge in edges_sorted:
    # Try adding edge and check if it introduces a cycle
    if not forms_cycle(edges_BB + [edge[:2]], num_cities):
        edges_BB.append(edge[:2])
    # Check if the graph with these edges is biconnected
    temp_graph = G.edge_subgraph(edges_BB).copy()
    if nx.is_biconnected(temp_graph):
        break

# Graph of the Biconnected Subgraph
G_BB = G.edge_subgraph(edges_BB).copy()

# STEP 2: Tour Identification
# Using the approximation algorithm for TSP on the reduced graph G_BB
tour = nx.approximation.traveling_salesman_problem(G_BB, cycle=True, weight='weight')
tour.append(tour[0])  # ensure the tour is closed (start and end at the same node)

# Calculate the total cost and the maximum distance between consecutive cities
total_cost = sum(G.edges[tour[i], tour[i + 1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(G.edges[tour[i], tour[i + 1]]['weight'] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)