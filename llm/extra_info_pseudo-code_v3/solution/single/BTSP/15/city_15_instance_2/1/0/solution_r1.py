import math
import itertools
from collections import defaultdict
import networkx as nx

# City coordinates initially provided
cities_coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_distances(cities):
    distances = {}
    for i in cities:
        for j in cities:
            if i != j:
                distances[(i, j)] = euclidean_distance(cities[i], cities[j])
    return distances

def has_hamiltonian_cycle(graph, N):
    # This function attempts to find a Hamiltonian Cycle using networkx
    try:
        cycle = nx.algorithms.approximation.traveling_salesman_problem(graph, cycle=True)
        if len(cycle) == N + 1 and cycle[0] == cycle[-1]:
            return cycle
    except nx.NetworkXNoPath:
        return None

def bottleneck_tsp(cities):
    N = len(cities)
    distances = calculate_distances(cities)
    sorted_edges = sorted(distances.items(), key=lambda x: x[1])
    
    graph = nx.Graph()
    graph.add_nodes_from(cities.keys())
    
    for ((u, v), dist) in sorted_edges:
        graph.add_edge(u, v, weight=dist)
        cycle = has_hamiltonian_cycle(graph, N)
        if cycle:
            # Calculate metrics for the found Hamiltonian Cycle
            max_distance = max(distances[(cycle[i], cycle[i+1])] for i in range(len(cycle) - 1))
            total_distance = sum(distances[(cycle[i], cycle[i+1])] for i in range(len(cycle) - 1))
            return cycle, total_distance, max_distance
        
    return None  # In case no cycle is found

# Find the optimal route with the minimum maximum edge length
result = bottleneck_tgsp(cities_coordinates)
if result:
    tour, total_cost, max_edge_length = result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_edge_length)
else:
    print("No Hamiltonian cycle found that satisfies the conditions.")