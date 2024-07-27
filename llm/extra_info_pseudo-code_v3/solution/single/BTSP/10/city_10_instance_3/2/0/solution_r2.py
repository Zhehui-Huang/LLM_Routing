import math
import itertools
from collections import defaultdict

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

# Generate all edges with their distances
edges = sorted((dist_matrix[i][j], i, j) for i in range(num_cities) for j in range(i + 1, num_cities))

def check_hamiltonian_path(bottleneck):
    # Graph creation under the bottleneck constraint
    graph = defaultdict(list)
    for cost, u, v in edges:
        if cost <= bottleneck:
            graph[u].append(v)
            graph[v].append(u)

    # Finding all paths from node 0 that visit all nodes exactly once and return to the start
    def find_path(start, visited, current_path):
        if len(current_path) == num_cities:
            if start in graph[current_path[-1]]:
                return current_path + [start]
            else:
                return None

        for next_node in graph[current_path[-1]]:
            if not visited[next_node]:
                visited[next_node] = True
                potential_path = find_path(start, visited, current_path + [next_node])
                if potential_path:
                    return potential_path
                visited[next_node] = False
        return None

    visited = [False] * num_cities
    visited[0] = True
    return find_path(0, visited, [0])

# Use binary search to find the optimal maximum distance between consecutive cities
low, high = 0, max(dist_matrix[i][j] for i in range(num_cities) for j in range(i+1, num_cities))
result_path = None
while low <= high:
    mid = (low + high) / 2
    path = check_hamiltonian_path(mid)
    if path:
        result_path = path
        high = mid - 1
    else:
        low = mid + 1

if result_path:
    max_edge_weight = max(dist_matrix[result_path[i]][result_path[i+1]] for i in range(len(result_utils) - 1))
    total_travel_cost = sum(dist_matrix[result_path[i]][result_path[i+1]] for i in range(len(result_path) - 1))
    print(f"Tour: {result_path}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_edge_weight}")
else:
    print("No valid tour was found.")