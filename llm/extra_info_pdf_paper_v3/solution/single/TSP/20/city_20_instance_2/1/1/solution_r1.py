import math
import networkx as nx
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_odd_degree_vertices(T):
    odd_degree_vertices = []
    for node, degree in dict(T.degree()).items():
        if degree % 2 != 0:
            odd_degree_vertices.append(node)
    return odd_degree_vertices

def minimum_weight_perfect_matching(G, odd_degree_vertices):
    subgraph = G.subgraph(odd_degree_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True)

def create_eulerian_circuit(combined_graph, starting_vertex):
    return list(nx.eulerian_circuit(combined_graph, source=starting_vertex))

def compute_tour_cost(distance_matrix, tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# City coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Calculate the distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Create the graph from the distance matrix
G = nx.Graph()
for i in range(num_cities):
    for j in range(i+1, num_cities):  # Avoid repeating edges
        G.add_edge(i, j, weight=distance_matrix[i][j])

# 1. Minimum Spanning Tree
mst = nx.minimum_spanning_tree(G)

# 2. Find vertices with odd degree
odd_degree_vertices = find_odd_degree_vertices(mst)

# 3. Minimum-cost perfect matching
matching = minimum_weight_perfect_matching(G, odd_degree_vertices)

# 4. Combine the MST and matching
mst.add_edges_from(matching)

# 5. Find the Eulerian circuit
eulerian_circuit = create_eulerian_circuit(mst, starting_vertex=0)

# 6. Convert to Hamiltonian circuit
visited = set()
tour = []
for u, v in eulerian_circuit:
    if u not in visited:
        tour.append(u)
        visited.add(u)
tour.append(0)  # Complete the tour by returning to the start

# 7. Calculate the tour cost
tour_cost = compute_tour_cost(distance_matrix, tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {tour_cost}")