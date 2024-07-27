import math
import networkx as nx
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of cities
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculate distances between all pairs of cities
distances = {(i, j): euercise(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Sort edges by distance
sorted_edges = sorted(distances.items(), key=lambda x: x[1])

# Attempting construction of Hamiltonian paths
def closest_distance_threshold(edges):
    G = nx.Graph()

    for (i, j), dist in edges:
        G.add_edge(i, j, weight=dist)
        if nx.is_connected(G) and len(nx.minimum_spanning_edges(G)) == len(cities) - 1:
            # Check for Hamiltonian Cycle
            tsp_solution = nx.approximation.traveling_salesman_problem(G, weight='weight', cycle=True)
            if tsp_solution[0] == tsp_solution[-1] and sorted(tsp_solution[:-1]) == sorted(cities.keys()):
                return tsp_solution, dist
    return None, None

# Main loop to find the smallest threshold distance
for threshold in sorted(set(distances.values())):
    graph_edges = [(e, dist) for e, dist in sorted_edges if dist <= threshold]
    tour, distance_threshold = closest_distance_threshold(graph_edges)
    if tour:
        # Calculate metrics
        max_distance = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        total_distance = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
        print("Tour:", tour)
        print("Total travel cost:", total_distance)
        print("Maximum distance between consecutive cities:", max_distance)
        break  # Stop once a valid tour is found
else:
    print("No valid route found.")