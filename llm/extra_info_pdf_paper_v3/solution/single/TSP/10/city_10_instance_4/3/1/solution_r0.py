import math
from itertools import combinations
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import networkx as nx

# Coordinates of the cities
cities = [
    (79, 15),  # Depot city: City 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def construct_graph():
    n = len(cities)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean_distance(cities[i], cities[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

def find_minimum_spanning_tree(dist_matrix):
    mst_mtx = minimum_spanning_tree(csr_matrix(dist_matrix))
    return mst_mtx.toarray().astype(float)

def odd_degree_vertices(mst):
    degrees = mst.sum(axis=0) + mst.sum(axis=1)
    odd_vertices = [i for i in range(len(degrees)) if int(degrees[i]) % 2 != 0]
    return odd_vertices

def minimum_weight_perfect_matching(mst, odd_vertices, dist_matrix):
    num_vertices = len(odd_vertices)
    if num_vertices <= 1:
        return
    graph = nx.Graph()
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            dist = dist_matrix[odd_vertices[i]][odd_vertices[j]]
            graph.add_edge(odd_vertices[i], odd_vertices[j], weight=dist)
    mate = nx.algorithms.matching.min_weight_matching(graph, maxcardinality=True)
    return mate

def eulerian_tour(mst, start_vertex):
    graph = nx.Graph(mst)
    euler_cycle = list(nx.eulerian_circuit(graph, source=start_vertex))
    return euler_cycle

def make_hamiltonian_cycle(euler_cycle):
    path = []
    visited = set()
    cost = 0
    for u, v in euler_cycle:
        if u not in visited:
            visited.add(u)
            path.append(u)
        if v not in visited:
            visited.add(v)
            path.append(v)
            cost += dist_matrix[u][v]
    # Add return to start
    path.append(path[0])
    cost += dist_based_graph[path[-2]][path[0]]  # cost from last to start
    return path, cost

# Step 1: Construct Distance based graph
dist_matrix = construct_graph()

# Step 2: Construct Minimum Spanning Tree (MST)
mst = find_minimum_spanning_tree(dist_matrix)

# Step 3: Find vertices with odd degree in the MST
odd_vertices = odd_degree_vertices(mst)

# Step 4: Find minimum cost perfect matching among the odd degree vertices
matching = minimum_weight_perfect_matching(mst, odd_vertices, dist_matrix)

# Step 5: Combine MST and matching into a single graph for Eulerian Tour
for u, v in matching:
    mst[u, v] += dist_matrix[u][v]
    mst[v, u] += dist_matrix[u][v]

# Step 6: Compute Eulerian tour from Eulerian graph
euler_cycle = eulerian_tour(mst, 0)

# Step 7: Convert Eulerian cycle to Hamiltonian cycle
tour, total_travel_cost = make_hamiltonian_cycle(euler_cycle)

# Output
print("Tour:", tour)
print("Total travel cost:", total_travel_detect)