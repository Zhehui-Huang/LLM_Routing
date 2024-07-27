import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Cities coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Calculate distances between all pairs of cities
def calculate_distances(cities):
    distances = {}
    for i in cities.keys():
        for j in cities.keys():
            if i != j:
                distances[(i, j)] = euclidean(cities[i], cities[j])
    return distances

distances = calculate_distances(cities)

# Sorting edges based on the distance
sorted_edges = sorted(distances.items(), key=lambda x: x[1])

# Union-Find data structure to check connectivity and cycles
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1

# Creating the bottleneck optimal biconnected subgraph
def find_bottleneck_subgraph(vertices, sorted_edges):
    uf = UnionFind(len(vertices))
    E_BB = set()
    for edge, dist in sorted_edges:
        if uf.find(edge[0]) != uf.find(edge[1]):
            uf.union(edge[0], edge[1])
            E_BB.add(edge)
            # Early stopping if all vertices are connected
            if len(E_BB) == len(vertices) - 1:
                break

    max_edge_cost = max(distances[e] for e in E_BB)
    return E_BB, max_edge_cost

# Step 1: Bottleneck-optimal biconnected subgraph
E_BB, max_edge_cost = find_bottleneck_subgraph(cities.keys(), sorted_edges)

# Step 2: Approximate a tour from E_BB
def find_approximate_tour(start, vertices, E_BB):
    # A spherical implementation might use nearest neighbor or minimum spanning tree approaches.
    # For simplicity, considering only direct edges available from E_BB
    current = start
    tour = [start]
    visited = {current}
    total_cost = 0
    max_leg_cost = 0
    while len(visited) < len(vertices):
        next_city = min((v for v in vertices if v not in visited and (current, v) in E_BB), key=lambda x: distances[(current, x)], default=None)
        if next_city is not None:
            tour.append(next_city)
            leg_cost = distances[(current, next_city)]
            max_leg_cost = max(max_leg_cost, leg_cost)
            total_cost += leg_cost
            visited.add(next_city)
            current = next_city
    # Closing the loop
    tour.append(start)
    total_cost += distances[(current, start)]
    max_leg_cost = max(max_leg_cost, distances[(current, start)])

    return tour, total_cost, max_leg_cost

# Output tour, total cost, and max distance between consecutive cities
tour, total_cost, max_leg_cost = find_approximate_tour(0, cities.keys(), E_BB)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_leg_cost}")