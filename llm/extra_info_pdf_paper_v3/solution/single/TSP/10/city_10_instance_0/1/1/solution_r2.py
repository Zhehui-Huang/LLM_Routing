import numpy as np
from scipy.spatial import distance_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.optimize import linear_sum_assignment
import networkx as nx

def compute_euclidean_distances(coords):
    return distance_matrix(coords, coords)

def find_minimum_spanning_tree(dist_matrix):
    mst = minimum_spanning_tree(dist_matrix)
    return mst.toarray()

def find_odd_degree_nodes(mst):
    degrees = np.sum(mst > 0, axis=1)
    return np.where(degrees % 2 == 1)[0]

def create_min_cost_matching(mst, odd_deg_nodes, dist_matrix):
    num_nodes = len(odd_deg_nodes)
    subgraph = dist_matrix[np.ix_(odd_deg_nodes, odd_deg_nodes)]
    row_ind, col_ind = linear_sum_assignment(subgraph)
    matching_graph = np.zeros_like(mst)
    for i, j in zip(row_ind, col_ind):
        matching_graph[odd_deg_nodes[i], odd_deg_nodes[j]] = subgraph[i, j]
        matching_graph[odd_deg_nodes[j], odd_deg_nodes[i]] = subgraph[i, j]
    return matching_graph

def create_eulerian_graph(mst, matching_graph):
    return mst + matching_graph

def find_eulerian_tour(graph):
    g = nx.from_numpy_matrix(graph, create_using=nx.MultiGraph)
    eulerian_circuit = list(nx.eulerian_circuit(g, source=0))
    return [u for u, v in eulerian_circuit] + [eulerian_circuit[0][0]]

def make_hamiltonian_path(eulerian_tour):
    seen = set()
    hamiltonian_path = []
    for city in eulerian_tour:
        if city not in seen:
            hamiltonian_path.append(city)
            seen.add(city)
    hamiltonian_path.append(hamiltonian_path[0])  # To make a complete tour
    return hamiltonian_path

def compute_total_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Cities coordinates
coords = np.array([
    (50, 42), (41, 1), (18, 46), (40, 98), (51, 69),
    (47, 39), (62, 26), (79, 31), (61, 90), (42, 49)])
    
dist_matrix = compute_euclidean_distances(coords)
mst = find_minimum_spanning_tree(dist_matrix)
odd_deg_nodes = find_odd_degree_nodes(mst)
matching_graph = create_min_cost_matching(mst, odd_deg_nodes, dist_matrix)
eulerian_graph = create_eulerian_graph(mst, matching_graph)
eulerian_tour = find_eulerian_tour(eulerian_graph)
hamiltonian_path = make_hamiltonian_path(eulerian_tour)
total_cost = compute_total_cost(hamiltonian_path, dist_matrix)

print(f'Tour: {hamiltonian_path}')
print(f'Total travel cost: {total_cost:.2f}')