import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix
from networkx.algorithms.approximation import christofides_tsp
from networkx.algorithms.euler import eulerian_circuit

# Define the coordinates of the cities including the depot city.
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Create a complete graph with cities as nodes and edges weighted by Euclidean distance.
def create_graph(coords):
    G = nx.Graph()
    for i, coord1 in enumerate(coords):
        for j, coord2 in enumerate(coords):
            if i != j:
                dist = np.linalg.norm(np.array(coord1)-np.array(coord2))
                G.add_edge(i, j, weight=dist)
    return G

# Executing Christofides Algorithm using NetworkX's built-in function.
G = create_graph(coords)
tour = christofides_tsp(G, weight="weight")

# Calculating the total travel cost of the tour.
def calculate_total_cost(G, tour):
    total_cost = sum(G[tour[i]][tour[(i + 1) % len(tour)]]['weight'] for i in range(len(tour)))
    return total_cost

total_cost = calculate_total_cost(G, tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)