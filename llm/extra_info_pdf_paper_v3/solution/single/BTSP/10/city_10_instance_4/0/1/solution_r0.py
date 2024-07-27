import math
from scipy.spatial import distance_matrix
import numpy as np
from queue import PriorityQueue

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def prim_mst(num_cities, dist_matrix):
    # Initialize a Minimum Spanning Tree using Prim's algorithm
    mst_edges = []
    visited = [False] * num_cities
    min_edge = PriorityQueue()
    min_edge.put((0, 0))  # (cost, start_node)
    total_cost = 0

    while not min_edge.empty():
        cost, u = min_edge.get()
        if visited[u]:
            continue
        total_cost += cost
        visited[u] = True
        for v in range(num_cities):
            if not visited[v] and dist_matrix[u][v] > 0:
                min_edge.put((dist_matrix[u][v], v))

        for v in range(num_cities):
            if visited[v] and v != u:
                mst_edges.append((u, v, dist_matrix[u][v]))

    return mst_edges, total_cost

def create_eulerian_tour(mst, num_cities):
    adj_list = {i: [] for i in range(num_cities)}
    for u, v, _ in mst:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    start_vertex = 0
    stack = [start_vertex]
    path = []
    while stack:
        vertex = stack[-1]
        if adj_list[vertex]:
            next_vertex = adj_list[vertex].pop()
            adj_list[next_vertex].remove(vertex)
            stack.append(next_vertex)
        else:
            path.append(stack.pop())
    
    return path

def shortcut_path(path):
    visited = set()
    short_path = []
    for city in path:
        if city not in visited:
            visited.add(city)
            short_path.append(city)
    return short_path

cities = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9),
    (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

num_cities = len(cities)
dist_matrix = distance_matrix(cities, cities)

# Finding Minimum Spanning Tree:
mst_edges, _ = prim_mst(num_cities, dist_matrix)
euler_tour = create_eulerian_tour(mst_edges, num_cities)
hamiltonian_path = shortcut_path(euler_tour)
hamiltonian_path.append(hamiltonian_path[0])  # Return to start city.

# Calculate the total cost and the maximum distance between consecutive cities:
total_cost = sum(dist_matrix[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(len(hamiltonian_path)-1))
max_distance = max(dist_matrix[hamiltonian_path[i]][hamiltonian_path[i+1]] for i in range(len(hamiltonian_path)-1))

print(f"Tour: {hamiltonian_path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")