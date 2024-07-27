import numpy as np
import networkx as nx
from scipy.spatial.distance import euclidean
from itertools import combinations
from scipy.optimize import linear_sum_assignment

def calculate_distance_matrix(cities):
    num_cities = len(cities)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distance_matrix[i][j] = euclidean(cities[i], cities[j])
    return distance_matrix

def mst_and_odd_vertices(graph):
    mst = nx.minimum_spanning_tree(graph)
    odd_degree_nodes = [v for v in mst.nodes() if mst.degree(v) % 2 == 1]
    return mst, odd_degree_nodes

def min_weight_perfect_matching(graph, odd_degree_nodes):
    subgraph = graph.subgraph(odd_degree_appng_nodes)
    complete_graph = nx.Graph()
    for u, v in combinations(odd_degree_nodes, 2):
        complete_graph.add_edge(u, v, weight=graph[u][v]['weight'])
    
    cost_matrix = np.full((len(odd_degree_nodes), len(odd_degree_nodes)), np.inf)
    for i, u in enumerate(odd_degree_nodes):
        for j, v in enumerate(odd_degree_nodes):
            if u != v:
                cost_matrix[i][j] = graph[u][v]['weight']
    
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    new_graph = nx.Graph()
    for idx in range(len(row_ind)):
        u = odd_degree_nodes[row_ind[idx]]
        v = odd_degree_nodes[col_ind[idx]]
        new_graph.add_edge(u, v, weight=graph[u][v]['weight'])
    
    return new_graph

def find_eulerian_tour(graph):
    eulerian_tour = list(nx.eulerian_circuit(graph, source=0))
    return eulerian_tour

def transform_to_hamiltonian(eulerian_tour):
    visited = set()
    hamiltonian_circuit = []
    for u, v in eulerian_tour:
        if u not in visited:
            hamiltonian_circuit.append(u)
            visited.add(u)
    hamiltonian_circuit.append(0)  # adding the depot city to complete the circuit
    return hamiltonian_circuit

# Define the cities coordinates
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Calculate Distance Matrix and create Graph
distance_matrix = calculate_distance_matrix(cities)
G = nx.complete_graph(len(cities))
for i in range(len(cities)):
    for j in range(len(cities)):
        G[i][j]["weight"] = distance_matrix[i][j]

# Step 1: Minimum Spanning Tree (MST) and odd vertices
mst, odd_degree_nodes = mst_and_odd_vertices(G)

# Step 2: Minimum-Weight Perfect Matching
M = min_weight_perfect_matching(G, odd_degree_nodes)

# Step 3: Combine MST and Matching
G_multigraph = nx.MultiGraph()
G_multigraph.add_edges_from(mst.edges(data=True))
G_multigraph.add_edges_from(M.edges(data=True))

# Step 4: Eulerian Circuit
eulerian_tour = find_eulerian_tour(G_multigraph)

# Step 5: Hamiltonian Circuit
tour = transform_to_hamiltonian(eulerian_tour)

# Calculate cost of the tour
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)