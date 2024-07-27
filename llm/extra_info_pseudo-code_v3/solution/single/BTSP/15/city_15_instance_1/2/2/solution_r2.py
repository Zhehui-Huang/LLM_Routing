import math
import itertools
import networkx as nx

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
num_cities = len(cities)
dist_matrix = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Sort list of edges based on their distances extracted from distance matrix
edges = [(i, j, dist_matrix[i][j]) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges.sort(key=lambda x: x[2])

# Utility to construct graph from edges under given weight limit
def create_graph(weight_limit):
    G = nx.Graph()
    for u, v, w in edges:
        if w <= weight_limit:
            G.add_edge(u, v, weight=w)
    return G

# Iterate over unique weights to find minimal bottleneck Hamiltonian cycle
for weight in set(edge[2] for edge in edges):
    G = create_graph(weight)
    if nx.is_connected(G) and all(G.degree(node) >= 2 for node in G):
        try:
            cycle = nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight')
            if len(cycle[:-1]) == num_cities:  # Check if all cities are included
                max_distance_in_cycle = max(dist_matrix[cycle[i]][cycle[i+1]] for i in range(len(cycle) - 1))
                total_cost = sum(dist_matrix[cycle[i]][cycle[i+1]] for i in range(len(cycle) - 1))
                print(f"Tour: {cycle}")
                print(f"Total travel cost: {total_cost}")
                print(f"Maximum distance between consecutive cities: {max_distance_in_cycle}")
                break
        except nx.NetworkXNoPath:
            continue