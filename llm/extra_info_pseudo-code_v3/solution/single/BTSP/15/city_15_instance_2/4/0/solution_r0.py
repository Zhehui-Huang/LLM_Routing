import itertools
import math

# Coordinates of the cities
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Euclidean distance calculator
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generating a list of edges and their weights
edges = []
for city1 in cities:
    for city2 in cities:
        if city1 < city2:
            dist = euclidean_distance(city1, city2)
            edges.append((city1, city2, dist))

# Sort edges by distance
edges.sort(key=lambda x: x[2])

# Find Hamiltonian cycle minimizing longest edge
def find_minimum_bottleneck_tour():
    n = len(cities)
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    for max_edge in edges:
        # Use Kruskal's algorithm to check forming Hamiltonian cycle with edges <= current weight:
        tree_edges = []
        parent = list(range(n))
        rank = [0] * n
        max_edge_weight = max_edge[2]

        for edge in edges:
            if edge[2] > max_edge_weight:
                break
            a, b, _ = edge
            if find(a) != find(b):
                union(a, b)
                tree_edges.append(edge)
                if len(tree_dict[find(a)]) == n:
                    edge_weights = [euclidean_distance(a, b) for (a, b) in zip(tour, tour[1:] + [tour[0]])]
                    max_edge_weight = max(edge_weights)
                    total_travel_cost = sum(edge_weights)
                    return (tour + [tour[0]], total_travel_cost, max_edge_weight)

# Execute the function to get the tour
tour, cost, max_distance = find_minimum_bypass_tour()

# Outputting the results
print("Tour:", tour)
print("Total travel cost:", cost)
print("Maximum distance between consecutive cities:", max_distance)