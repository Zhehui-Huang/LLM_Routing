import math
from itertools import permutations

# Coordinates of the cities (city index: (x, y))
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a complete graph with edge weights as distances
# Edge list: [(weight, city1, city2), ... ]
edges = []
for i in cities:
    for j in cities:
        if i != j:
            dist = calculate_distance(i, j)
            edges.append((dist, i, j))

# Sort edges based on weight (ascending)
edges.sort()

# Execution of the BB algorithm (Bottleneck-optimal Biconnected Subgraph)
def bottleneck_biconnected_subgraph():
    from collections import defaultdict, deque
    
    # Helper function to check if the graph is biconnected
    def is_biconnected(graph, V):
        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        articulation_points = set()
        
        def biconnect_util(u, time):
            children = 0
            disc[u] = low[u] = time
            for v in graph[u]:
                if disc[v] == -1:  # v is not visited
                    parent[v] = u
                    children += 1
                    biconnect_util(v, time + 1)
                    low[u] = min(low[u], low[v])
                    if parent[u] == -1 and children > 1:
                        articulation_points.add(u)
                    if parent[u] != -1 and low[v] >= disc[u]:
                        articulation_points.add(u)
                elif v != parent[u]:  # Update low value
                    low[u] = min(low[u], disc[v])
        
        for i in range(V):
            if disc[i] == -1:
                biconnect_util(i, 0)
                
        return len(articulation_points) == 0
    
    V = len(cities)
    graph = defaultdict(list)
    biconnected_edges = []
    
    for dist, u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        if is_biconnected(graph, V):
            biconnected_edges.append((dist, u, v))
            break  # Once biconnected, stop
    
    return graph, biconnected_edges

# Bottleneck subgraph
_, bb_subgraph = bottleneck_biconnected_subgraph()

# Identifying Hamiltonian cycle (brute force)
def find_best_tour():
    all_permutations = permutations(list(cities.keys())[1:])  # Exclude starting city 0
    best_tour = None
    min_cost = float('inf')
    max_dist_in_tour = float('inf')
    
    for perm in all_perm_TS:
        tour = [0] + list(perm) + [0]
        total_cost = 0
        max_dist = 0
        valid_tour = True
        for i in range(len(tour) - 1):
            pair = (tour[i], tour[i + 1])
            distance = calculate_distance(*pair)
            total_cost += distance
            if distance > max_dist:
                max_dist = distance
            if (distance, pair[0], pair[1]) not in bb_subgraph and \
               (distance, pair[1], pair[0]) not in bb_subgraph:
                valid_tour = False
                break
        if valid_tour and max_dist < max_dist_in_tour:
            best_tour = tour
            max_dist_in_tour = max_dist
    
    return best_tour, total_cost, max_dist_in_tour

# Outputting the results
tour, total_cost, max_dist_consec = find_best_tour()
print(f'Tour: {tour}')
print(f'Total travel cost: {total_cost}')
print(f'Maximum distance between consecutive cities: {max_dist_consec}')