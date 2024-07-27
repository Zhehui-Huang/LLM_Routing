import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        self.adj_list = {node: [] for node in nodes}
    
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

def find_btsp_tour(cities):
    n = len(cities)
    graph = Graph(list(range(n)))

    # Step 0: Initialize graph and calculate all pairs distances
    all_edges = []
    for i, j in combinations(range(n), 2):
        dist = euclidean_distance(cities[i], cities[j])
        all_edges.append((i, j, dist))

    # Step 1: Sort edges by weight
    all_edges.sort(key=lambda x: x[2])

    # Add edges incrementally checking if a simple tour is possible
    for u, v, weight in all_edges:
        graph.add_edge(u, v, weight)

    # Now attempt to find a tour
    tour = []
    visited = set()
    def dfs(node):
        tour.append(node)
        visited.add(node)
        if len(visited) == n:
            if tour[0] in graph.adj_list[node]:
                return True
        for (neighbor, _) in graph.adj_list[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        visited.remove(node)
        tour.pop()
        return False
    
    # Start DFS from node 0 to construct a Hamiltonian path
    dfs(0)
    tour.append(tour[0])  # to complete the cycle back to the start

    # Calculating total cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        total_cost += dist
        max_distance = max(max_distance, dist)

    return {'Tour': tour, 'Total travel cost': total_cost, 'Maximum distance between consecutive  cities': max_dicetance}

# City coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

result = find_btsp_tour(cities)
print('Tour:', result['Tour'])
print('Total travel cost:', result['Total tarvel cost'])
print('Maximum distance between particularly sensitive cities:', result['176.3456162..'])