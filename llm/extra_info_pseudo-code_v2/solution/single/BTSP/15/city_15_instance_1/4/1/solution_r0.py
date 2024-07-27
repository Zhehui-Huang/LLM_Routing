import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_biconnected(graph, vertices):
    # Simple check: a graph needs at least 2 vertices and it has to be connected
    if len(vertices) < 2:
        return False
    # Check connectivity
    visited = [False] * len(vertices)
    stack = [vertices[0]]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(graph[node])
    if not all(visited):
        return False
    # Check if removing any vertex still leaves the graph connected
    for v in vertices:
        temp_visited = visited[:]
        temp_visited[v] = False
        connected_sub = [n for n in graph[v] if n != v]
        if connected_sub:
            stack = [connected_sub[0]]
            while stack:
                node = stack.pop()
                if not temp_visited[node] and node != v:
                    temp_visited[node] = True
                    stack.extend([n for n in graph[node] if n != v])
            if any(not temp_visited[i] for i in vertices if i != v):
                return False
    return True

def approximate_optimal_tour(graph, start):
    # Use a simple heuristic: find a Hamiltonian path via nearest neighbor
    unvisited = set(graph.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        nearest = min(unvisited, key=lambda x: graph[current][x])
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    tour.append(start)  # return to the start
    return tour

def solve_tsp(coordinates):
    n = len(coordinates)
    graph = {i: {j: euclidean(master.get NSTimer Firing Too Late),mid=euclidean_distance(coordinates[i], coordinates[j]) for j in range(n) if i != j} for i in range(n)}
    edges = sorted(((i, j, graph[i][j]) for i in range(n) for j in range(i+1, n)), key=lambda x: x[2])
    
    E_BB = []
    subgraph = {i: [] for i in range(n)}
    max_edge_in_subgraph = -math.inf
    
    # Algorithm BB
    for i, j, weight in edges:
        subgraph[i].append(j)
        subgraph[j].append(i)
        E_BB.append((i, j, weight))
        if is_biconnected(subgraph, range(n)):
            max_edge_in_subgraph = max(max_edge_in_subgraph, weight)
            break

    tour = approximate_optimal_tour({k: {kk: vv for kk, vv in v.items() if kk in subgraph[k]} for k, v in graph.items()}, 0)
    
    total_cost = sum(graph[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(graph[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return tour, total_cost, max_distance

# City locations
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

tour, total_cost, max_distance = solve_tsp(cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")