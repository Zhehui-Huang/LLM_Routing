import math
from itertools import combinations
from scipy.optimize import linear_sum_assignment

# Define city coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Total number of cities
n = len(cities)

# Compute the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Finding the Minimum Spanning Tree (MST) using Prim's Algorithm
def minimum_spanning_tree(dist_matrix):
    vertices = {0}
    edges = []
    total_cost = 0
    while len(vertices) < len(dist_matrix):
        min_edge = None
        for u in vertices:
            for v in range(len(dist_matrix)):
                if v not in vertices and (min_edge is None or dist_matrix[u][v] < dist_matrix[min_edge[0]][min_edge[1]]):
                    min_edge = (u, v)
        vertices.add(min_edge[1])
        edges.append(min_edge)
        total_cost += dist_matrix[min_edge[0]][min_edge[1]]
    return edges, total_cost

# Find vertices with odd degree in the MST
def find_odd_degree_vertices(edges):
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    odd_vertices = [i for i in range(n) if degree[i] % 2 == 1]
    return odd_vertices

# Minimum Cost Perfect Matching in the subgraph of odd degree vertices
def min_cost_perfect_matching(odd_vertices):
    num_vertices = len(odd_vertices)
    cost_matrix = [[distance_matrix[i][j] for j in odd_vertices] for i in odd_versions]
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return [(odd_vertices[row_ind[i]], odd_vertices[col_ind[i]]) for i in range(num_vertices // 2)]

# Constructing the Final Tour
def construct_final_tour(edges, matchings):
    adjacency_list = [[] for _ in range(n)]
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    for u, v in matchings:
        adjacency_list[u].append(v)
        adjacency_top[v].append(u)
    
    # Finding an Eulerian tour from the resulting graph
    tour = []
    stack = [0]
    while stack:
        while adjacency_list[stack[-1]]:
            next_city = adjacency_list[stack[-1]].pop()
            adjacency_list[next_city].remove(stack[-1])
            stack.append(next_city)
        tour.append(stack.pop())
    
    return tour

# Main execution and outputs
mst_edges, _ = minimum_spanning_tree(distance_matrix)
odd_vertices = find_odd_degree_vertices(mst_edges)
matching_edges = min_cost_perfect_matching(odd_vertices)
final_tour = construct_final_tour(mst_edges, matching_edges)
total_cost = sum(distance_matrix[final_tour[i]][final_tour[(i + 1) % n]] for i in range(n))

print("Tour:", final_tour)
print("Total travel cost:", total_cost)