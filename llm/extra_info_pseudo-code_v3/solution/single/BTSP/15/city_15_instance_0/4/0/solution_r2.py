import math
import networkx as nx

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Function to construct a graph up to a given threshold
def construct_graph(cities, max_distance):
    G = nx.Graph()
    n = len(cities)
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            if dist <= max_distance:
                G.add_edge(i, j, weight=dist)
    return G

# Main function to find the optimal Hamiltonian path minimizing max edge length
def optimal_path(cities):
    n = len(cities)
    edges = [
        (i, j, euclidean_distance(cities[i], cities[j]))
        for i in range(n) for j in range(i+1, n)
    ]
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    
    for _, _, d in edges:
        G = construct_graph(cities, d)
        try:
            cycle = nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight')
            if cycle[0] == 0 and cycle[-1] == 0:
                max_edge_length = max(euclidean_distance(cities[cycle[i]], cities[cycle[i+1]]) for i in range(len(cycle)-1))
                total_distance = sum(euclidean_distance(cities[cycle[i]], cities[cycle[i+1]]) for i in range(len(cycle)-1))
                return cycle, total_distance, max_edge_length
        except nx.NetworkXError:
            continue
    return None

# Cities coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Find optimal path minimizing the maximum distance between consecutive cities
result = optimal_path(cities)
if result:
    path, total_cost, max_edge_length = result
    print(f"Tour: {path}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_edge_length}")
else:
    print("No suitable tour found.")