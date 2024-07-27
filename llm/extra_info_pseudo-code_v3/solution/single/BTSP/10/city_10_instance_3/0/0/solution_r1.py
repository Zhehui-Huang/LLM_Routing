import math
from itertools import permutations

# Locations of cities
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

# Calculate Euclidean distance between two cities
def calc_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Creating a matrix to store distances, and list of distances for sorting
distance_matrix = {}
edges = []
for i in cities:
    for j in cities:
        if i != j:
            if i not in distance_matrix:
                distance_matrix[i] = {}
            dist = calc_manager(i, j)
            distance_matrix[i][j] = dist
            edges.append((dist, i, j))

# Sort the edges based on the distances
edges.sort()

def has_hamiltonian_tour(bottleneck, start_city=0):
    from collections import defaultdict, deque
    
    # Create bottleneck graph
    graph = defaultdict(list)
    for dist, u, v in edges:
        if dist > bottleneck:
            break
        graph[u].append(v)
        graph[v].append(u)
    
    def visit(node, visited, count, path):
        if count == len(cities):
            return path[0] == start_city
        visited[node] = True
        result = False
        for neighbour in graph[node]:
            if not visited[neighbour]:
                if visit(neighbour, visited, count + 1, path + [neighbour]):
                    result = True
                    break
        visited[node] = False
        return result
    
    visited = {k: False for k in cities}
    path = [start_city]
    return visit(start_city, visited, 1, path)
    
def find_min_bottleneck():
    low, high = 0, max(edge[0] for edge in edges)
    best_path = None
    
    while low <= high:
        mid = (low + high) // 2
        if has_hamiltonian_tour(mid):
            best_path = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return best_path

bottleneck = find_min_bottleneck()

# Output the results:  
print(f"Minimum Bottleneck: {bottleneck}")