import math
import networkx as nx

# Define the cities and their coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Step 0: Prepare the graph
G = nx.Graph()
for i in cities.keys():
    for j in cities.keys():
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(i, j))

# Sort edges by weight
sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])

# Step 1: Algorithm BB
def find_biconnected_subgraph(G, sorted_edges):
    # Initialize the solution set
    H = nx.Graph()
    H.add_nodes_from(G.nodes())

    for edge in sorted_edges:
        H.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(H):
            # If H is biconnected, return it
            return H, max(e[2]['weight'] for e in H.edges(data=True))
    return None, None

E_BB, c_BB = find_biconnected_subgraph(G, sorted_edges)

# Step 2: Tour Identification
# Generate square graph G^2
G_sq = nx.power(G, 2)

# Find Hamiltonian Cycle of minimum bottleneck in the square of G
paths = list(nx.approximation.traveling_salesman_problem(G_sq, cycle=True))
bottleneck = max(euclidean_unadjusted(e[0], e[1]) for e in zip(paths[:-1], paths[1:]))

# Calculate distance and maximum distance between consecutive cities
total_cost = sum(euclidean_distance(paths[i], paths[i+1]) for i in range(len(paths)-1))
max_distance = max(euclidean_distance(paths[i], paths[i+1]) for i in range(len(paths)-1))

# Output formatted results
print(f"Tour: {paths}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")