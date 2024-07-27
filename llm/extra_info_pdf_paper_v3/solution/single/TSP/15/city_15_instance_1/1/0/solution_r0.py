import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations

# Define cities' coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
    4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
    8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate Euclidean distances between all cities
def distance_matrix(cities):
    n_cities = len(cities)
    dist_matrix = np.zeros((n_cities, n_cities))
    for i in range(n_cities):
        for j in range(n_cities):
            dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

# Construct a graph based on cities' distances
def create_graph(dist_matrix):
    G = nx.Graph()
    for i in range(len(dist_matrix)):
        for j in range(len(dist_matrix)):
            if i != j:
                G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

# Find Minimum Spanning Tree using Prim's Algorithm
def minimum_spanning_tree(G):
    return nx.minimum_spanning_tree(G, weight='weight')

# Find odd-degree vertices in Minimum Spanning Tree
def find_odd_degree_vertices(MST):
    return [v for v, d in MST.degree() if d % 2 == 1]

# Minimum-cost perfect matching for odd degree vertices
def min_cost_perfect_matching(G, odd_vertices):
    subG = G.subgraph(odd_vertices)
    min_matching = nx.algorithms.matching.min_weight_matching(subG, maxcardinality=True, weight='weight')
    return min_matching

# Combine MST and matching into a multigraph, find Eulerian circuit
def create_eulerian_circuit(MST, matching, start_vertex):
    multi_G = nx.MultiGraph(MST)
    multi_G.add_edges_from(matching)
    eulerian_circuit = list(nx.eulerian_circuit(multi_G, source=start_vertex))
    return eulerian_circuit

# Transform Eulerian circuit into a Hamiltonian path (visit each city once)
def eulerian_to_hamiltonian(eulerian_circuit):
    seen = set()
    path = []
    for u, v in eulerian_circuit:
        if u not in seen:
            path.append(u)
            seen.add(u)
    path.append(path[0])  # complete the cycle
    return path

# Calculate tour cost from the path
def calculate_tour_cost(path, dist_matrix):
    cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
    return cost

# Main function to process the task
def solve_tsp(cities):
    dist_matrix = distance_matrix(cities)
    G = create_graph(dist_matrix)
    MST = minimum_spanning_tree(G)
    odd_vertices = find_odd_degree_vertices(MST)
    matching = min_cost_perfect_matching(G, odd_vertices)
    eulerian_circuit = create_eulerian_circuit(MST, matching, start_vertex=0)
    hamiltonian_path = eulerian_to_hamiltonian(eulerian_circuit)
    total_cost = calculate_tour_cost(hamiltonian_path, dist_matrix)
    return hamiltonian_path, total_cost

# Execute the solving function
tour, cost = solve_tsp(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")