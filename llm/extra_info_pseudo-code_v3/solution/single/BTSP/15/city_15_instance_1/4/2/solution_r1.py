import math

# Define city coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Get all edges in form of (i, j, distance)
def get_edges():
    edges = []
    num_cities = len(cities)
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = distance(cities[i], cities[j])
            # Create edge in both directions since it's an undirected graph
            edges.append((i, j, dist))
            edges.append((j, i, dist))
    edges.sort(key=lambda x: x[2])  # Sort edges by length
    return edges

def find_tour():
    num_cities = len(cities)
    edges = get_edges()
    
    # Using a disjoint-set (Union-Find) structure to detect cycles efficiently
    parent = list(range(num_cities))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
            return True
        return False
    
    min_max_distance = float('inf')
    best_tour = []

    # Incrementally check increasing edge lengths
    for max_edge_length in sorted(set(e[2] for e in edges)):
        subgraph_edges = [(u, v) for u, v, d in edges if d <= max_edge_length]
        parent = list(range(num_cities))  # reset union-find
        
        graph = [[] for _ in range(num_cities)]
        for u, v in subgraph_edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Try to find a Hamiltonian cycle starting from node 0
        path = []
        visited = set()

        def dfs(node):
            visited.add(node)
            path.append(node)
            if len(path) == num_cities:
                if 0 in graph[node]:  # Complete cycle
                    path.append(0)
                    max_dist = max([distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1)])
                    nonlocal min_max_distance, best_tour
                    if max_dist < min_max_distance:
                        min_max_distance = max_dist
                        best_tour = path[:]
                    path.pop()
                    visited.remove(node)
                    path.pop()
                    return
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            visited.remove(node)
            if path:
                path.pop()

        dfs(0)

        if best_tour:
            # Calculate the total cost of the best tour found
            total_distance = sum(distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour)-1))
            return best_tour, total_distance, min_max_distance

# Execute the find_tour function to solve the problem
result = find_tour()

if result:
    tour, total_cost, max_distance = result
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No valid tour found.")