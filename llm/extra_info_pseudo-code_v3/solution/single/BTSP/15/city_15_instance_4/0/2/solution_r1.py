import numpy as np
from itertools import combinations

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
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def find_bottleneck_tour(coords):
    n = len(coords)
    edges = [(calculate_distance(coords[i], coords[j]), i, j) for i, j in combinations(range(n), 2)]
    edges.sort()
    
    for d, i, j in edges:
        uf = UnionFind(n)
        
        # Create a subgraph with edges of distance <= d
        for dist, u, v in edges:
            if dist > d:
                break
            uf.union(u, v)
        
        # Check if all vertices are connected
        if len(set(uf.find(x) for x in range(n))) == 1:
            # Construct the tour based on the MST formed
            tour = [0]
            visited = [False] * n
            visited[0] = True
            current = 0
            max_distance = d
            total_distance = 0
            
            def find_next(city, visited):
                for dist, u, v in edges:
                    if dist > d:
                        break
                    if u == city and not visited[v]:
                        visited[v] = True
                        return v
                    if v == city and not visited[u]:
                        visited[u] = True
                        return u
                return None
            
            for _ in range(n - 1):
                next_city = find_next(current, visited)
                tour.append(next_city)
                total_distance += calculate_distance(coords[current], coords[next_city])
                current = next_city
            
            tour.append(0)  # Close the tour by returning to the depot
            total_distance += calculate_distance(coords[current], coords[0])
            return tour, total_distance, max_distance

    return [], 0, 0

coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

tour, total_cost, max_distance = find_bottleneck_tour(coords)
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")