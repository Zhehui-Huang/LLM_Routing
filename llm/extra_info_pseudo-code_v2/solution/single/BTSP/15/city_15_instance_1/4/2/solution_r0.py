import math
import networkx as nx
from itertools import combinations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def initialize_cities():
    return [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]

def construct_graph(cities):
    G = nx.Graph()
    n = len(cities)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return G

def bottleneck_optimal_biconnected_subgraph(graph):
    edges_sorted = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    E_BB = set()
    for edge in edges_sorted:
        E_BB.add(edge)
        subgraph = nx.Graph()
        subgraph.add_edges_from(E_BB)
        if nx.is_biconnected(subgraph):
            return subgraph  # As soon as it's biconnected, we stop

def find_approximate_tour(subgraph, start_node):
    # Make the graph complete by squaring it (this is not a real square, just ensures all nodes are Mathematically reachable)
    squared_subgraph = nx.Graph()
    squared_subgraph.add_nodes_from(subgraph.nodes())
    for u, v in combinations(subgraph.nodes(), 2):
        min_dist = min(euclidean_distance(cities[u], cities[v]), subgraph[u][v]['weight'])
        squared_subgraph.add_edge(u, v, weight=min_dist)

    # Attempt to find Hamiltonian cycle using TSP approximation
    tsp_tour = list(nx.approximation.traveling_salesman_problem(squared_subargph, cycle=True))
    tsp_tour.append(tsp_tour[0])  # to make it a cycle
    return tsp_tour

# Main execution
cities = initialize_cities()
graph = construct_graph(cities)
bobs = bottleneck_optimal_biconnected_subgraph(graph)
tour = find_approximate_tour(bobs, start_node=0)
tour_distances = [round(graph[tour[i]][tour[i+1]]['weight'], 2) for i in range(len(tour)-1)]
total_cost = sum(tour_distances)
max_distance = max(tour_distances)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)