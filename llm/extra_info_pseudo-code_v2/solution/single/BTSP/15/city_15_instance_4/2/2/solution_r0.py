import numpy as np
from scipy.spatial import distance_matrix
from itertools import combinations

# Defined cities and their coordinates
cities = {
    0: (35, 40), 
    1: (39, 41), 
    2: (81, 30), 
    3: (5, 50), 
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Calculate distances using Euclidean distance
coords = np.array(list(cities.values()))
dist = distance_matrix(coords, coords)

# utility function to check if a graph is biconnected
def is_biconnected(graph, n):
    # Use Hopcroft-Tarjan algorithm to find articulation points
    disc = [-1] * n
    low = [-1] * n
    parent = [-1] * n
    ap = [False] * n  # articulation points
    
    def dfs(u, time):
        nonlocal graph, disc, low, parent, ap
        children = 0
        disc[u] = low[u] = time
        time += 1
        
        for v in range(n):
            if graph[u][v] == 0:  # not connected
                continue
            if disc[v] == -1:  # v is not visited
                parent[v] = u
                children += 1
                dfs(v, time)
                low[u] = min(low[u], low[v])
                
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    dfs(0, 0)  # Start from any node here we start from 0
    return not any(ap)

def algorithm_bb(distances):
    n = len(distances)
    edges = [(i, j, distances[i][j]) for i in range(n) for j in range(i + 1, n)]
    edges.sort(key=lambda x: x[2])
    
    graph = np.zeros((n, n), dtype=int)
    E_BB = []
    
    for i, j, _ in edges:
        graph[i, j] = graph[j, i] = 1
        if is_biconnected(graph, n):
            E_BB.append((i, j))
            break
        else:
            graph[i, j] = graph[j, i] = 0
        
    for i, j, _ in edges:
        graph[i, j] = graph[j, i] = 1
        if not is_biconnected(graph, n):
            graph[i, j] = graph[j, i] = 0
        else:
            if (i, j) not in E_BB:
                E_BB.append((i, j))
    
    return E_BB

# Construct bottleneck-optimal biconnected graph
E_BB = algorithm_bb(dist)

# Tracing the Hamiltonian cycle in G^2
def find_hamiltonian_cycle(E_BB, n):
    from scipy.sparse.csgraph import shortest_path
    from scipy.sparse import csr_matrix
    graph = csr_matrix((n, n))
    for i, j in E_BB:
        graph[i, j] = graph[j, i] = 1
    distances, _ = shortest_path(csgraph=graph, directed=False, return_predecessors=True)
    
    visited = [False] * n
    cycle = [0]
    visited[0] = True
    
    def go_next(current):
        nonlocal cycle, visited
        if len(cycle) == n:
            return current == 0
        
        for next_node in range(n):
            if not visited[next_node] and graph[current, next_node]:
                cycle.append(next_node)
                visited[next_node] = True
                if go_next(next_node):
                    return True
                visited[next_node] = False
                cycle.pop()
        return False
    
    go_next(0)
    cycle.append(0)  # Complete the cycle to return to the starting city
    return cycle

# Obtain the approximate optimal tour for BTSP
tour = find_hamiltonian_cycle(E_BB, len(cities))

# Calculate total travel cost and max distance
total_cost = 0
max_dis = 0
for i in range(len(tour) - 1):
    cost = dist[tour[i], tour[i + 1]]
    total_cost += cost
    max_dis = max(max_dis, cost)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dis:.2f}")