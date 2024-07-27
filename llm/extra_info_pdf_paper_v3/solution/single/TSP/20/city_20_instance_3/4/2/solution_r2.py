import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean

# Coordinates of all cities including the depot (city 0)
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance between two cities
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

# Create a complete graph with cities as nodes
def create_graph(cities, distances):
    G = nx.Graph()
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            G.add_edge(i, j, weight=distances[i][j])
    return G

# Christofides algorithm to approximate TSP solution
def christofides_tsp(cities):
    distances = calculate_distances(cities)
    G = create_graph(cities, distances)
    # Create a minimum spanning tree
    mst = nx.minimum_spanning_tree(G)
    odd_degree_nodes = [v for v, d in mst.degree() if d % 2 == 1]
    # Create a subgraph of vertices with odd degree
    odd_subgraph = G.subgraph(odd_degree_nodes)
    # Find minimum weight matching
    matching = nx.algorithms.matching.min_weight_matching(odd_subgraph, maxcardinality=True)
    # Combine the MST and the matching to create an Eulerian graph
    mst.add_edges_from(matching)
    # Get the Eulerian tour
    eulerian_tour = list(nx.eulerian_circuit(mst, source=0))
    # Convert Eulerian tour to Hamiltonian circuit
    visited = set()
    tour = [0]
    for u, v in eulerian_tour:
        if v not in visited:
            tour.append(v)
            visited.add(v)
    tour.append(0)  # return to the depot
    # Calculate tour cost
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return tour, tour_cost

# Execute the Christofides TSP algorithm
tour, tour_cost = christofides_tsp(cities)

# Print the results
print("Tour:", tour)
print("Total travel cost:", int(tourasd_cost))