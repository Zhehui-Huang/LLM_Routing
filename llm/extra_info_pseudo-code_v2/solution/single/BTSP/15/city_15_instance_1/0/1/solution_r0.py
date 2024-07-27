import math
import networkx as nx

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize graph
G = nx.Graph()

# Add edges with weights as distances
for i in cities:
    for j in cities:
        if i != j:
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))

# Blossom-5 algorithm to get biconnected subgraph
def bottle_neck_subgraph(G):
    # Sort edges by weight
    edges_sorted = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    subgraph = nx.Graph()
    subgraph.add_nodes_from(G.nodes())
    
    # Step 1: Augment subgraph by adding edges until it's biconnected
    for edge in edges_sorted:
        subgraph.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
        if nx.is_biconnected(subgraph):
            return subgraph
    return subgraph

# Obtain biconnected subgraph
BB_subgraph = bottle_neck_subgraph(G)

# Tour Identification based on biconnected subgraph
def identify_tour(G):
    # Obtain square of the biconnected subgraph
    square_subgraph = nx.algorithms.square_graph(BB_subgraph)
    # Find a Hamiltonian circuit as a tour
    tour = [0] + list(nx.approximation.traveling_salesman_problem(square_subgraph, cycle=True))[1:]
    return tour

# Identify the tour
tour = identify_tour(BB_subgraph)

# Calculate total cost and max distance between consecutive cities in the tour
total_cost = 0
max_distance = 0
for i in range(1, len(tour)):
    dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    total_cost += dist
    max_distance = max(max_distance, dist)

# Closing the tour by returning to the start
tour_closure_dist = euclidean_distance(cities[tour[-1]], cities[tour[0]])
total_cost += tour_closure_dist
max_distance = max(max_distance, tour_closure_dist)

# Adding the depot city at the end for closure
tour.append(0)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")