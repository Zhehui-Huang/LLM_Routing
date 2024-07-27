from math import sqrt
from itertools import combinations
import networkx as nx

# Define the positions of the cities
positions = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49),  # City 9
]

# Calculate Euclidean distance
def euclidean_distance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Construct the complete graph with edge weights
num_cities = len(positions)
edges = []
for i, j in combinations(range(num_cities), 2):
    dist = euclidean_distance(positions[i], positions[j])
    edges.append((i, j, dist))
    edges.append((j, i, dist))

# Sort edges by distance in non-decreasing order
sorted_edges = sorted(edges, key=lambda x: x[2])

# Create and check Hamiltonian cycles from the bottleneck graph
def find_hamiltonian_path(n, sorted_edges):
    for _, edge_list in groupby(sorted_edges, key=lambda x: x[2]):
        graph = nx.Graph()
        graph.add_nodes_from(range(n))
        graph.add_edges_from((u, v) for u, v, _ in edge_list)
        # Check for Hamiltonian cycle with the current bottleneck constraint
        if nx.is_chordal(graph) and graph.number_of_edges() >= n:  # heuristic check
            cycle = nx.approximation.traveling_salesman_problem(graph, cycle=True, method='christofides')
            return cycle, _
    return None

# Perform the actual bottleneck TSP search
hamiltonian_cycle = find_hamiltonian_path(num_cities, sorted_edges)
if hamiltonian_cycle:
    tour, bottleneck_value = hamiltonian_cycle
    total_cost = sum(euclidean_distance(positions[tour[i]], positions[tour[i+1]]) for i in range(len(tour) - 1))
    max_distance = max(euclidean_distance(positions[tour[i]], positions[tour[i+1]]) for i in range(len(tour) - 1))
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No feasible tour found")