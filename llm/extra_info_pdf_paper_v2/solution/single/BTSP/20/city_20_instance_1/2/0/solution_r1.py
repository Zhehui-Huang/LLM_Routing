import math
from itertools import combinations

# Define the cities with their coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def prim_minimum_spanning_tree(coords):
    num_cities = len(coords)
    edges = {i: [] for i in range(num_cities)}
    included = [False] * num_cities
    min_edge = [(float('inf'), -1)] * num_cities
    min_edge[0] = (0, 0)
    mst_cost = 0
    mst_edges = []

    for _ in range(num_cities):
        v = -1
        for i in range(num_cities):
            if not included[i] and (v == -1 or min_edge[i][0] < min_edge[v][0]):
                v = i
        if min_edge[v][0] == float('inf'):
            return None  # No MST exists if part of the graph is disconnected

        included[v] = True
        mst_cost += min_edge[v][0]
        if min_edge[v][1] != v:
            mst_edges.append((v, min_edge[v][1]))

        for to in range(num_cities):
            weight = euclidean_distance(coords[v], coords[to])
            if weight < min_edge[to][0] and not included[to]:
                min_edge[to] = (weight, v)
    
    return mst_edges, mst_cost

def find_tour(mst, start_node):
    from collections import defaultdict, deque

    adj_list = defaultdict(list)
    for edge in mst:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    # Find a Hamiltonian path using DFS
    path = []
    visited = set()
    def dfs(node):
        visited.add(node)
        path.append(node)
        if len(path) == len(cities):
            return True
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        path.pop()
        visited.remove(node)
        return False
    
    dfs(start_node)
    path.append(path[0])  # Complete the tour by returning to the start
    return path

def calculate_metrics(tour, cities):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

mst, _ = prim_minimum_spanning_tree(cities)
tour = find_tour(mst, 0)
total_cost, max_distance = calculate_metrics(tour, cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")