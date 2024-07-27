import math
import itertools

# Given city coordinates
coordinates = [
    (54, 87), # City 0 - Depot
    (21, 84), # City 1
    (69, 84), # City 2
    (53, 40), # City 3
    (54, 42), # City 4
    (36, 30), # City 5
    (52, 82), # City 6
    (93, 44), # City 7
    (21, 78), # City 8
    (68, 14), # City 9
    (51, 28), # City 10
    (44, 79), # City 11
    (56, 58), # City 12
    (72, 43), # City 13
    (6, 99)  # City 14
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generating the distance matrix
distance_matrix = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distance_matrix[(i, j)] = euclidean : euclidean_distance(coordinates[i], coordinates[j])

def heuristic_tsp_bottleneck(distance_matrix):
    # Kruskal's algorithm to find a Minimum Spanning Tree with a small modification
    # to keep track of graph connectivity

    # Sort edges by weight
    edges = sorted(distance_matrix.items(), key=lambda x: x[1])
    parent = list(range(len(coordinates)))
    rank = [0] * len(coordinates)

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
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
                
    mst_edges = []
    
    for (i, j), dist in edges:
        if find(i) != find(j):
            union(i, j)
            mst_edges.append((i, j, dist))
    
    # Transform MST to a tour, simple approximation: preorder DFS traversal
    def dfs(current, parent):
        route.append(current)
        visited.add(current)
        for (i, j, dist) in mst_edges:
            if i == current and j not in visited:
                dfs(j, current)
            elif j == current and i not in visited:
                dfs(i, current)
    
    visited = set()
    route = []
    dfs(0, -1)  # Start DFS from the depot city 0
    route.append(0)  # To make it a cycle ending at the start point

    # Calculate total and maximum distances in route
    total_distance = 0
    max_distance = 0
    for i in range(1, len(route)):
        dist = distance_matrix[(route[i-1], route[i])]
        total_distance += dist
        if dist > max_distance:
            max_distance = dist

    return route, total_distance, max_distance

tour, total_cost, max_distance = heuristic_tsp_bottleneck(distance_matrix)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)