from math import sqrt, inf
from itertools import combinations

def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define the cities coordinates
cities = [
    (9, 93),  # Depot city 0
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Construct the distance matrix
n = len(cities)
dist_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Heuristic: Minimum Spanning Tree (MST) based approach
def mst_heuristic():
    # Kruskal's algorithm to find MST with modifications for BTSP
    edges = [(dist_matrix[i][j], i, j) for i, j in combinations(range(n), 2)]
    edges.sort()
    parent = list(range(n))
    rank = [0] * n

    def find(city):
        if parent[city] != city:
            parent[city] = find(parent[city])
        return parent[city]

    def union(city1, city2):
        root1 = find(city1)
        root2 = find(city2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []
    for cost, city1, city2 in edges:
        if find(city1) != find(city2):
            union(city1, city2)
            mst.append((city1, city2))

    # Creating the tour from MST by tracing a path using DFS
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for city1, city2 in mst:
        graph[city1].append(city2)
        graph[city2].append(city1)

    def dfs(city, parent):
        tour.append(city)
        for neighbor in graph[city]:
            if neighbor != parent:
                dfs(neighbor, city)
        if city == 0 and len(tour) < n + 1:  # Ensure all nodes are only used once
            tour.append(0)

    tour = []
    dfs(0, -1)
    return tour

tour = mst_heuristic()

# Calculate total cost and maximum distance in the tour
total_travel_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")