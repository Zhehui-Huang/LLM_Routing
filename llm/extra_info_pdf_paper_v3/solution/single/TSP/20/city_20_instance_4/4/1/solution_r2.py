from math import sqrt
from itertools import combinations

# Cities' coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distances between all pairs of cities
n = len(cities)
distances = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

# Prim's algorithm for MST
def prim_starting_at_zero(n, distances):
    in_tree = [False] * n
    cost = [float('inf')] * n
    parent = [-1] * n
    cost[0] = 0
    mst_edges = []
    
    for _ in range(n):
        # Select the minimum cost vertex from the vertices that are not yet included.
        u = min((c, i) for i, c in enumerate(cost) if not in_tree[i])[1]
        in_tree[u] = True
        if parent[u] != -1:
            mst_edges.append((parent[u], u))
        
        for v in range(n):
            if distances[u][v] < cost[v] and not in_tree[v]:
                cost[v] = distances[u][v]
                parent[v] = u
    
    return mst_edges

mst_edges = prim_starting_at_zero(n, distances)

# Finding nodes with an odd degree in the MST
degree = [0] * n
for u, v in mst_edges:
    degree[u] += 1
    degree[v] += 1

odd_degree_nodes = [i for i in range(n) if degree[i] % 2 == 1]

# Finding minimum-cost perfect matching using a greedy approach
matches = []
used = [False] * n
for u in odd_degree_nodes:
    if not used[u]:
        distances_to_v = [(distances[u][v], v) for v in odd_degree_nodes if not used[v] and v != u]
        min_distance, v = min(distances_to_v)
        matches.append((u, v))
        used[u] = True
        used[v] = True

# Combine the edges from MST and matching to form an Eulerian circuit
adj_list = {i: [] for i in range(n)}
for u, v in mst_edges + matches:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Hierholzer's algorithm to find the Eulerian cycle
def find_eulerian_tour(graph, start_vertex):
    # Start from a vertex with an odd degree
    stack = [start_vertex]
    path = []
    while stack:
        vertex = stack[-1]
        if graph[vertex]:
            next_vertex = graph[vertex].pop()
            stack.append(next_vertex)
            graph[next_vertex].remove(vertex)
        else:
            path.append(stack.pop())
    return path

eulerian_tour = find_eulerian_tour(adj_list, 0)

# Remove repeated nodes to form a valid TSP route (Hamiltonian cycle)
visited = set()
final_tour = []
for node in eulerian_tour:
    if node not in visited or node == 0:
        visited.add(node)
        final_tour.append(node)

# Ensure the tour starts and ends at the depot city
final_tour.append(final_tour[0])

# Calculate the cost of the tour
total_cost = sum(distances[final_tour[i]][final_tour[i+1]] for i in range(len(final_tour)-1))

# Print the results
print("Tour:", final_tour)
print("Total travel cost:", total_cost)