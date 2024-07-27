import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_biconnected(graph, num_vertices):
    visited = [False] * num_vertices
    discovery = [float("Inf")] * num_vertices
    low = [float("Inf")] * num_resources
    parent = [-1] * num_vertices
    bridges = []
    articulation_points = []

    def bridge_util(u, visited, parent, low, discovery):
        children = 0
        visited[u] = True
        discovery[u] = low[u] = timer[0]
        timer[0] += 1
        
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                bridge_util(v, visited, parent, low, discovery)
                
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    articulation_points.append(u)
                if parent[u] != -1 and low[v] >= discovery[u]:
                    articulation_points.append(u)
                    
                if low[v] > discovery[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], discovery[v])

    timer = [0]
    for i in range(num_vertices):
        if not visited[i]:
            bridge_util(i, visited, parent, low, discovery)

    return len(articulation_points) == 0 and len(bridges) == 0

def approximate_BTSP(coordinates):
    num_cities = len(coordinates)
    sorted_edges = sorted([(euclidean_distance(coordinates[i], coordinates[j]), i, j) for i, j in itertools.combinations(range(num_cities), 2)], key=lambda x: x[0])
    
    E_BB = []
    graph = [[] for _ in range(num_cities)]
    
    def add_edge(u, v):
        graph[u].append(v)
        graph[v].append(u)
        
    for dist, u, v in sorted_edges:
        graph_backup = [list(adj) for adj in graph]
        add_edge(u, v)
        if is_biconnected(graph, num_cities):
            E_BB.append((dist, u, v))
        else:
            graph = graph_backup

    # Form a Hamiltonian cycle in the augmented biconnected graph
    visited = [False] * num_cities
    tour = []
    def euler_tour(v):
        for u in graph[v]:
            if (v, u) in E_BB or (u, v) in E_BB:
                if (v, u) in E_BB:
                    E_BB.remove((v, u))
                else:
                    E_BB.remove((u, v))
                euler_tour(u)
        tour.append(v)
        
    euler_tour(0)
    
    final_tour = []
    visited = [False] * num_cities
    for city in tour:
        if not visited[city]:
            final_tour.append(city)
            visited[city] = True
    final_tour.append(final_tour[0]) # Complete the cycle by returning to the start
    
    total_cost = sum([euclidean_distance(coordinates[final_tour[i]], coordinates[final_tour[i+1]]) for i in range(len(final_tour)-1)])
    max_distance = max([euclidean_distance(coordinates[final_tour[i]], coordinates[final_tour[i+1]]) for i in range(len(final_tour)-1)])
    
    return {
        "Tour": final_tour,
        "Total travel cost": total_cost,
        "Maximum distance between consecutive cities": max_distance
    }

# Define city coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

result = approximate_BTSP(cities)

print("Tour:", result["Tour"])
print("Total travel cost:", round(result["Total travel cost"], 2))
print("Maximum distance between consecutive cities:", round(result["Maximum distance between consecutive cities"], 2))