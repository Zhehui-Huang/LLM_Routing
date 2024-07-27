import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

def tsp_heuristic(cities):
    coordinates = np.array(cities)
    n = len(coordinates)
    dist_matrix = distance_matrix(coordinates, coordinates)

    # Minimum Spanning Tree using Prim's algorithm
    parent = [-1] * n
    key = [float('inf')] * n
    mst_set = [False] * n
    key[0] = 0

    for count in range(n):
        u = np.argmin(key)
        mst_set[u] = True
        
        for v in range(n):
            if dist_matrix[u][v] > 0 and mst_set[v] == False and key[v] > dist_matrix[u][v]:
                key[v] = dist_matrix[u][v]
                parent[v] = u

    # Find vertices of odd degree in MST
    degrees = [0] * n
    for i in range(1, n):
        degrees[i] += 1
        degrees[parent[i]] += 1

    odd_vertices = [i for i in range(n) if degrees[i] % 2 != 0]

    # Minimum cost perfect matching
    N = len(odd_vertices)
    cost = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            cost[i][j] = dist_matrix[odd_vertices[i]][odd_vertices[j]]

    row_ind, col_ind = linear_sum_assignment(cost)
    matching = []
    for i in range(N):
        matching.append((odd_vertices[row_ind[i]], odd_vertices[col_ind[i]]))

    # Building the Eulerian circuit
    adj_list = [[] for _ in range(n)]
    for i in range(1, n):
        adj_list[parent[i]].append(i)
        adj_list[i].append(parent[i])

    for u, v in matching:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Hierholzer's algorithm to find Eulerian tour
    def find_eulerian_tour(u):
        stack = [u]
        path = []
        while stack:
            u = stack[-1]
            if adj_list[u]:
                v = adj_list[u].pop()
                adj_list[v].remove(u)
                stack.append(v)
            else:
                path.append(stack.pop())
        return path

    # Starting at the depot city
    eulerian_tour = find_eulerian_tour(0)

    # Remove duplicates to form a Hamiltonian circuit
    visited = set()
    tour = []
    for vertex in eulerian_tour:
        if vertex not in visited:
            visited.add(vertex)
            tour.append(vertex)
    if tour[0] != tour[-1]:
        tour.append(tour[0])

    # Compute total travel cost
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return tour, total_cost

# Define cities
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

tour, total_cost = tsp_heuristic(cities)

print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")