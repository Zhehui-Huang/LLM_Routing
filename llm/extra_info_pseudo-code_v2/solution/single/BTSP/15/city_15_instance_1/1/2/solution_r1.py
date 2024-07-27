import math
import networkx as nx

# Coordinates of cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a full mesh graph where each node is a city and each edge weight is the Euclidean distance between cities
def create_complete_graph(node_coordinates):
    G = nx.Graph()
    n = len(node_coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(node_coordinates[i], node_coordinates[j])
            G.add_edge(i, j, weight=dist)
    return G

# Algorithm to find a tour minimizing the maximum edge length (Implementation of the pseudocode provided)
def find_bottleneck_hamiltonian_cycle(G):
    # Start with empty biconnected component
    edges_sorted_by_weight = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    selected_edges = []
    biconnected_graph = nx.Graph()
    
    # Add edges until the graph is biconnected
    for u, v, data in edges_sorted_by_weight:
        biconnected_graph.add_edge(u, v, weight=data['weight'])
        selected_edges.append((u, v))
        if nx.is_biconnected(biconnected_graph):
            break

    # Find the minimum weight maximum edge in the biconnected component
    tour = nx.approximation.traveling_salesman_problem(biconnected_graph, cycle=True, weight='weight')
    
    # Re-adjust to ensure the starting point is 0 and the end point is 0
    start_index = tour.index(0)
    adjusted_tour = tour[start_index:] + tour[:start_index] + [0]
    
    return adjusted_tour

# Calculate the total cost and max edge distance in the given tour
def evaluate_tour(tour, G):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour)-1):
        edge_cost = G[tour[i]][tour[i+1]]['weight']
        total_cost += edge_cost
        max_distance = max(max_distance, edge_cost)
    return total_cost, max_distance

# Main algorithm execution
def main():
    G = create_complete_graph(coordinates)
    tour = find_bottleneck_hamiltonian_cycle(G)
    total_cost, max_edge_distance = evaluate_tour(tour, G)
    
    return {
        'Tour': tour,
        'Total travel cost': total_cost,
        'Maximum distance between consecutive cities': max_edge_distance
    }

# Execution of the main function and print the output
result = main()
print("Tour:", result['Tour'])
print("Total travel cost:", result['Total travel cost'])
print("Maximum distance between consecutive cities:", result['Maximum distance between consecutive cities'])