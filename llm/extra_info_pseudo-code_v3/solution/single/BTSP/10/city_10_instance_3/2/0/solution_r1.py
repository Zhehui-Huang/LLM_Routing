import math

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between any two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

num_cities = len(cities)
dist_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Sort all distances and include city pairs for each distinct distance
all_edges = sorted((dist_matrix[i][j], i, j) for i in range(num_cities) for j in range(i + 1, num_cities))
unique_distances = sorted(set(weight for weight, i, j in all_edges))

# Function to check if a subgraph contains a Hamiltonian cycle starting and ending at node 0
def valid_tour(bottleneck):
    from collections import deque, defaultdict

    visited = [False] * num_cities
    neighbors = defaultdict(list)
    
    # Constructing a graph with the current bottleneck
    for weight, i, j in all_edges:
        if weight <= bottleneck:
            neighbors[i].append(j)
            neighbors[j].append(i)

    # BFS to check for connectivity and cycle possibility from node 0
    def bfs():
        queue = deque([0])
        path = []
        seen = set(queue)
        while queue:
            u = queue.popleft()
            path.append(u)
            if len(path) == num_cities:
                return path + [0]  # returning path if it contains all nodes plus returning to start
            for v in neighbors[u]:
                if v not in seen:
                    seen.add(v)
                   queue.append(v)
                    if len(seen) == num_cities and 0 in neighbors[v]:
                        path.append(v)
                        return path + [0]
        return []
    
    path = bfs()
    if path and all(dist_matrix[path[i]][path[i+1]] <= bottleneck for i in range(len(path) - 1)):
        return path
    return []

# Find the minimum bottleneck that allows for a Hamiltonian cycle
for bottleneck in unique_distances:
    path_found = valid_tour(bottleneck)
    if path_found:
        # Calculate total cost and the bottleneck max distance
        total_cost = sum(dist_matrix[path_found[i]][path_found[i+1]] for i in range(len(path_found) - 1))
        max_dist = max(dist_matrix[path_found[i]][path_found[i+1]] for i in range(len(path_found) - 1))
        print(f"Tour: {path_found}")
        print(f"Total travel cost: {total_cost}")
        print(f"Maximum distance between consecutive cities: {max_dist}")
        break