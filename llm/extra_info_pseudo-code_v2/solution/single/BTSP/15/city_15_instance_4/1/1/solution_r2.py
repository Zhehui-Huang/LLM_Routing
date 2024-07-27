import math
import networkx as nx

# Data setup: Coordinates for each of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to calculate Euclidean distance between two points
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete weighted graph from given city coordinates
def create_complete_graph(coords):
    G = nx.Graph()
    number_of_cities = len(coords)
    for i in range(number_of_cities):
        for j in range(i + 1, number_of_cities):
            distance = calc_distance(coords[i], coords[j])
            G.add_edge(i, j, weight=distance)
    return G

# Gauging if the subgraph formed is biconnected
def is_biconnected(graph):
    return nx.is_biconnected(graph)

# To form a bottleneck biconnected subgraph using sorted edges
def find_biconnected_subgraph(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    B = nx.Graph()
    B.add_nodes_from(G.nodes())
    for u, v, data in sorted_edges:
        B.add_edge(u, v, weight=data['weight'])
        if is_biconnected(B):
            return B
    return B # In case full graph needed but not biconnected

# Solve the Bottleneck Traveling Salesman Problem (BTSP)
def solve_btsp(cities_graph):
    B_subgraph = find_biconnected_subgraph(cities_graph)
    path = list(nx.approximation.traveling_salesman_problem(B_subgraph, cycle=True))
    
    # Ensuring the path starts and ends at the depot city
    if path[0] != 0:
        # Find the index of the start city and perform rotation
        start_index = path.index(0)
        path = path[start_index:] + path[:startindex]
    path.append(path[0])  # Completing the cycle

    # Calculate total distance and maximum leg distance
    total_dist = 0
    max_leg_dist = 0
    for i in range(len(path) - 1):
        dist = cities_graph[path[i]][path[i+1]]['weight']
        total_dist += dist
        if dist > max_leg_dist:
            max_leg_dist = dist

    return path, total_dist, max_leg_dist

# Main execution
G = create_complete_graph(cities)
tour, total_cost, max_distance = solve_btsp(G)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)