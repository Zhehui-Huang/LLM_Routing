import math
import itertools

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_distances(cities):
    n = len(cities)
    return [[euclidean_distance(*cities[i], *cities[j]) for j in range(n)] for i in range(n)]

def prim_mst(distances):
    n = len(distances)
    in_tree = [False] * n
    min_edge = [(float('inf'), -1) for _ in range(n)]
    min_edge[0] = (0, 0)
    mst_edges = []
    while len(mst_edges) < n-1:
        u = min((cost, idx) for idx, (cost, v) in enumerate(min_edge) if not in_tree[idx])[1]
        in_tree[u] = True
        mst_edges.append((u, min_edge[u][1]) if min_edge[u][1] != u else (min_edge[u][1], u))

        for v in range(n):
            if not in_tree[v] and distances[u][v] < min_edge[v][0]:
                min_edge[v] = (distances[u][v], u)
    return [(u, v) if u != v else None for u, v in mst_edges if u != v]

def find_odd_degree_vertices(mst_edges, n):
    degree = [0] * n
    for u, v in mst_edges:
        degree[u] += 1
        degree[v] += 1
    return [u for u in range(n) if degree[u] % 2 == 1]

def compute_min_weight_perfect_matching(odd_vertices, distances):
    num_vertices = len(odd_vertices)
    if num_vertices <= 1:
        return []

    pairs = list(itertools.combinations(odd_vertices, 2))
    weights = {pair: distances[pair[0]][pair[1]] for pair in pairs}
    
    # Using a simple greedy approach to find a matching (Non-optimal, but simple for illustration)
    # A proper implementation would look into Blossom algorithm for minimum weighted perfect matching
    matching = []
    while pairs:
        u, v = min(pairs, key=lambda x: weights[x])
        matching.append((u, v))
        pairs = [pair for pair in pairs if u not in pair and v not in pair]
    return matching

def create_eulerian_circuit(mst_edges, matching, n):
    adj_list = {i: [] for i in range(n)}
    for u, v in mst_edges + matching:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    start = 0
    tour = []
    stack = [start]
    path = []
    
    while stack:
        u = stack[-1]
        if adj_list[u]:
            v = adj_list[u].pop()
            adj_list[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())
    return path[::-1]

cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

distances = calculate_distances(cities)
mst_edges = prim_mst(distances)
odd_vertices = find_odd_degree_vertices(mst_edges, len(cities))
matching = compute_min_weight_perfect_matching(odd_vertices, distances)
eulerian_circuit = create_eulerian_circuit(mst_edges, matching, len(cities))
unique_tour = list(dict.fromkeys(eulerian_circuit + [eulerian_circuit[0]]))  # Ensure starting at the depot and becomes Hamiltonian

total_cost = sum(distances[unique_tour[i]][unique_tour[i+1]] for i in range(len(unique_tour) - 1))

print(f"Tour: {unique_tour}")
print(f"Total travel cost: {total_cost:.2f}")