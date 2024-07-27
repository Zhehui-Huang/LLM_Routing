import math
import networkx as nx

# Define the cities and their coordinates
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create a complete graph with distances as weights
def create_graph(coordinates):
    G = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=calculate_distance(coordinates[i], coordinates[j]))
    return G

# Find a bottleneck-optimal biconnected subgraph
def find_biconnected_subgraph(G):
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    H = nx.Graph()
    H.add_nodes_from(G.nodes())
    for u, v, data in edges_sorted:
        H.add_edge(u, v, weight=data['weight'])
        if nx.is_biconnected(H):
            return H
    return H  # In case all edges are necessary

# Finding the tour
def find_tour(H, start_node=0):
    # Utilizing Christofides algorithm to approximate the solution
    cycle = list(nx.approximation.traveling_salesman_problem(H, cycle=True, weight='weight'))
    if cycle[0] != start_node:
        # Rotate to start at the depot city (start_node)
        start_index = cycle.index(start_node)
        cycle = cycle[start_index:] + cycle[:start_index]
    cycle.append(cycle[0])  # Complete the circuit by returning to the start
    return cycle

# Main function to execute the solution strategy
def solve_btsp(coordinates):
    G = create_graph(coordinates)
    H = find_biconnected_subgraph(G)
    tour = find_tour(H)
    if start_node != tour[-1]:  # Ensure the tour ends at the depot
        tour.append(start_node)

    total_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    max_distance = max(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

    return {
        "Tour": tour,
        "Total travel cost": total_cost,
        "Maximum distance between consecutive cities": max_distance
    }

# Execute and print results
result = solve_btsp(coordinates)
print(f"Tour: {result['Tour']}")
print(f"Total travel cost: {round(result['Total travel cost'], 2)}")
print(f"Maximum distance between consecutive cities: {round(result['Maximum distance between consecutive cities'], 2)}")