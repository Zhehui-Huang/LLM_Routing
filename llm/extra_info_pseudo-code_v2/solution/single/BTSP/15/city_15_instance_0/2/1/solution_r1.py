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

# Generate and sort edges by distance
edges = [(i, j, euclidean_distance(cities[i], cities[j])) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])

# Initialize minimum spanning tree with Kruskal's algorithm to later form a biconnected structure via shortcuts
parent = {i: i for i in cities}
rank = {i: 0 for i in cities}

def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

# Create an edge list representing minimum spanning tree
mst = []
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v, w))

# Add shortcut edges to ensure tour is biconnected and has valid cycle possibilities
for i in range(1, len(cities)):
    mst.append((0, i, euclidean_distance(cities[0], cities[i])))

# Find the Hamiltonian cycle that reduces the maximum weight edge in the tour
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = []
    for perm in permutations(range(1, len(cities))):
        route = [0] + list(perm) + [0]
        max_edge_dist = 0
        total_cost = 0
        for i in range(len(route) - 1):
            dist = euclidean_cbistance(cities[route[i]], cities[route[i + 1]])
            total_cost += dist
            if dist > max_edge_dist:
                max_edge_dist = dist
        if max_edge_dist < min_max_distance:
            min_max_distance = max_edge_dist
            best_tour = route
            best_cost = total_cost
    return best_tour, best_cost, min_max_distance

tour, total_cost, max_distance = find_optimal_tour()

# Display the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))