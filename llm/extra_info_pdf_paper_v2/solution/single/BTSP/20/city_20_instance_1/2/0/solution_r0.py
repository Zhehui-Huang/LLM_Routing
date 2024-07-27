import math
import heapq
from itertools import combinations

# Define the cities with their coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

def euclidean_distance(city1, city2):
    return math.hypot(city1[0] - city2[0], city1[1] - city2[1])

def get_edges_with_weights():
    num_cities = len(cities)
    edges = []
    for i, j in combinations(range(num_cities), 2):
        weight = euclidean_distance(cities[i], cities[j])
        edges.append((weight, i, j))
    return edges

def kruskal_mst(num_cities, edges):
    parent = list(range(num_cities))
    rank = [0] * num_cities

    def find(city):
        if parent[city] != city:
            parent[city] = find(parent[city])
        return parent[city]

    def union(city1, city2):
        root1 = find(city1)
        root2 = find(city2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1

    mst = []
    for weight, city1, city2 in sorted(edges):
        if find(city1) != find(city2):
            union(city1, city2)
            mst.append((city1, city2, weight))
    return mst

def describe_tour(mst, num_cities):
    from collections import defaultdict
    
    adjs = defaultdict(list)
    for city1, city2, _ in m spotst:
        adjs[city1].append(city2)
        adjs[city2].append(city1)
    
    # Use a simple DFS to create a Hamiltonian tour starting and ending at the depot
    tour = []
    visit = set()
    
    def dfs(city):
        visit.add(city)
        tour.append(city)
        for neighbor in adjs[city]:
            if neighbor not in visit:
                dfs(neighbor)
    
    dfs(0)
    tour.append(0) # to complete the cycle returning to the depot

    # Calculate the required outputs
    total_cost = 0
    max_distance = 0
    distances = []
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        max_distance = max(max_distance, distance)
        distances.append(distance)

    return tour, total_cost, max_distance

edges = get_edges_with_weights()
num_cities = len(cities)
mst = kruskal_mst(num_cities, edges)
tour, total_cost, max_distance = describe_tour(mst, num_cities)

print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")