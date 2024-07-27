import math
import networkx as nx

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a complete graph from given city coordinates
def create_complete_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

# Create a bottleneck-optimal biconnected subgraph using a basic greedy approach
def algorithm_BB(G):
    sorted_edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    G_BB = nx.Graph()
    G_BB.add_nodes_from(G.nodes())
    for edge in sorted_edges:
        G_BB.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(G_BB):
            break
    return G_BB

# Solve the bottleneck traveling salesman problem
def solve_BTSP(cities):
    G = create_complete_graph(cities)
    G_BB = algorithm_BB(G)
    # Finding a tour in the biconnected subgraph coming from the bottleneck
    tour = list(nx.approximation.traveling_salesman_problem(G_BB, cycle=True, weight='weight'))
    tour.append(tour[0])  # To make the tour complete by returning to the start
    
    # Calculate the total cost and maximum segment cost in the tour
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = G.get_edge_data(tour[i], tour[i + 1])['weight']
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    return tour, total_cost, max_distance

# Coordinates of the cities including the depot
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Execute the solution function and print the results
tour, total_cost, max_distance = solve_BTSP(cities)
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)