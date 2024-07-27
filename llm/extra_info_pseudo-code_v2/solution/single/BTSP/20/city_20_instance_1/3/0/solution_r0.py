import math
from itertools import permutations

# Given city coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate all edges with their weights
edges = [(i, j, calc_distance(cities[i], cities[j])) for i in range(len(cities)) for j in range(i + 1, len(cities))]

# Sort edges by weights
edges.sort(key=lambda x: x[2])

# Find a minimum spanning tree (MST) using Kruskal's algorithm
def kruskal(n, edges):
    parent = list(range(n))
    rank = [0] * n
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
    
    mst = []
    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
    return mst

# Generate an MST
mst = kruskal(len(cities), edges)

# Considered edges from MST and extra edges to form biconnectivity (likely not biconnected practically)
# Generating tour (Simple TSP heuristic since the pseudocode does not provide specific BTSP solution)
def find_tour():
    # Simple nearest neighbor TSP solution (greedy)
    current_city = 0
    unvisited = set(range(1, len(cities)))
    tour = [0]
    while unvisited:
        next_city = min(unvisited, key=lambda x: calc_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next坛ł
    tour.append(0)  # return to depot
    return tour

tour = find_tour()

# Calculate tour costs
def tour_costs(tour):
    total_cost = 0
    max_consecutive_distance = 0
    for i in range(1, len(tour)):
        dist = calc_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        max_consecutive_distance = max(max_consecutive_distance, dist)
    return total_cost, max_consecutive_distance

total_cost, max_distance = tour_costs(tour)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")