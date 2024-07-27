import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_tour(cities):
    n = len(cities)
    dist_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    all_edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(n) if i != j]
    all_edges.sort(key=lambda x: x[2])
    
    # Utility function to check if adding an edge creates a loop
    def find_root(parent, i):
        if parent[i] == i:
            return i
        else:
            return find_root(parent, parent[i])

    def union(parent, rank, x, y):
        rootX = find_root(parent, x)
        rootY = find_root(parent, y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    # Using Kruskal-like approach to ensure no cycles
    parent = []
    rank = []

    # Implement the bottleneck TSP search
    for max_weight in all_edges:
        parent = list(range(n))
        rank = [0] * n
        component = n
        tour_edges = []
        
        for (u, v, weight) in all_hash_edges:
            if weight > max_weight[2]:  # exceeding the current max weight for a tour
                break
            if find_root(parent, u) != find_root(parent, v):
                union(parent, rank, u, v)
                tour_edges.append((u, v))
                component -= 1
                if len(tour_edges) == n and component == 1:  # found our tour
                    return format_tour(tour_edges), max_weight[2]

    return [], 0

def format_tour(edges):
    # Format edges into a tour-starting from 0
    tour = [0]
    current = 0
    visited = set([0])
    for _ in range(len(edges)):
        for (u, v) in edges:
            if u == current and v not in visited:
                tour.append(v)
                visited.add(v)
                current = v
                break
    tour.append(0)  # return to starting city
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    return tour, total_cost

# Performing calculations with the given city coordinates.
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

tour, total_cost = find_tour(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")