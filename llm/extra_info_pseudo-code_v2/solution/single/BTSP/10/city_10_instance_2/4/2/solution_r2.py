import math
import networkx as nx

# City coordinates
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

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Creating a complete graph with edge weights as distances
G = nx.Graph()
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Step 1: Algorithm BB (Bottleneck-optimal Biconnected Subgraph)
def Algorithm_BB(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = []
    for edge in sorted_edges:
        E_BB.append(edge)
        if nx.is_biconnected(nx.Graph(E_BB)):
            break
    max_weight = max([edge[2]['weight'] for edge in E_BB])
    return nx.Graph(E_BB), max_weight

G_bb, c_BB = Algorithm_BB(G)

# Step 2: Tour Identification
def identify_approximate_optimal_tour(H):
    # Generate G^2 of the biconnected subgraph
    H_squared = nx.Graph()
    for u in H:
        for v in H:
            if u != v and nx.shortest_path_length(H, u, v) == 2:
                H_squared.add_edge(u, v, weight=max(H[u][z]['weight'], H[z][v]['weight']) for z in nx.common_neighbors(H, u, v))

    # Find Hamiltonian cycle
    tour = nx.approximation.traveling_salesman_problem(H_squared, cycle=True, weight='weight')
    return tour

tour = identify_approximate_optimal_tour(G_bb)

# Calculate metrics
max_distance = max(G[x][y]['weight'] for x, y in zip(tour[:-1], tour[1:]))
total_cost = sum(G[x][y]['weight'] for x, y in zip(tour[:-1], tour[1:]))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)