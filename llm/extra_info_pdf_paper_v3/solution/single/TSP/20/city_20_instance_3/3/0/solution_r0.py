import math
from heapq import heappop, heappush
from itertools import combinations

# Helper function to calculate Euclidean distance
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# List of cities including the depot city
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
          (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
          (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Step 1: Compute all pairwise distances
n = len(cities)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        distances[i][j] = distances[j][i] = euclidean_distance(*cities[i], *cities[j])

# Step 2: Prim's MST algorithm for shortest spanning tree (SST)
def prim_mst(distances):
    n = len(distances)
    in_tree = [False] * n
    min_edge = [(float('inf'), None) for _ in range(n)]  # (cost, to_city)
    min_edge[0] = (0, 0)  # Start from vertex 0
    mst_edges = []
    total_cost = 0
    for _ in range(n):
        u = min((cost, v) for v, (cost, _) in enumerate(min_edge))[1]
        in_tree[u] = True
        total_cost += min_edge[u][0]
        if u != 0:
            mst_edges.append((min_edge[u][1], u))
        
        for v in range(n):
            if not in_tree[v] and distances[u][v] < min_edge[v][0]:
                min_edge[v] = (distances[u][v], u)
    return mst_edges, total_cost

mst_edges, _ = prim_mst(distances)

# Step 3: Formulate vertices of odd degrees from the MST and perfect matching
degree = [0] * n
for u, v in mst_edges:
    degree[u] += 1
    degree[v] += 1

odd_vertices = [v for v in range(n) if degree[v] % 2 == 1]
odd_pair_distances = {(u, v): distances[u][v] for u, v in combinations(odd_vertices, 2)}

# Minimum cost perfect matching on the vertices with odd degree
def min_cost_perfect_matching(odd_vertices, distances):
    matchings = []
    
    # Pair vertices optimally and recursively
    def recur_matching(pairs, cost_so_far):
        nonlocal min_cost, matchings
        if not pairs:
            if cost_so_far < min_cost:
                min_cost = cost_so_far
                matchings = current_matching[:]
        else:
            v = pairs[0]
            for u in pairs[1:]:
                pair_dist = distances[(u, v)]
                new_pairs = [w for w in pairs if w not v and w not u]
                current_matching.append((v, u))
                recur_matching(new_pairs, cost_so_far + pair_dist)
                current_matching.pop()
    
    current_matching = []
    min_cost = float('inf')
    recur_matching(odd_vertices, 0)
    return matchings

match_edges = min_cost_perfect_matching(odd_vertices, odd_pair_distances)

# Step 4: Use mst_edges and matching_edges to derive a Eulerian graph
tour_edges = mst_edges + match_edges

# Use depth-first search or Fleury's algorithm to find the Eulerian circuit from tour_edges and convert to Hamiltonian
def eulerian_to_hamiltonian(tour_edges, start):
    graph = {i: [] for i in range(n)}
    for u, v in tour_edges:
        graph[u].append(v)
        graph[v].append(u)
  
    # Eulerian circuit using Hierholzer's algorithm
    current_path, circuit = [start], []

    while current_path:
        u = current_path[-1]
        if graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            current_path.append(v)
        else:
            circuit.append(current_path.pop())
    circuit.reverse()

    # Ensure only unique city visits in order for Hamiltonian path
    visited = set()
    hamiltonian_path = []
    for city in circuit:
        if city not in visited:
            visited.add(city)
            hamiltonian_path.append(city)

    # Reconnect back to start
    hamiltonian_path.append(hamiltonian_path[0])
    return hamiltonian_path

tour = eulerian_to_hamiltonian(tour_edges, 0)

# Step 5: Calculate total travel cost
def calculate_total_cost(tour, distances):
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost

total_travel_cost = calculate_total_cost(tour, distances)

# Prepare final output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")