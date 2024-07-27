import numpy as np
import networkx as nx
from itertools import combinations
from scipy.spatial.distance import euclidean

def calculate_distances(cities):
    n = len(cities)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = euclidean(cities[i], cities[j])
    return dist

def find_mst(distances):
    G = nx.Graph()
    n = len(distances)
    for i in range(n):
        for j in range(i+1, n):
            G.add_edge(i, j, weight=distances[i][j])
    return nx.minimum_spanning_tree(G)

def find_odd_vertices(mst):
    return [v for v, d in mst.degree() if d % 2 == 1]

def minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, True)

def create_eulerian_graph(mst, matching):
    eulerian_graph = nx.MultiGraph(mst)
    eulerian_graph.add_edges_from(matching)
    return eulerian_graph

def find_hamiltonian_circuit(eulerian_graph, start_vertex):
    eulerian_circuit = list(nx.eulerian_circuit(eulerian_graph, source=start_vertex))
    path = [start_vertex]
    visited = set(path)
    for u, v in eulerian_circuit:
        if v not in visited:
            path.append(v)
            visited.add(v)
    path.append(start_vertex)
    return path

def total_travel_cost(cities, tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Cities coordinates specified
cities = [
    (53, 68),  # Depot city 0
    (75, 11),
    (91, 95),
    (22, 80),
    (18, 63),
    (54, 91),
    (70, 14),
    (97, 44),
    (17, 69),
    (95, 89)
]

# Calculate pair-wise distances
distances = calculate_distances(cities)

# Compute the MST
mst = find_mst(distances)

# Find odd degree vertices
odds = find_odd_vertices(mst)

# Compute the minimum weight perfect matching on odd vertices
matching = minimum_weight_perfect_matching(mst, odds)

# Create Eulerian graph by merging MST and matching
eulerian_graph = create_eulerian_graph(mst, matching)

# Find the Hamiltonian circuit using the Eulerian circuit technique
tour = find_hamiltonian_circuit(eulerian_graph, start_vertex=0)

# Compute the total cost of the tour
cost = total_travel_cost(cities, tour)

# Output the tour and the total travel cost
print("Tour:", tour)
print("Total travel cost:", cost)