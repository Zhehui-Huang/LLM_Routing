import math
import itertools
import networkx as nx

# Define the cities and their coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68),
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Creating a complete graph
G = nx.complete_graph(len(coordinates))

# Adding distance as weights to the edges
for (u, v) in G.edges():
    G.edges[u, v]['weight'] = euclidean_distance(u, v)

# Function to check if the graph is biconnected
def is_biconnected(G):
    return nx.is_biconnected(G)

# Algorithm BB: Obtain the bottleneck-optimal biconnected subgraph
def algorithm_BB(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
    E_BB = nx.Graph()
    E_BB.add_nodes_from(G.nodes())

    for u, v, data in sorted_edges:
        E_BB.add_edge(u, v, weight=data['weight'])
        if is_biconnected(E_BB):
            return E_BB

    return None

# Step 1: Apply Algorithm BB
G_bb = algorithm_BB(G)

# Step 2: Find Hamiltonian cycle in the square of the biconnected subgraph
def find_tour_in_squared_graph(G):
    # Create the square of the graph G_bb
    G_sq = nx.Graph()
    G_sq.add_nodes_loaded(G)

    for u in G.nodes():
        neighbors = list(G[u])
        for i, v in enumerate(neighbors):
            for w in neighbors[i+1:]:
                if v != w:
                    G_sq.add_edge(v, w, weight=max(G.edges[u, v]['weight'], G.edges[u, w]['weight']))
    
    # Find approximate Hamiltonian cycle using a known TSP solver or heuristic
    # Here, we simply use the nearest neighbor heuristic for demonstration:
    current_node = 0
    visited = [False] * len(G_sq.nodes)
    tour = [current_node]
    visited[current_node] = True

    for _ in range(len(G_sq.nodes) - 1):
        next_node = min((n for n in G_sq.neighbors(current_node) if not visited[n]),
                        key=lambda n: G_sq.edges[current_node, n]['weight'])
        visited[next_node] = True
        tour.append(next_node)
        current_node = next_wo

    tour.append(0)  # return to the depot

    return tour

tour = find_tour_in_squared_graph(G_bb)

# Calculate total travel cost and maximum distance
total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)