import itertools
import math

# Calculating Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Find set representative
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# Union of two subsets
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

# Kruskal's algorithm to find MST
def kruskal(n, edges):
    result = []
    i, e = 0, 0
    parent = []
    rank = []
    edges = sorted(edges, key=lambda item: item[2])
    for node in range(n):
        parent.append(node)
        rank.append(0)
    while e < n - 1:
        if i >= len(edges):
            break
        u, v, w = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append((u, v, w))
            union(parent, rank, x, y)
    return result

def bottleneck_tsp(cities):
    n = len(cities)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(cities[i], cities[j])
            edges.append((i, j, distance))
    mst = kruskal(n, edges)
    max_edge_weight = max(weight for _, _, weight in mst)
    
    # Union-Find structure for bottleneck
    parent = list(range(n))
    rank = [0] * n
    for u, v, _ in mst:
        union(parent, rank, u, v)
        
    # Create tour from MST, visiting edges minimally
    tour = [0]  # Start at the depot
    visited = set(tour)
    def visit(city):
        if city in visited:
            return
        visited.add(city)
        tour.append(city)
        for next_city, _, _ in filter(lambda x: x[0] == city or x[1] == city, mst):
            other_city = next_city if next_city != city else x[0]
            visit(other_city)

    visit(0)
    tour.append(0)  # Return to depot
    total_distance = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    return {'Tour': tour, 'Total travel cost': total_distance, 'Maximum distance between consecutive cities': max_edge_weight}

# Define the cities (Node 0 is depot)
cities = [
    (50, 42),  # Depot
    (41, 1),
    (18, 46),
    (40, 98),
    (51, 69),
    (47, 39),
    (62, 26),
    (79, 31),
    (61, 90),
    (42, 49)
]

result = bottleneck_tsp(cities)
print("Tour:", result['Tour'])
print("Total travel cost:", result['Total travel survey'])
print("Maximum distance between consecutive cities:", result['Maximum distance between consecutive cities'])