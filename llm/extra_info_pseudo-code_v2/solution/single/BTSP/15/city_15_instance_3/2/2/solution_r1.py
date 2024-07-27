import math
import networkx as nx

# Coordinates of cities including depot city (city index 0 is the depot)
cities = [
    (16, 90),  # Depot City 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create a complete graph
G = nx.complete_graph(len(cities))
for u, v in G.edges():
    G.edges[u, v]['weight'] = distance(u, v)

# Bundle edges by weight
edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

# Find a biconnected subgraph such that bottleneck is minimized
def find_biconnected_with_min_bottleneck():
    for weight in edges_sorted:
        G_sub = nx.Graph()
        G_sub.add_nodes_from(G.nodes())
        G_sub.add_edge(weight[0], weight[1], weight=weight[2]['weight'])
        # Continue adding edges until biconnection is fulfilled
        for edge in edges_sorted:
            G_sub.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
            if nx.is_biconnected(G_sub):
                max_edge_weight = max((G_sub[u][v]['weight'] for u, v in G_sub.edges()))
                return G_sub, max_edge_weight

# Generate biconnected subgraph
G_bicon, max_bottleneck = find_biconnected_with_min_bottleneck()

# Generate a tour from biconnected subgraph using a heuristic such as the nearest neighbor TSP
def tsp_tour(graph):
    current_node = 0
    path = [current_node]
    total_cost = 0
    visited = set(path)
    
    while len(visited) < len(G.nodes()):
        # selecting the closest unvisited node
        neighbors = sorted((graph[current_node][n]['weight'], n) for n in graph.neighbors(current_node) if n not in visited)
        if not neighbors:   # If there are no unvisited neighbors
            break
        _, next_node = neighbors[0]
        total_cost += graph[current_node][next_node]['weight']
        current_node = next_node
        visited.add(current_node)
        path.append(current_node)
        
    # Returning to the depot
    path.append(0)
    total_cost += graph[current_node][0]['weight']
    max_edge_weight = max(graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
    
    return path, total_cost, max_edge_weight

tour, total_cost, max_consecutive_distance = tsp_tour(G_bicon)

# Correcting the tour formation from our last faulty cycle check
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")