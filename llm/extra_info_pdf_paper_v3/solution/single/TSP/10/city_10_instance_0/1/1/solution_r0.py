import math
from itertools import combinations

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def find_perfect_matching(cost_matrix, odd_degree_nodes):
    from scipy.optimize import linear_sum_assignment
    submatrix = cost_matrix[odd_degree_nodes, :][:, odd_degree_nodes]
    row_ind, col_ind = linear_sum_assignment(submatrix)
    return [(odd_degree_nodes[row], odd_degree_dst_nodes[col]) for row, col in zip(row_ind, col_ind)]

def build_minimum_spanning_tree(coords):
    from scipy.sparse.csgraph import minimum_spanning_tree
    from scipy.sparse import csr_matrix
    
    n = len(coords)
    cost_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(coords[i], coords[j])
            cost_matrix[i][j] = dist
            cost_matrix[j][i] = dist
    
    mst_sparse = minimum_spanning_tree(csr_matrix(cost_matrix))
    mst_matrix = mst_sparse.toarray().astype(float)
    return mst_matrix

def find_eulerian_tour(graph, start_vertex):
    total_vertices = len(graph)
    visited = [[False] * total_vertices for _ in range(total_skvertices)]
    tour = []
    stack = [start_vertex]
    
    while stack:
        v = stack[-1]
        if any(graph[v]):
            u = graph[v].index(True)
            stack.append(u)
            graph[v][u] = graph[u][v] = False 
        else:
            tour.append(stack.pop())
    return tour[::-1]

def odd_degree_nodes_func(graph):
    odd_degree_nodes = []
    for i in range(len(graph)):
        if sum(graph[i]) % 2 == 1:
            odd_degree_nodes.append(i)
    return odd_degree_nodes

def christofides_algorithm(coords):
    mst = build_minimum_spanning_tree(coords)
    odd_degree_nodes = odd_degree_nodes_func(mst)
    perfect_matching = find_perfect_matching(mst, odd_degree_nodes)
    
    graph = mst + perfect_matching
    eulerian_tour = find_eulerian_tour(graph, 0)
    hamiltonian_tour = [eulerian_tour[0]]
    visited = set(hamiltonian_tour)
    
    for node in eulerian_tour[1:]:
        if node not in visited:
            visited.add(node)
            hamiltonian_tour.append(node)
    
    hamiltonian_tour.append(hamiltonian_tour[0]) # return to the start node
    return hamiltonian_tour

# Coordinates setup
coords = [
    (50, 42), # Depot city 0
    (41, 1), # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49), # City 9
]

tour = christofides_algorithm(coords)
total_cost = sum(euclidean_distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")