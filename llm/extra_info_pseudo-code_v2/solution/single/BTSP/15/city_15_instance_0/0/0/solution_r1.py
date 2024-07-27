import math
import itertools

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def find_tour(cities):
    num_cities = len(cities)
    distances = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]
    
    # Building initial edge list
    edges = sorted([(distances[i][j], i, j) for i in range(num_cities) for j in range(i+1, num_cities)], key=lambda x: x[0])
    
    # Kruskal's algorithm to ensure connectivity with minimum maximum edge (bottleneck)
    parent = list(range(num_cworkspacesities))
    rank = [0] * num_cities
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
    
    mst = []  # Minimum Spanning Tree storage
    for dist, i, j in edges:
        if find(i) != find(j):
            union(i, j)
            mst.append((i, j, dist))
    
    if len(mst) != num_cities - 1:
        raise ValueError("MST does not contain exactly n-1 edges")
    
    # Find an Eulerian tour in the MST, doubled to ensure all vertices can be reached at least twice
    # Convert tree to adjacency list
    adj_list = {i: [] for i in range(num_cities)}
    for i, j, _ in mst:
        adj_list[i].append(j)
        adj_list[j].append(i)
    
    # Hierholzer's algorithm to find an Eulerian circuit
    def find_euler_tour(u):
        tour = []
        stack = [u]
        while stack:
            v = stack[-1]
            if adj_list[v]:
                w = adj_list[v].pop()
                adj_list[w].remove(v)
                stack.append(w)
            else:
                tour.append(stack.pop())
        return tour[::-1]
    
    euler_tour = find_euler_tour(0)
    
    # Making the tour a valid Hamiltonian tour by visiting cities only once
    visited = [False] * num_cities
    hamiltonian_tour = []
    for city in euler_tour:
        if not visited[city]:
            hamiltonian_tour.append(city)
            visited[city] = True
    
    # Return to start
    hamiltonian_tour.append(hamiltonian_tour[0])
    
    # Calculate distances
    tour_distance = sum(distances[hamiltonian_tour[i]][hamiltonian_tour[i+1]] for i in range(len(hamiltonian_tour) - 1))
    max_edge = max(distances[hamiltonian_tour[i]][hamiltonian_tour[i+1]] for i in range(len(hamiltonian_tour) - 1))
    
    return {
        "Tour": hamiltonian_tour,
        "Total travel cost": tour_distance,
        "Maximum distance between consecutive cities": max_edge
    }

# Cities coordinates given in the task
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

result = find_tour(cities)

print("Tour:", result["Tour"])
print("Total travel cost:", round(result["Total travel cost"], 2))
print("Maximum distance between consecutive cities:", round(result["Maximum distance between consecutive cities"], 2))