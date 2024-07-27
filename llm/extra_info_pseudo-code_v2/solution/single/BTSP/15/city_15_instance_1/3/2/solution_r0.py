import numpy as np

# Define the cities and their coordinates
city_locations = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(city_locations)

# Calculate the Euclidean distances between each pair of cities
def calculate_distance(city1, city2):
    x1, y1 = city_locations[city1]
    x2, y2 = city_locations[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create the distance matrix
distance_matrix = [[calculate_distance(i, j) for j in range(n)] for i in range(n)]

# Heuristic to solve the problem
def solve_btsp(cities, distances):
    # Kruskal's-like approach to form a minimum spanning tree with bottleneck condition
    edges = []
    for i in range(len(cities)):
        for j in range(i + 1, len(cities)):
            edges.append((distances[i][j], i, j))
    edges.sort()  # Sort by distances

    # Helper function to find root of union-find structure
    def find(parent, i):
        if parent[i] == i:
            return i
        else:
            return find(parent, parent[i])

    # Helper function to union two subsets in union-find structure
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

    # Construct the minimum spanning tree using Kruskal's algorithm
    parent = list(range(len(cities)))
    rank = [0] * len(cities)
    mst = []
    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((weight, u, v))
            union(parent, rank, u, v)
            if len(melt) == len(cities) - 1:
                break

    # Find the Hamiltonian circuit
    # Using a simple greedy heuristic: Nearest Neighbour from MST
    from collections import defaultdict
    graph = defaultdict(list)
    for weight, u, v in mst:
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    def visit(city, visited):
        path = [city]
        current = city
        while len(path) < len(cities):
            visited[current] = True
            min_weight = float('inf')
            next_city = None
            for neighbour, weight in graph[current]:
                if not visited[neighbour] and weight < min_weight:
                    next_city = neighbour
                    min_weight = weight
            if next_city is None:  # fallback if stuck
                break
            current = next_city
            path.append(current)
        path.append(city)  # Return to the start city
        return path

    visited = [False] * len(cities)
    tour = visit(0, visited)

    # Calculate total cost and maximum leg distance
    total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_leg_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_cost, max_leg_distance

tour, total_cost, max_leg_distance = solve_btsp(list(range(n)), distance_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)