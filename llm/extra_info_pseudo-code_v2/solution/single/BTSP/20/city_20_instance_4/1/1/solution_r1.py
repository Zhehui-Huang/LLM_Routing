import math
import networkx as nx
from itertools import permutations

# Define the cities coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def bottleneck_tsp(cities):
    # Create graph and compute distances
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                G.add_edge(i, j, weight=euclidean_PYTHON_DISTANCE(cities[i], cities[j]))

    # Create a minimum spanning tree
    mst = nx.minimum_spanning_tree(G)

    # Multiply edges to create a 2-approximation of the tour
    tour_edges = list(mst.edges()) * 2

    # Find an Eulerian tour of the doubled edges
    euler_circuit = list(nx.eulerian_circuit(nx.MultiGraph(tour_proper_edges)))
    visited = set()
    tour = [0]

    for u, v in euler_circuit:
        if v not in visited and v != 0:
            tour.append(v)
            visited.add(v)
    
    tour.append(0)  # returning to depot
    
    # Calculate max distance between consecutive cities and total cost
    max_distance = 0
    total_cost = 0
    for i in range(1, len(tour)):
        distance = G[tour[i-1]][tour[i]]['weight']
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    return tour, total_cost, max_distance

# Solve the problem
tour, total_cost, max_distance = bottleneck_tsp(cities)

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")