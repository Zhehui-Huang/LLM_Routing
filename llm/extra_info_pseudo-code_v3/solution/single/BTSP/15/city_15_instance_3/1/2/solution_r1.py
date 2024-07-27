import math
from collections import defaultdict

# City coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def dist(i, j):
    """ Compute the Euclidean distance between city i and city j """
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Find the maximum bottleneck edge constraint that still allows for a tour
def is_valid_bottleneck(max_len):
    # Create the subgraph with edges less than or equal to max_len
    graph = defaultdict(list)
    for i in cities:
        for j in cities:
            if i != j and dist(i, j) <= max_len:
                graph[i].append(j)

    # Try to perform DFS to find a Hamiltonian path
    def dfs(node, visited, path):
        if len(path) == len(cities):
            # Return to depot and check edge back
            if path[0] in graph[node]:
                return path + [path[0]]
            return False
        visited.add(node)
        for next_node in graph[node]:
            if next_node not in visited:
                res = dfs(next_node, visited, path + [next_node])
                if res:
                    return res
        visited.remove(node)
        return False

    # Start DFS from the depot
    path = dfs(0, set(), [0])
    return path

# Binary search over edge lengths to find the minimum bottleneck distance
sorted_distances = sorted(dist(i, j) for i in cities for j in cities if i < j)
low, high = 0, len(sorted_distances) - 1

while low < high:
    mid = (low + high) // 2
    if is_valid_bottleneck(sorted_distances[mid]):
        high = mid
    else:
        low = mid + 1

# Final assessment with the smallest valid bottleneck
best_bottleneck = sorted_distances[high]
tour = is_valid_bottleneck(best_bottleneck)

# Calculate detailed tour information
total_travel_cost = sum(dist(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
maximum_distance = max(dist(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {best_bottleneck}")