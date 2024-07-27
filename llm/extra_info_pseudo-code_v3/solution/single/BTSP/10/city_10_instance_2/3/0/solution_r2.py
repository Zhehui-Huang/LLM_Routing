import math
import networkx as nx
from itertools import permutations, combinations

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def find_bottleneck_tsp_tour(coords):
    n = len(coords)
    # Create all possible edges along with their weights
    edges = [(i, j, euclidean_distance(coords[i], coords[j])) for i in range(n) for j in range(i + 1, n)]
    edges = sorted(edges, key=lambda x: x[2])  # Sort edges by weight

    for _, _, max_weight in edges:
        G = nx.Graph()
        G.add_nodes_from(range(n))
        edge_list = [(u, v) for u, v, w in edges if w <= max_weight]
        G.add_edges_from(edge_list)
        # Try to find a Hamiltonian cycle in the graph limited by max_weight
        for perm in permutations(range(1, n)):  # Start from node 0 and check permutational paths connecting back to 0
            cycle = [0] + list(perm) + [0]
            if all(G.has_edge(cycle[i], cycle[i+1]) for i in range(len(cycle)-1)):
                total_cost = sum(euclidean_distance(coords[cycle[i]], coords[cycle[i+1]]) for i in range(len(cycle)-1))
                return cycle, total_cost, max_weight

    return None, None, None

cities = [
    (90, 3),  # City 0 (Depot)
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Execute the TSP solving function
tour, total_cost, max_distance = find_bottleneck_tsp_tour(cities)

if tour:
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No feasible tour found.")