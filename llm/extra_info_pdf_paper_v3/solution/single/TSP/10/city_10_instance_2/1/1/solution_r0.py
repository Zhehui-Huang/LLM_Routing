import numpy as np
from scipy.spatial.distance import euclidean
from itertools import combinations
from networkx import Graph, minimum_spanning_tree, complete_graph, odd_degree_nodes
from networkx.algorithms.matching import min_weight_matching

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate distances between all pairs of cities
def distance_matrix(cities):
    num_cities = len(cities)
    dists = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dists[i][j] = euclidean(cities[i], cities[j])
    return dists

dist_matrix = distance_matrix(cities)

# Create a complete graph from distances
def create_complete_graph(dist_matrix):
    G = Graph()
    num_cities = len(dist_matrix)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            G.add_edge(i, j, weight=dist_matrix[i][j])
    return G

complete_G = create_complete_graph(dist_matrix)

# Function to find a minimum weight matching in the graph for odd degree vertices
def perfect_matching_min_weight(odd_verts, graph):
    odd_graph = complete_graph(odd_verts)
    for u, v, d in odd_graph.edges(data=True):
        d['weight'] = graph[u][v]['weight']
    return min_weight_matching(odd_graph, maxcardinality=True, weight='weight')

# Christofides' algorithm implementation
def christofides_tsp(graph):
    # 1. Create Minimum Spanning Tree (MST)
    mst = minimum_spanning_tree(graph)
    
    # 2. Find vertices with an odd degree
    odd_degree_vertices = list(odd_degree_nodes(mst))
    
    # 3. Find minimum weight perfect matching for odd degree vertices in MST
    matching = perfect_matching_min_weight(odd_degree_vertices, graph)
    
    # 4. Combine MST and minimum weight perfect matching
    multi_graph = Graph()
    for u, v, data in mst.edges(data=True):
        multi_graph.add_edge(u, v, weight=data['weight'])
    for u, v in matching:
        multi_graph.add_edge(u, v, weight=graph[u][v]['weight'])

    # 5. Find an Eulerian circuit in the combined graph
    eulerian_tour = list(nx.eulerian_circuit(multi_graph, source=0))
    
    # 6. Make the tour Hamiltonian
    seen = set()
    hamiltonian_tour = [0]
    for u, v in eulerian_tour:
        if v not in seen:
            seen.add(v)
            hamiltonian_tour.append(v)
    hamiltonian_tour.append(0)  # return to depot city 0
    
    return hamiltonian_tour

# Get the tour
tour = christofides_tsp(complete_G)

# Calculate the total cost of the tour
def calculate_total_cost_of_tour(tour, dist_matrix):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += dist_matrix[tour[i-1]][tour[i]]
    return total_cost

total_cost = calculate_total_cost_of_tour(tour, dist_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)