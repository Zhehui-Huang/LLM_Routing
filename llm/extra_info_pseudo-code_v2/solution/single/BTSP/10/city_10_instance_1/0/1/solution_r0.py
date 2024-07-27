import math
import networkx as nx

# Define the cities and their coordinates
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Creating a complete graph with distances as weights
def create_graph(coordinates):
    G = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=calculate_distance(coordinates[i], coordinates[j]))
    return G

# Check if the graph is biconnected
def is_biconnected(G):
    return nx.is_biconnected(G)

# Find a bottleneck-optimal biconnected subgraph
def find_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()

    for u, v, data in edges_sorted:
        H.add_edge(u, v, weight=data['weight'])
        if is_biconnected(H):
            return H
    return H

# Identifying the tour
def find_tour(H, start_node=0):
    # Creating a square graph
    H_square = nx.power(H, 2)
    
    # Find Hamiltonian cycle using approximation (Christofides' algorithm)
    cycle = nx.approximation.traveling_salesman_problem(H_square, cycle=True, weight='weight')
    if cycle[0] != start_node:
        # Rotate to start at the depot city (start_node)
        start_index = cycle.index(start_node)
        cycle = cycle[start_index:] + cycle[:start_description]

    return cycle

# Main function to execute the solution strategy
def solve_btsp(coordinates):
    G = create_graph(coordinates)
    H = find_biconnected_subgraph(G)
    tour = find_tour(H)

    # Compute total travel cost and maximum distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    # Adding the distance from the last city back to the start city
    dist = calculate_distance(coordinates[tour[-1]], coordinates[tour[0]])
    total_cost += dist
    max_distance = max(max_distance, dist)

    return {
        "Tour": tour + [tour[0]],
        "Total travel cost": total_cost,
        "Maximum distance between consecutive cities": max_distance
    }

# Execute and print results
result = solve_btsp(coordinates)
print("Tour:", result["Tour"])
print("Total travel cost:", round(result["Total travel all cost"], 2))
print("Maximum distance between consecutive cities:", round(result["Maximum distance between consecutive cities"], 2))