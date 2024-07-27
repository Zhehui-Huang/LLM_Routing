import numpy as np
import networkx as nx

# Coordinates of the cities
cities = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
          (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
          (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
          (60, 63), (93, 15)]

# Function to calculate Euclidean distance between two points
def euclidean_dist(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a complete graph with weights as distances
def create_complete_graph(cities):
    G = nx.complete_graph(len(cities))
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            dist = euclidean_dist(cities[i], cities[j])
            G[i][j]['weight'] = dist
            G[j][i]['weight'] = dist  # Since it's an undirected graph
    return G

# Bottleneck-optimal Biconnected Subgraph (Algorithm BB)
def bottleneck_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    
    # Add edges one by one checking for biconnectivity
    for u, v, data in edges_sorted:
        H.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(H):
            break
    return H

# Hamiltonian cycle in the square of the graph
def find_hamiltonian_cycle(H):
    H2 = nx.power(H, 2)  # Square of the graph
    cycle = nx.approximation.traveling_salesman_problem(H2, cycle=True)
    return cycle

# Compute the TSP metrics
def compute_tsp_metrics(cycle, G):
    total_cost = 0
    max_distance = 0
    for i in range(len(cycle) - 1):
        edge_cost = G[cycle[i]][cycle[i + 1]]['weight']
        total_cost += edge_cost
        if edge_cost > max_distance:
            max_distance = edge_cost
    return total_cost, max_distance

# Implementation of the BTSP 
def solve_btsp(cities):
    G = create_complete_graph(cities)
    H = bottleneck_biconnected_subgraph(G)
    cycle = find_hamiltonian_cycle(H)
    total_cost, max_distance = compute_tsp_metrics(cycle, G)
    cycle.append(cycle[0])  # Complete the cycle
    return cycle, total_cost, max_distance

# Run the BTSP Solver
tour, total_travel_cost, max_distance_between_cities = solve_btsp(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities:.2f}")