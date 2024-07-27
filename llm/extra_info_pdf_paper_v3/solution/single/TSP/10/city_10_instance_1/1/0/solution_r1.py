import math
from itertools import combinations
import networkx as nx

def euclidean_distance(p1, p2):
    return math.dist(p1, p2)

def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

def find_minimum_spanning_tree(cities):
    n = len(cities)
    G = nx.Graph()
    for i in range(n):
        for j in range(i + 1, n):
            G.add_edge(i, j, weight=euclidean_distance(cities[i], cities[j]))
    return nx.minimum_spanning_tree(G)

def find_odd_degree_vertices(G):
    return [v for v, degree in G.degree() if degree % 2 != 0]

def min_weight_perfect_matching(G, odd_vertices):
    return nx.algorithms.matching.min_weight_matching(G.subgraph(odd_vertices), maxcardinality=True)

def create_eulerian_circuit(G, starting_vertex):
    if nx.is_eulerian(G):
        return list(nx.eulerian_circuit(G, source=starting_vertex))
    return None

def simplify_tour(circuit):
    visited = set()
    tour = []
    for u, _ in circuit:
        if u not in visited:
            tour.append(u)
            visited.add(u)
    tour.append(tour[0])
    return tour

def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance_matrix[tour[i-1]][tour[i]]
    return total_cost

# Define city coordinates
cities = [
    (53, 68), (75, 11), (91, 95), (22, 80),
    (18, 63), (54, 91), (70, 14), (97, 44),
    (17, 69), (95, 89)
]

# Calculate distance matrix
distance_matrix = calculate_distance_matrix(cities)

# Create graph and find minimum spanning tree
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        G[i][j]['weight'] = distance_matrix[i][j]
mst = find_minimum_spanning_tree(cities)

# Get vertices with odd degree and calculate the minimal perfect matching
odd_degree_vertices = find_odd_degree_vertices(mst)
matching = min_weight_perfect_matching(G, odd_degree_vertices)

# Create combined graph of MST and Matching
multi_graph = nx.MultiGraph(mst)
multi_graph.add_edges_from(matching)

# Create Eulerian circuit
circuit = create_eulerian_circuit(multi_graph, 0)

# Construct the simplified tour
tour = simplify_tour(circuit)

# Calculate cost
tour_cost = calculate_tour_cost(tour, distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", tour_cost)