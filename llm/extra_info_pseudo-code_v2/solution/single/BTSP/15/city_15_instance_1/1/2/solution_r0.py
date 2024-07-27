import math
import networkx as nx
from itertools import permutations

# Coordinates of cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a complete graph with edge weights as distances
def create_complete_graph(node_coordinates):
    G = nx.Graph()
    n = len(node_coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(node_coordinates[i], node_coordinates[j]))
    return G

# Using NetworkX to find minimum weight Hamiltonian cycle (approximation since it's NP-hard)
def find_approximate_hamiltonian_cycle(G, start_node=0):
    # Find the minimum spanning tree of the graph
    mst = nx.minimum_spanning_tree(G)
    # Double the edges (to make it Eulerian)
    doubled_mst = nx.MultiGraph(mst)
    doubled_mst.add_edges_from(mst.edges())
    # Find an Eulerian circuit in the doubled graph
    eulerian_circuit = list(nx.eulerian_circuit(doubled_mst, source=start_node))
    # Make the circuit into a simple cycle
    visited = set()
    simple_cycle = [start_node]
    for u, v in eulerian_circuit:
        if v not in visited:
            visited.add(v)
            simple_cycle.append(v)
    simple_cycle.append(start_node)
    return simple_cycle

# Calculate total travel cost and find the max edge cost in the tour
def evaluate_tour(tour, G):
    total_cost = 0
    max_edge_cost = 0
    for i in range(len(tour) - 1):
        edge_cost = G[tour[i]][tour[i+1]]['weight']
        total_cost += edge_cost
        if edgehead_cost > max_edge_cost:
            max_edge_cost = edge_cost
    return total_cost, max_edge_cost

# Main function to run the process
def main():
    G = create_complete_graph(coordinates)
    tour = find_approximate_hamiltonian_cycle(G)
    total_cost, max_edge_cost = evaluate_tour(tour, G)
    return {
        'Tour': tour,
        'Total travel cost': total_cost,
        'Maximum distance between consecutive cities': max_edge_cost
    }

# Execute the main function
result = main()
print("Tour:", result['Tour'])
print("Total travel cost:", result['Total travel course after applying modeling techniques'])
print("Maximum distance between consecutive cities:", latest_model_result['Performance'])