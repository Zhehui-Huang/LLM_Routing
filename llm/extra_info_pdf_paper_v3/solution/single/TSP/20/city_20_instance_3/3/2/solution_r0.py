import math
from itertools import combinations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def mst_prim(cities):
    num_cities = len(cities)
    in_tree = [False] * num_cities
    cost = [float('inf')] * num_cities
    parent = [-1] * num_cities
    cost[0] = 0
    
    for _ in range(num_cities):
        # Find the smallest cost vertex not yet in the tree
        u = min((cost[i], i) for i in range(num_cities) if not in_tree[i])[1]
        in_tree[u] = True
        
        for v in range(num_cities):
            if not in_tree[v] and v != u:
                dist = euclidean_distance(cities[u], cities[v])
                if dist < cost[v]:
                    cost[v] = dist
                    parent[v] = u
                    
    mst_edges = []
    for i in range(1, num_cities):
        mst_edges.append((parent[i], i))
    
    return mst_edges

def find_odd_vertices(mst_edges, num_cities):
    degree = [0] * num_cities
    for u, v in mst_edges:
        degree[u] += 1
        degree[v] += 1
    odd_vertices = [i for i in range(num_cities) if degree[i] % 2 == 1]
    return odd_vertices

def minimum_cost_matching(odd_vertices, cities):
    num_odd = len(odd_vertices)
    min_cost = {}
    pairs = tuple(combinations(odd_vertices, 2))
    for u, v in pairs:
        min_cost[(u, v)] = euclidean_distance(cities[u], cities[v])

    # Using a simple greedy approach to get pairs (not optimal minimum-cost perfect matching)
    matched_pairs = []
    visited = set()
    for u, v in sorted(pairs, key=lambda x: min_cost[x]):
        if u not in visited and v not in visited:
            visited.add(u)
            visited.add(v)
            matched_pairs.append((u, v))
    
    return matched_pairs

def form_eulerian_cycle(mst_edges, matched_pairs):
    adjacency_list = {}
    for u, v in mst_edges + matched_pairs:
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return eulerian_from_adjacency_list(adjacency_list, 0)

def eulerian_from_adjacency_list(adjacency_list, start_vertex):
    stack = [start_vertex]
    path = []
    
    while stack:
        u = stack[-1]
        if u in adjacency_list and adjacency_list[u]:
            v = adjacency_list[u].pop()
            stack.append(v)
            adjacency_list[v].remove(u)
        else:
            path.append(stack.pop())
    
    return path

def shortcut_hamiltonian(eulerian_cycle):
    visited = set()
    path = []
    for city in eulerian_cycle:
        if city not in visited:
            visited.add(city)
            path.append(city)
    path.append(path[0])  # Completing the cycle
    return path

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Define the problem
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Step 1: Find MST using Prim's algorithm
mst_edges = mst_prim(cities)

# Step 2: Identifying odd degree vertices in MST
odd_vertices = find_odd_vertices(mst_edges, len(cities))

# Step 3: Find minimum-cost perfect matching for the odd-degree vertices
matched_pairs = minimum_cost_matching(odd_vertices, cities)

# Step 4: Form Eulerian Cycle by combining MST edges and matched pairs
eulerian_cycle = form_eulerian_cycle(mst_edges, matched_pairs)

# Step 5: Convert the Eulerian circuit to a Hamiltonian circuit (tour) using shortcutting
hamiltonian_tour = shortcut_hamiltonian(eulerian_cycle)

# Step 6: Calculate the total travel cost
total_cost = calculate_tour_cost(hamiltonian_tour, cities)

# Output the results
print("Tour:", hamiltonian_tour)
print("Total travel cost:", total_cost)