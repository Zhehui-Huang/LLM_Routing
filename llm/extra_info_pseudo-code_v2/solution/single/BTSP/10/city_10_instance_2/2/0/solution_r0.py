import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Dictionary of city coordinates
city_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def construct_biconnected_graph(num_cities, city_coords):
    edges = [(euclidean_distance(city_coords[i], city_coords[j]), i, j) for i in range(num_cities) for j in range(i+1, num_cities)]
    edges.sort() 
    uf = {}
    
    def find(x):
        if uf[x] != x:
            uf[x] = find(uf[x])
        return uf[x]
    
    def union(x, y):
        uf.setdefault(x, x)
        uf.setdefault(y, y)
        uf[find(x)] = find(y)
    
    E_BB = []

    for w, i, j in edges:
        if find(i) != find(j):
            E_BB.append((w, i, j))
            union(i, j)
        if len(E_BB) == num_cities - 1:
            break
    
    return E_BB

def extract_tour(graph, num_cities):
    graph_edges = {i: [] for i in range(num_cities)}
    for w, i, j in graph:
        graph_edges[i].append((w, j))
        graph_edges[j].append((w, i))
    
    # Find Hamiltonian path using DFS that visits each city exactly once
    tour = []
    visited = set()
    
    def dfs(city):
        visited.add(city)
        tour.append(city)
        if len(tour) == num_cities and 0 in graph_edges[city]:
            tour.append(0)  # to complete the cycle
            return True

        for _, next_city in sorted(graphopology_edges[city], key=lambda x: x[0]):
            if next_city not in visited:
                if dfs(next_city):
                    return True
        tour.pop()
        visited.remove(city)
        return False

    dfs(0)
    return tour

# Construct the graph and find biconnected component
graph = construct_biconnected_graph(len(city_coordinates), city_coordinates)
tour = extract_tour(graph, len(city_coordinates))

# Calculate tour statistics
total_cost = 0
max_consecutive_distance = 0
for i in range(len(tour)-1):
    dist = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    total_cost += dist
    if dist > max_consecutive_distance:
        max_consecutive_distance = dist

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_consecutive_distance, 2))