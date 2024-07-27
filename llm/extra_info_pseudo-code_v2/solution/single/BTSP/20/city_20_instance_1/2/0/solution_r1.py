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

# Step 1: Algorithm BB - Create a biconnected subgraph with minimal maximum edge weight
def find_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda e: e[2]['weight'])
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    max_edge_weight = None
    
    for edge in sorted_edges:
        H.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(H):
            max_edge_weight = edge[2]['weight']
            break
        
    return H, max_edge_weight

E_BB, max_edge_weight_BB = find_biconnounced_subgraph(G)

# Create a modified graph to find the Hamiltonian circuit
H = nx.Graph()
H.add_nodes_from(E_BB.nodes())
H.add_edges_from(E_BB.edges())

# Use the nearest neighbor heuristic to find a Hamiltonian circuit
def nearest_neighbor_tour(G, start_node):
    unvisited = set(G.nodes())
    tour = [start_node]
    current = startio
    unvisited.remove(start_node)
    
    while unvisited:
        next_node = min(unvisited, key=lambda node: G.edges[current, node]['weight'])
        tour.append(next_node)
        unvisited.remove(next_node)
        current = next_node
        
    tour.append(start_node)  # return to the start node
    return tour

# Calculating the tour using the modified graph
tour = nearest_neighbor_tour(H, 0)

# Calculate total distance and maximum distance between consecutive cities in the tour
total_travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")