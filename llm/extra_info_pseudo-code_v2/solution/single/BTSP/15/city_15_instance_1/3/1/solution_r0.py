import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def get_all_edges(cities):
    n = len(cities)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((dist, i, j))
    edges.sort()
    return edges

def check_biconnected(V, E_BB, start):
    from collections import defaultdict, deque
  
    adj = defaultdict(set)
    for dist, u, v in E_BB:
        adj[u].add(v)
        adj[v].add(u)

    def bfs(source):
        queue = deque([source])
        visited = set([source])
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return visited
    
    # Check connectivity
    visited = bfs(start)
    if len(visited) != V:
        return False
    
    # Check for biconnectivity via bridge finding
    def find_bridges():
        ids = [0] * V
        low = [0] * V
        visited = [False] * V
        
        def dfs(at, parent, bridges, id_counter):
            visited[at] = True
            low[at] = ids[at] = id_counter[0]
            id_counter[0] += 1
            
            for to in adj[at]:
                if to == parent:
                    continue
                if not visited[to]:
                    dfs(to, at, bridges, id_counter)
                    low[at] = min(low[at], low[to])
                    if ids[at] < low[to]:
                        bridges.append((at, to))
                else:
                    low[at] = min(low[at], ids[to])
        
        bridges = []
        for i in range(V):
            if not visited[i]:
                dfs(i, -1, bridges, [0])
        
        return len(bridges) == 0

    return find_bridges()      

def heuristic_algorithm(cities):
    # Step 0
    edges = get_all_edges(cities)
    E_BB = []

    # Step 1 and Step 2
    for edge in edges:
        E_BB.append(edge)
        if check_biconnected(len(cities), E_BB, 0):
            c_BB = max(dist for dist, _, _ in E_BB)
            break

    # Step 1 - Tour identification: use permutations to find a feasible hamiltonian path on G^2 of E_BB
    # Since G^2 is not given, trying to use the original set with its connectivity
    min_tour = []
    min_cost = float('inf')
    min_max_edge = float('inf')
    
    indices = list(range(len(cities)))
    for perm in permutations(indices):
        if perm[0] == 0:  # start from the depot city
            valid = True
            max_edge = 0
            total_cost = 0
            for i in range(1, len(perm)):
                dist = euclidean_distance(cities[perm[i-1]], cities[perm[i]])
                total_cost += dist
                max_edge = max(max_edge, dist)
            dist = euclidean_distance(cities[perm[-1]], cities[perm[0]])
            total_cost += dist
            max_edge = max(max_edge, dist)
            
            if max_edge < min_max_edge:
                min_max_edge = max_edge
                min_cost = total_cost
                min_tour = list(perm) + [perm[0]]

    return {'tour': min_tour, 'total_travel_cost': min_cost, 'maximum_distance_between_consecutive_cities': min_max_edge}

# Cities coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

result = heuristic_algorithm(cities)
print("Tour:", result['tour'])
print("Total travel cost:", result['total_travel_ctbr>Cost'])
print("Maximum distance between consecutive cities:", result['maximum_distance_between_consecutive_cities'])