import math
import numpy as np
from scipy.spatial.distance import pdist, squareform
from scipy.optimize import linear_sum_assignment

def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

# List of city coordinates
cities = [
    (16, 90),  # Depot City 0
    (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50),
    (35, 73), (42, 64), (64, 30), (70, 95),
    (29, 64), (32, 79)
]

# Calculate the distance matrix
distance_matrix = squareform(pdist(cities, metric='euclidean'))

# Find minimum spanning tree using Kruskal's algorithm with a union-find structure
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(n, distance_matrix):
    result = []  # Store the resultant MST
    i, e = 0, 0  # Initially there are 0 edges in MST
    
    # Creating edge list
    edges = [(i, j, distance_matrix[i][j]) for i in range(n) for j in range(i + 1, n)]
    edges = sorted(edges, key=lambda item: item[2])
    
    parent = []; rank = []
    
    for node in range(n):
        parent.append(node)
        rank.append(0)
    
    while e < n - 1:
        u, v, w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            e = e + 1
            result.append((u, v))
            union(parent, rank, x, y)
    
    return result

mst_edges = kruskal(len(cities), distance_matrix)

# Odd degree node collection
degree_count = [0] * len(cities)
for u, v in mst_edges:
    degree_count[u] += 1
    degree_count[v] += 1
    
odd_degree_nodes = [i for i in range(len(cities)) if degree_count[i] % 2 != 0]

# Minimum-weight perfect matching for odd-degree nodes
subgraph = distance_matrix[np.ix_(odd_degree_nodes, odd_degree_nodes)]
row_ind, col_ind = linear_sum_assignment(subgraph)

# Add the edges to the MST
mst_adj_list = {key: [] for key in range(len(cities))}
for u, v in mst_edges:
    mst_adj_list[u].append(v)
    mst_adj_list[v].append(u)

for i, j in zip(row_ind, col_ind):
    if i != j:
        u, v = odd_degree_nodes[i], odd_degree_nodes[j]
        mst_adj_list[u].append(v)
        mst_adj_list[v].append(u)

# Finding an Eulerian tour using Hierholzer's algorithm
def eulerian_tour(start, adj_list):
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        if adj_list[v]:
            u = adj_list[v].pop()
            adj_list[u].remove(v)  # remove the opposite edge
            stack.append(u)
        else:
            path.append(stack.pop())
    return path

# Create a duplicate list for removal of edges
mst_adj_list_copy = {u: v[:] for u, v in mst_adj_list.items()}
tour = eulerian_tour(0, mst_adj_list_copy)

# Remove repeated nodes to create a Hamiltonian cycle
visited = set()
final_tour = []
for city in tour:
    if city not in visited or city == 0:
        final_tour.append(city)
        visited.add(city)

# Calculate the tour cost
total_cost = sum(distance_matrix[final_tour[i], final_tour[i+1]] for i in range(len(final_tour)-1))

# Output results
print("Tour:", final_tour)
print("Total travel cost:", total_cost)