import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def build_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def get_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    
    for u, v, data in sorted_edges:
        H.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(H):
            return H
        
    raise Exception("Unable to form a biconnected subgraph with given edges")  # Ensure an exception is raised if no biconnected graph found

def find_bottleneck_tour(H, start_node):
    # Create square of the graph
    G_squared = nx.Graph()
    G_squared.add_nodes_from(H.nodes())
    for path in nx.all_pairs_shortest_path(H):
        source = path[0]
        for target, p in path[1].items():
            if len(p) == 2 and source != target:  # Direct neighbors
                G_squared.add_edge(source, target, weight=H[source][target]['weight'])
    
    # Find Hamiltonian cycle in G_squared starting from start_node
    cycle = list(nx.approximation.traveling_salesman_problem(G_squared, weight='weight', cycle=True))
    cycle.append(cycle[0])  # Make it a cycle back to start
    
    return cycle

def calculate_costs(cycle, G):
    total_distance = 0
    max_distance = 0
    for i in range(len(cycle) - 1):
        dist = G[cycle[i]][cycle[i+1]]['weight']
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

# City coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Start the solution
G = build_graph(cities)
H = get_biconnected_subgraph(G)
tour = find_bottleneck_tour(H, 0)
total_cost, max_edge_cost = calculate_costs(tour, G)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_edge_cost, 2))