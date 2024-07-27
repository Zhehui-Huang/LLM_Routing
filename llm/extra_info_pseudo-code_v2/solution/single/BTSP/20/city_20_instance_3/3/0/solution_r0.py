import math
from itertools import combinations
from networkx import Graph
from networkx.algorithms.connectivity import minimum_edge_cut, is_biconnected
from networkx.algorithms.approximation import traveling_salesman_problem

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def create_graph(cities):
    graph = Graph()
    n = len(cities)
    distances = {}
    # Adding edges with weights based on Euclidean distance
    for (i, city1), (j, city2) in combinations(enumerate(cities), 2):
        dist = euclidean_distance(city1, city2)
        distances[(i, j)] = dist
        graph.add_edge(i, j, weight=dist)

    # Sort edges by distance ascending
    sorted_edges = sorted(distances.items(), key=lambda x: x[1])
    return graph, sorted_edges

def bottleneck_optimal_biconnected_subgraph(graph, sorted_edges):
    # Step 0: Initialize E_BB as an empty set in the form of a Graph
    E_BB = Graph()
    E_BB.add_nodes_from(graph)

    # Step 1 and 2: Add edges while checking biconnectivity
    for (u, v), weight in sorted_iv:
        E_BB.add_edge(u, v, weight=weight)
        if is_biconnected(E_BB):
            break
    
    return E_BB, max((data['weight'] for u, v, data in E_BB.edges(data=True)))

def compute_tour(subgraph):
    # Step 2: Identify an approximate optimal tour in the square graph
    square = subgraph.copy()
    n = square.number_of_nodes()
    for u in square.nodes():
        neighbors_u = list(square.neighbors(u))
        for i in range(len(neighbors_u)):
            for j in range(i + 1, len(neighbors_u)):
                if not square.has_edge(neighbors_u[i], neighbors_u[j]):
                    weight = square[u][neighbors_u[i]]['weight'] + square[u][neighbors_u[j]]['weight']
                    square.add_edge(neighbors_u[i], neighbors_u[j], weight=weight)

    # Approximate solution to the Traveling Salesman Problem
    tour = traveling_salesman_problem(square, cycle=True, weight='weight', method='greedy')
    return tour

# Define cities as tuples of (x, y) coordinates
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Initialize graph and sort edges
graph, sorted_iv = create_graph(cities)

# Step 1: Find bottleneck-optimal biconnected subgraph
biconnected_subgraph, max_weight = bottleneck_optimal_biconnected_subgraph(graph, sorted_iv)

# Step 2: Compute Tour
tour = compute_tour(biconnected_subgraph)

# Output formatting
total_cost = sum(graph.edges[tour[i], tour[i + 1]]['weight'] for i in range(len(tour) - 1))
max_distance = max(graph.edges[tour[i], tour[i + 1]]['weight'] for i in range(len(tour) - 1))

output_tour = tour + [tour[0]]

print(f"Tour: {output_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_weight:.2f}")