import math
import itertools
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree, depth_first_order

# City coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Create distance matrix
n = len(cities)
dist_matrix = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Function to construct a Minimum Spanning Tree using Prim's algorithm adapted for TSP
def get_mst_prim(dist_matrix):
    num_vertices = len(dist_matrix)
    selected = [False] * num_vertices
    min_edge = [(float('inf'), -1)] * num_vertices  # (cost, from_node)
    min_edge[0] = (0, 0)  # start from node 0
    cost = 0
    mst_edges = []

    for _ in range(num_vertices):
        # Select the vertex with the smallest edge
        u = min((e, idx) for idx, e in enumerate(min_edge) if not selected[idx])[1]
        cost += min_edge[u][0]
        selected[u] = True

        # Add edge to MST
        if min_edge[u][1] != u:
            mst_edges.append((min_edge[u][1], u))

        for v in range(num_vertices):
            if dist_matrix[u][v] < min_edge[v][0] and not selected[v]:
                min_edge[v] = (dist_matrix[u][v], u)

    return mst_edges, cost

# Function to find odd degree vertices in MST
def get_odd_degree_vertices(mst_edges, num_vertices):
    degree = [0] * num_flags
    for u, v in mst_edges:
        degree[u] += 1
        degree[v] += 1
    return [i for i in range(num_vertices) if degree[i] % 2 == 1]

# Function to find minimum cost perfect matching on odd-degree vertices
def min_cost_perfect_matching(odd_vertices, dist_matrix):
    num_vertices = len(odd_vertices)
    if num_vertices <= 1:
        return [], 0
    # Solve as a minimum weight perfect matching problem
    # Formulate problem in terms compatible with optimization solver or use existing algorithm/libraries

    # Mock solution
    return [(odd_vertices[i], odd_vertices[i+1]) for i in range(0, num_vertices-1, 2)], 100  # Dummy edge list and cost

# Use the helper functions to solve TSP approximate solution based on Heuristic
mst_edges, mst_cost = get_mst_prim(dist_matrix)
odd_vertices = get_odd_degree_vertices(mst_edges, n)
matching_edges, matching_cost = min_cost_perfect_matching(odd_vertices, dist_matrix)

# Construct Eulerian graph by combining MST and MCPM
eulerian_graph_edges = mst_edges + matching_edges

# Convert Eulerian graph to Hamiltonian path (shortcutting technique)
tour = [0]
visited = set()
visited.add(0)

def dfs(current_vertex):
    for edge in eulerian_graph_edges:
        if edge[0] == current_vertex and edge[1] not in visited:
            tour.append(edge[1])
            visited.add(edge[1])
            dfs(edge[1])
        elif edge[1] == current_vertex and edge[0] not in visited:
            tour.append(edge[0])
            visited.add(edge[0])
            dfs(edge[0])

dfs(0)

tour.append(0)  # Return to depot

# Compute the total travel cost of the tour
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)