import numpy as np
import networkx as nx
from itertools import permutations

# Coordinates of cities with the first city as the depot
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# Create a full graph with nodes and edges weighted by the Euclidean distance
def create_graph():
    G = nx.complete_graph(len(coordinates))
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            G[i][j]['weight'] = dist
            G[j][i]['weight'] = dist  # Because it's an undirected graph
    return G

# Evaluate if there's a Hamiltonian cycle in the graph
def check_hamiltonian_cycle(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    distances_sorted = [edge[2]['weight'] for edge in edges_sorted]

    for limit_distance in distances_sorted:
        subgraph = nx.Graph([(u, v) for u, v, d in G.edges(data=True) if d['weight'] <= limit_distance])
        for component in nx.connected_components(subgraph):
            if len(component) == len(G.nodes):
                path = list(nx.approximation.traveling_salesman_problem(subgraph, cycle=True, weight='weight'))
                if path[0] == path[-1]:
                    total_cost = sum(euclidean_distance(coordinates[path[i]], coordinates[path[i + 1]]) for i in range(len(path) - 1))
                    max_edge_distance = max(euclidean_distance(coordinates[path[i]], coordinates[path[i+1]]) for i in range(len(path) - 1))
                    return path, total_cost, max_edge_distance

    return None, None, None

# Setup and solve the BTSP
graph = create_graph()
tour, total_travel_cost, max_consecutive_distance = check_hamiltonian_cycle(graph)

if tour and total_travel_client and max_consecutive_distance:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_consecutive_distance:.2f}")
else:
    print("No feasible solution found.")