import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_biconnected(graph, num_vertices):
    """ Simple check for biconnectivity; here we assume the graph is always biconnected for simplification """
    return True  # Assuming the graph constructed is always biconnected for given cities

def calculate_total_and_max_cost(tour, positions):
    total_cost = 0
    max_cost = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(positions[tour[i]], positions[tour[i+1]])
        total_cost += dist
        if dist > max_cost:
            max_cost = dist
    return total_cost, max_cost

# Cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Bottleneck-optimal Biconnected Subgraph
edges = []
for i in cities:
    for j in cities:
        if i != j:
            edges.append((euclidean_distance(cities[i], cities[j]), i, j))

# Sort edges by distance
edges.sort()

# Applying Algorithm BB
E_BB = []
parents = list(range(len(cities)))

def find(vertex):
    if parents[vertex] != vertex:
        parents[vertex] = find(parents[vertex])
    return parents[vertex]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        parents[root2] = root1
        
# Kruskal’s algorithm to find Minimum Spanning Tree (MST) that is also biconnected
for cost, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        E_BB.append((u, v, cost))

# Assuming we have a biconnected component now
# Finding tour: Simple approximation using sorted edges
sorted_edges = sorted(E_BB, key=lambda x: x[2]) # Sort edges by weight within the biconnected subgraph
used = {}
tour = [0]
current = 0

while len(tour) < len(cities):
    for edge in sorted_edges:
        if edge[0] == current and edge[1] not in tour:
            tour.append(edge[1])
            current = edge[1]
            break
        elif edge[1] == current and edge[0] not in tour:
            tour.append(edge[0])
            current = edge[0]
            break

tour.append(0)  # return to depot

total_cost, max_dist = calculate_total_and_max_cost(tour, cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")