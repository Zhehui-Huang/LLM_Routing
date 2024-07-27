import math
from itertools import permutations

# Given city coordinates with depots and others
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate edges and sort them by distance
edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])

# Utilitarian functions for checking connectivity and biconnectivity
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

# Building a biconnected graph using the edges
def build_biconnected_graph():
    parent = {i: i for i in cities}
    rank = {i: 0 for i in cities}
    bb_edges = []
    for (src, dest, weight) in edges:
        if find(parent, src) != find(parent, dest):
            union(parent, rank, src, dest)
            bb_edges.append((src, dest, weight))
            if len(bb_edges) >= len(cities):  # Sufficient edges to form a biconnected graph
                break
    return bb_edges

bb_graph = build_biconnected_graph()

# Finding routes and calculating bottleneck cost
def hamiltonian_path(bb_edges):
    adj_matrix = {i: [] for i in cities}
    for (src, dest, weight) in bb_edges:
        adj_matrix[src].append((dest, weight))
        adj_matrix[dest].append((src, weight))
        
    min_tour_cost = float('inf')
    min_tour = []
    max_dist = float('inf')
    
    for perm in permutations(range(1, len(cities))):  # Generate permutations leaving out the depot
        current_path = [0] + list(perm) + [0]
        current_cost = 0
        valid = True
        current_max_dist = 0
        
        for i in range(len(current_path) - 1):
            cost = euclidean_distance(cities[current_path[i]], cities[current_path[i + 1]])
            current_cost += cost
            current_max_dist = max(current_max_dist, cost)
            if not any(dest == current_path[i+1] for (dest, _) in adj_matrix[current_path[i]]):
                valid = False
                break

        if valid and current_cost < min_tour_cost:
            min_tour_cost = current_cost
            min_tour = current_path
            max_dist = current_max_dist
    
    return min_tour, min_tour_cost, max_dist

tour, total_cost, max_distance = hamiltonian_path(bb_graph)

# Output as per requirement format
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))