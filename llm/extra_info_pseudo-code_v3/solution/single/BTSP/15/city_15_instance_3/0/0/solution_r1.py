import math
from itertools import combinations

# Define cities coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all possible edges with distances
edges = [(i, j, calc_distance(i, j)) for i in cities for j in cities if i < j]
edges.sort(key=lambda x: x[2])  # Sort edges based on distance

def find_tour(max_length):
    # Graph preparations
    adj = {i: set() for i in cities}
    for i, j, d in edges:
        if d <= max_length:
            adj[i].add(j)
            adj[j].add(i)
    
    # DFS to find a valid Hamiltonian circuit
    def dfs(node, path, visited):
        if len(path) == len(cities):
            if node in adj[path[0]]:  # Check if we can return to the start
                return path + [path[0]]
            else:
                return None
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = dfs(neighbor, path + [neighbor], visited)
                if result:
                    return result
                visited.remove(neighbor)
        return None

    visited = {0}
    return dfs(0, [0], visited)

best_tour = None
best_max_dist = float('inf')

# Binary search on edge distances to find minimum max edge weight possible for a valid Hamiltonian circuit
left, right = 0, max(edge[2] for edge in edges)
while left <= right:
    mid = (left + right) / 2
    tour = find_tour(mid)
    if tour:
        max_dist_in_tour = max(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if max_dist_in_tour <= mid:
            best_tour = tour
            best_max_dist = max_dist_in_tour
            right = mid - 0.01
        else:
            left = mid + 0.01
    else:
        left = mid + 0.01

# Compute the total cost of the best tour
best_cost = sum(calc_distance(best_tour[i], best_tour[i+1]) for i in range(len(best_tour)-1))

print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")
print(f"Maximum distance between consecutive cities: {best_max_dist:.2f}")