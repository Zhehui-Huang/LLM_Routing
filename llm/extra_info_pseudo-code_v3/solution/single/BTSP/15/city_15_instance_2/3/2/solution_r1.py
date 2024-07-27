import math
import itertools

# Define the city coordinates
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

# Compute Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate all possible pairs of cities with their distances
def generate_edges():
    edge_list = []
    for i in cities:
        for j in cities:
            if i != j:
                edge_list.append((i, j, euclidean_distance(cities[i], cities[j])))
    return sorted(edge_list, key=lambda x: x[2])

edges = generate_edges()

# Attempt to find a Hamiltonian cycle given an edge weight limit
def can_form_hamiltonian_cycle(edge_max_weight):
    from collections import defaultdict
    
    # Build graph with edges not exceeding the max allowed weight
    graph = defaultdict(list)
    for u, v, weight in edges:
        if weight <= edge_max_weight:
            graph[u].append(v)
            graph[v].append(u)
    
    # Function to check for Hamiltonian cycle using backtracking
    def backtrack(path):
        if len(path) == len(cities):
            # Check if there is a return path to the start
            return path[0] in graph[path[-1]]
        last = path[-1]
        for next_city in graph[last]:
            if next_city not in path:
                path.append(next_city)
                if backtrack(path):
                    return True
                path.pop()
        return False
    
    # Trigger search from any city, start from the depot
    return backtrack([0])

# Binary search over the range of edge distances to find the minimum maximum edge weight
def find_min_max_edge_cycle():
    low, high = 0, max(e[2] for e in edges)
    best_tour_weight = None
    
    while low <= high:
        mid = (low + high) // 2
        if can_form_hamiltonian_cycle(mid):
            high = mid - 1
            best_tour_weight = mid
        else:
            low = mid + 1
    
    return best_tour_weight

best_weight = find_min_max_edge_cycle()

# Reconstruct tour using found best_weight
def reconstruct_tour(max_weight):
    from collections import deque
    
    # Build graph with max acceptable weight
    graph = defaultdict(list)
    distances = {}
    for u, v, weight in edges:
        if weight <= max_weight:
            graph[u].append(v)
            graph[v].append(u)
            distances[(u, v)] = weight
            distances[(v, u)] = weight
            
    # Breadth-First Search (BFS) for a path
    def bfs(start):
        queue = deque([([start], set([start]))])
        while queue:
            path, visited = queue.popleft()
            if len(path) == len(cities) and path[0] in graph[path[-1]]:
                return path + [path[0]]
            for neighbor in graph[path[-1]]:
                if neighbor not in visited:
                    queue.append((path + [neighbor], visited | {neighbor}))
        return None
    
    return bfs(0), sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

tour, total_travel_cost = reconstruct_tour(best_weight)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {best_weight}")