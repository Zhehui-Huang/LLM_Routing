import math
import itertools
from scipy.spatial.distance import euclidean
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from networkx.algorithms.matching import min_weight_matching
from networkx import Graph

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}

# Number of cities
num_cities = len(cities)

# Distance matrix computation
def calculate_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in cities:
        for j in cities:
            if i != j:
                dist_matrix[i][j] = euclidean(cities[i], cities[j])
    return dist_matrix

distance_matrix = calculate_distance_matrix(cities)

# Minimum Spanning Tree using the distance matrix
def get_minimum_spanning_tree(dist_matrix):
    tree = minimum_spanning_tree(csr_matrix(dist_matrix))
    return tree.toarray().astype(float)

mst_matrix = get_minimum_spanning_tree(distance_matrix)

# Find nodes with odd degree in MST
def find_odd_degree_nodes(mst):
    degree = [0] * num_cities
    for i in range(num_cities):
        for j in range(num_cities):
            if mst[i][j] > 0:
                degree[i] += 1
    odd_degree_nodes = [i for i in range(num_cities) if degree[i] % 2 == 1]
    return odd_degree_nodes

odd_degree_nodes = find_odd_degree_nodes(mst_matrix)

# Minimum Cost Perfect Matching on odd degree nodes
def perfect_matching_on_odd_nodes(odd_nodes, dist_matrix):
    g = Graph()
    g.add_nodes_from(odd_nodes)
    for pair in itertools.combinations(odd_nodes, 2):
        wt = dist_matrix[pair[0]][pair[1]]
        g.add_edge(*pair, weight=wt)
    matching = min_weight_matching(g, maxcardinality=True, weight='weight')
    return matching

matching = perfect_matching_on_odd_nodes(odd_degree_node, distance_matrix)

merged = mst_matrix.copy()
for u, v in matching:
    merged[u][v] = distance_matrix[u][v]
    merged[v][u] = distance_matrix[v][u]

# Convert the graph to an eulerian tour
def find_eulerian_tour(merged):
    from functools import reduce
    tour = []
    for i in range(num_cities):
        if sum(merged[i]) > 0:
            tour.append(i)
    return tour

tour = find_eulerian_tour(merged)

# Making sure the tour starts and ends at depot city 0
# and converting to a Hamiltonian path
final_tour = [0]
visited = set(final_tour)
for city in tour[1:]:
    if city not in visited:
        final_tour.append(city)
        visited.add(city)
final_tour.append(0)

# Calculating total travel cost of the tour
total_cost = 0
for i in range(1, len(final_tour)):
    total_cost += distance_matrix[final_tour[i-1]][final_tour[i]]

# Output the tour and the travel cost
print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_cost}")