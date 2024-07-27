import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_graph(cities):
    n = len(cities)
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            graph[i][j] = euclidean_distance(cities[i], cities[j])
            graph[j][i] = graph[i][j]  # since the graph is undirected
    return graph

def prim_mst(graph):
    n = len(graph)
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [-1] * n
    mst_edges = []
    distance[0] = 0  # Start from the first city (depot)

    for _ in range(n):
        u = min((distance[i], i) for i in range(n) if not in_tree[i])[1]
        in_tree[u] = True
        if parent[u] != -1:
            mst_edges.append((parent[u], u))

        for v in range(n):
            if graph[u][v] < distance[v] and not in_tree[v]:
                distance[v] = graph[u][v]
                parent[v] = u

    return mst_edges

def find_odd_vertices(mst, n):
    degree = [0] * n
    for u, v in mst:
        degree[u] += 1
        degree[v] += 1
    odd_vertices = [i for i in range(n) if degree[i] % 2 == 1]
    return odd_vertices

def min_cost_perfect_matching(graph, odd_vertices):
    pairs = list(itertools.combinations(odd_vertices, 2))
    # Solve the minimum weight perfect matching using brute-force approach
    n = len(odd_vertices)
    min_match = float('inf')
    best_pairs = []
    for selected_pairs in itertools.combinations(pairs, n//2):
        if is_valid_matching(selected_pairs, n):
            cost = sum(graph[u][v] for u, v in selected_pairs)
            if cost < min_match:
                min_match = cost
                best_pairs = selected_pairs
    return list(best_pairs)

def is_valid_matching(pairs, n):
    checker = set()
    for u, v in pairs:
        if u in checker or v in checker:
            return False
        checker.add(u)
        checker.add(v)
    return len(checker) == n

def eulerian_to_hamiltonian(mst, matching, n):
    adj_list = {i: [] for i in range(n)}
    for u, v in mst:
        adj_list[u].append(v)
        adj_list[v].append(u)
    for u, v in matching:
        adj_list[u].append(v)
        adj_list[v].append(u)
    visit = [False] * n
    path = []

    def dfs(node):
        for neighbor in adj_list[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                dfs(neighbor)
        path.append(node)

    visit[0] = True
    dfs(0)
    path.reverse()
    # Making it a circuit (return to depot)
    path.append(0)
    return path

# Setup the cities and solve the TSP
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]
number_of_cities = len(cities)
graph = construct_graph(cities)
mst_edges = prim_mst(graph)
odd_vertices = find_odd_vertices(mst_edges, number_of_cities)
matching = min_cost_perfect_matching(graph, odd_vertices)
tour = eulerian_to_hamiltonian(mst_edges, matching, number_of_cities)

# Calculate tour cost
total_cost = sum(graph[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)