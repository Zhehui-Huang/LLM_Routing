import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

def compute_euclidean_distance_matrix(coordinates):
    return squareform(pdist(coordinates))

def mst_prim(distance_matrix):
    num_vertices = len(distance_matrix)
    in_tree = [False] * num_vertices
    parent = [-1] * num_vertices
    key = [float('inf')] * num_vertices
    key[0] = 0
    
    for _ in range(num_vertices):
        u = min((key[v], v) for v in range(num_vertices) if not in_tree[v])[1]
        in_tree[u] = True
        for v in range(num_vertices):
            if distance_matrix[u][v] < key[v] and not in_tree[v]:
                key[v] = distance_matrix[u][v]
                parent[v] = u
    mst_edges = [(parent[i], i) for i in range(1, num_vertices) if parent[i] != -1]
    return mst_edges

def find_odd_vertices(mst_edges, num_vertices):
    degree = [0] * num_vertices
    for u, v in mst_edges:
        degree[u] += 1
        degree[v] += 1
    return [v for v, deg in enumerate(degree) if deg % 2 == 1]

def minimum_weight_perfect_matching(odd_vertices, distance_matrix):
    num_vertices = len(odd_vertices)
    if num_vertices <= 1:
        return []
    min_matching = []
    min_cost = float('inf')
    for vertices in combinations(odd_vertices, 2):
        cost = distance_matrix[vertices[0]][vertices[1]]
        current_matching = [(vertices[0], vertices[1])]
        remaining_vertices = list(set(odd_vertices) - set(vertices))
        current_cost = cost + sum(minimum_weight_perfect_matching(remaining_vertices, distance_matrix))
        if current_cost < min_cost:
            min_cost = current_cost
            min_matching = current_matching + minimum_weight_perfect_matching(remaining_vertices, distance_matrix)
    return min_matching

def find_eulerian_tour(edges, num_vertices):
    graph = [[] for _ in range(num_vertices)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    stack = [0]
    path = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())
    return path[::-1]

def shortcut_path(eulerian_tour):
    visited = set()
    path = []
    for vertex in eulerian_tour:
        if vertex not in visited or vertex == 0:
            path.append(vertex)
            visited.add(vertex)
    return path

def calculate_total_travel_cost(path, distance_matrix):
    return sum(distance_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

def christofides_tsp(coordinates):
    distance_matrix = compute_euclidean_distance_matrix(coordinates)
    num_vertices = len(coordinates)
    
    mst_edges = mst_prim(distance_matrix)
    odd_vertices = find_odd_vertices(mst_edges, num_vertices)
    matching_edges = minimum_weight_perfect_matching(odd_vertices, distance_matrix)
    
    edges = mst_edges + matching_edges
    eulerian_tour = find_eulerian_tour(edges, num_vertices)
    hamiltonian_path = shortcut_path(eulerian_tour)
    
    total_cost = calculate_total_travel_cost(hamiltonian_path + [0], distance_matrix)  # append depot to close the tour
    return hamiltonian_path + [0], total_cost   # ensure returning to the depot

# Sample coordinates
coordinates = [
    (79, 15),   # Depot city 0
    (79, 55),   # City 1
    (4, 80),    # City 2
    (65, 26),   # City 3
    (92, 9),    # City 4
    (83, 61),   # City 5
    (22, 21),   # City 6
    (97, 70),   # City 7
    (20, 99),   # City 8
    (66, 62)    # City 9
]

path, total_cost = christofides_tsp(coordinates)
print("Tour:", path)
print("Total travel cost:", total_cost)