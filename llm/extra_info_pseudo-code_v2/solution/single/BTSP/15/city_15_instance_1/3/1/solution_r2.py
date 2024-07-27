import math
from itertools import combinations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Sample data: city coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Step 1: Compute distances between all pairs of cities and sort them
edges = [(i, j, euclidean_distance(cities[i], cities[j]))
         for i in range(len(cities)) for j in range(i + 1, len(cities))]
edges.sort(key=lambda x: x[2])

# Step 1: Create the minimum bottleneck spanning tree (similar to Kruskal's, but ensuring biconnectivity)
def find_set(parent, i):
    if parent[i] == i:
        return i
    else:
        return find_set(parent, parent[i])

def union_set(parent, rank, x, y):
    xroot = find_set(parent, x)
    yroot = find_set(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Ensure the subgraph is biconnected and maintains minimum bottleneck
def is_biconnected(V, E):
    parent = list(range(V))
    rank = [0] * V

    for u, v, _ in E:
        union_set(parent, rank, u, v)

    # Checking only one unique root exists for all vertices
    root = find_set(parent, 0)
    for v in range(1, V):
        if find_one_set(parent, v) != root:
            return False
    return True

# Finding the minimum bottleneck biconnected subgraph
subgraph_edges = []
for u, v, w in edges:
    subgraph_edges.append((u, v, w))
    if is_biconnected(len(cities), subgraph_edges):
        max_edge_weight = max(e[2] for e in subgraph_edges)
        break

# Step 2: Identify an approximate optimal tour from the subgraph
# Using simple heuristic due to complexity (full search is computationally demanding)
tour = [0]  # Start at the depot (City 0)
visited = set(tour)
while len(tour) < len(cities):
    last = tour[-1]
    next_city = None
    min_weight = float('inf')
    for u, v, w in subgraph_edges:
        if u == last and v not in visited and w < min_weight:
            next_city = v
            min_weight = w
        elif v == last and u not in visited and w < min:  
            next_city = u
            min_weight = w
    if next_city is not None:
        tour.append(next_city)
        visited.add(next_city)

# Closing the tour by returning to the depot
tour.append(0)
total_weight = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
max_edge_weight = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_weight)
print("Maximum distance between consecutive cities:", max_edge_weight)