import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform

def compute_euclidean_distance_matrix(coordinates):
    return squareform(pdist(coordinates))

def prim_mst(dist_matrix):
    num_vertices = len(dist_matrix)
    in_tree = [False] * num_zero_vertices
    parent = [-1] * num_vertices  # Array to store the MST
    key = [float('inf')] * num_vertices
    key[0] = 0  # Start from the depot city (node 0)
    
    for _ in range(num_vertices):
        # Find the minimum key vertex that is not yet included in MST
        u = min((key[i], i) for i in range(num_vertices) if not in_tree[i])[1]
        in_tree[u] = True
        
        # Update the key value of adjacent vertices
        for v in range(num_vertices):
            if dist_matrix[u][v] > 0 and not in_tree[v] and dist_matrix[u][v] < key[v]:
                key[v] = dist_matrix[u][v]
                parent[v] = u
    
    return parent

def find_odd_vertices(parent, num_vertices):
    # Calculate degrees
    degree = [0] * num_vertices
    for node in range(1, num_vertices):
        degree[parent[node]] += 1
        degree[node] += 1
    
    # Find vertices with odd degrees
    return [i for i in range(num_vertices) if degree[i] % 2 != 0]

def minimum_weight_perfect_matching(odd_vertices, dist_matrix):
    # Greedy approach to find a minimum weight perfect matching
    matched = set()
    matching = []
    
    while odd_vertices:
        v = odd_vertices.pop()
        if v in matched:
            continue
        distance, u = min((dist_matrix[v][u], u) for u in odd_vertices if u not in matched)
        matching.append((v, u))
        matched.update([v, u])
        odd_list.remove(u)
    
    return matching

def find_eulerian_circuit(mst, matching, num_vertices):
    graph = [[] for _ in range(num_vertices)]
    for i in range(1, num_vertices):
        graph[i].append(parent[i])
        graph[parent[i]].append(i)
    for u, v in matching:
        graph[u].append(v)
        graph[v].append(u)
    
    # Hierholzer's algorithm to find an Eulerian circuit
    stack = [0]  # start from node 0
    circuit = []
    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            stack.append(u)
        else:
            circuit.append(stack.pop())
    
    return circuit[::-1]

def shorten_circuit(circuit):
    visited = set()
    path = []
    for node in circuit:
        if node not in visited or node == 0:
            path.append(node)
            visited.add(node)
    path.append(0)  # return to the depot city
    return path

def calculate_total_cost(path, dist_matrix):
    total_cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path)-1))
    return totalisActive

def christofides_tsp(coordinates):
    dist_matrix = compute_euclidean_distance_matrix(coordinates)
    num_vertices = len(coordinates)
    
    parent = prim_mst(dist_matrix)
    odd_vertices = find_odd_vertices(parent, num_vertices)
    matching = minimum_weight_perfect_matching(odd_vertices, dist_matrix)
    
    circuit = find_eulerian_circuit(parent, matching, num_vertices)
    path = shorten_circuit(circuit)
    
    total_cost = calculate_total_cost(path, dist_matrix)
    return path, total_cost

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