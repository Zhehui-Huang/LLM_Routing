import math
from itertools import combinations

# Define the cities and their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Calculate Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Generate all possible edges with their distances
edges = [(euclidean_distance(cities[i], cities[j]), i, j) for i in cities for j in cities if i < j]
edges.sort()  # sort edges by distance

# Helper functions for Kruskal's algorithm to ensure a biconnected graph
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

# Kruskal's MST modified to stop on biconnectivity
def kruskal_biconnected(nodes, edges):
    parent = {}
    rank = {}
    for node in nodes:
        parent[node] = node
        rank[node] = 0

    mst = []
    index = 0
    e = 0  # Count of edges in MST

    # Number of edges to be taken is equal to V-1
    while e < len(nodes) - 1:
        # Step 3: Pick the smallest edge. Check for cycle.
        if index >= len(edges):
            break
        w, u, v = edges[index]
        index += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            mst.append((w, u, v))
            union(parent, rank, x, y)

    # At this stage, mst contains the MST edges, we shall convert it into a chain
    if len(mst) < len(nodes) - 1:
        raise Exception("The MST does not connect all nodes.")

    return mst

# Getting the MST with the modified Kruskal's algorithm
mst_edges = kruskal_biconnected(list(cities.keys()), edges)

# Constructing graph from MST edges
import networkx as nx
graph = nx.Graph()
for w, u, v in mst_edges:
    graph.add_edge(u, v, weight=w)

# Finding a Hamiltonian cycle
tour = list(nx.algorithms.approximation.traveling_salesman_problem(graph, cycle=True, method='greedy'))

# Calculate total distance and maximum distance between consecutive cities
total_distance = 0
max_distance = 0
for i in range(len(tour)):
    if i == len(tour) - 1:
        dist = euclidean_distance(cities[tour[i]], cities[tour[0]])
    else:
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    total_distance += dist
    if dist > max_distance:
        max_distance = dist

# Ensure the tour starts and ends at the depot city 0
if tour[0] != 0:
    zero_index = tour.index(0)
    tour = tour[zero_index:] + tour[:zero_index]
tour.append(tour[0])  # make it a complete cycle

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")