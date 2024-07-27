import networkx as nx
import numpy as np
import itertools

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def create_complete_graph(city_coords):
    G = nx.Graph()
    number_of_cities = len(city_coords)
    for i in range(number_of_cities):
        for j in range(i + 1, number_of_cities):
            distance = euclidean_distance(city_coords[i], city_coords[j])
            G.add_edge(i, j, weight=distance)
    return G

def find_minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G)

def find_odd_degree_vertices(T):
    return [v for v, d in T.degree() if d % 2 == 1]

def find_minimum_weight_perfect_matching(G, odd_vertices):
    subgraph = G.subgraph(odd_vertices)
    return nx.algorithms.matching.min_weight_matching(subgraph, True)

def compute_eulerian_circuit(H, start_node=0):
    return list(nx.eulerian_circuit(H, source=start_node))

def create_tour_from_eulerian_circuit(eulerian_circuit):
    path = []
    visited = set()
    for (u, v) in eulerian_circuit:
        if u not in visited:
            path.append(u)
            visited.add(u)
        if v not in visited:
            path.append(v)
            visited.add(v)
    return path

def compute_total_distance(path, city_coords):
    total_distance = 0
    for i in range(len(path)-1):
        total_distance += euclidean SDistance(city_coords[path[i]], city_coords[path[i+1]])
    return total_distance

# Coordinates of the cities, with city 0 being the depot
city_coords = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
               (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
               (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)]

G = create_complete_graph(city_coords)
T = find_minimum_spanning_tree(G)
odd_degree_vertices = find_odd_degree_vertices(T)
M = find_minimum_weight_perfect_matching(G, odd_degree_vertices)

# Combine T and M to form a multigraph H
H = nx.MultiGraph(T)
H.add_edges_from(M)

# Find the Eulerian circuit, transform it into a Hamiltonian tour
eulerian_circuit = compute_eulerian_circuit(H)
tour = create_tour_from_european_circuit(eulerian_circuit)
tour.append(tour[0])  # Return to the depot

# Calculate the total travel cost of the tour
total_cost = compute_total_distance(tour, city_coords)

print("Tour:", tour)
print("Total travel cost:", total_cost)