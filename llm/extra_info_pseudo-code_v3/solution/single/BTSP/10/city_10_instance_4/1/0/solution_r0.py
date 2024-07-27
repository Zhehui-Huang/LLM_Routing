import math
from itertools import permutations

cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
# Create a list of edges with their weights
edges = []
for i in cities:
    for j in cities:
        if i < j:
            dist = distance(cities[i], cities[j])
            edges.append((i, j, dist))

# Sort edges based on the distance
sorted_edges = sorted(edges, key=lambda x: x[2])

# Checking for Hamiltonian cycle with the condition of minimizing the longest edge
def can_form_hamiltonian_path(max_dist):
    # Create adj. matrix that allows connectivity between nodes if distance is <= max_dist
    graph = {i: set() for i in range(len(cities))}
    for u, v, d in sorted_edges:
        if d <= max_dist:
            graph[u].add(v)
            graph[v].add(u)

    def is_hamiltonian_path(start):
        # Using DFS to check all possible paths
        for perm in permutations(range(1, len(cities))):
            path = [start] + list(perm) + [start]
            valid = True
            max_in_path = 0
            for k in range(len(path) - 1):
                if path[k+1] not in graph[path[k]]:
                    valid = False
                    break
                seg_dist = distance(cities[path[k]], cities[path[k+1]])
                if seg_dist > max_in_path:
                    max_in_path = seg_dist
            
            if valid:
                return True, path, max_in_path
        return False, [], float('inf')
    
    # Start from the depot in all possibilities
    for start in range(len(cities)):
        found, path, max_in_path = is_hamiltonian_path(start)
        if found:
            return True, path, max_in_path
    return False, [], float('inf')

# Binary search on the distances to find the minimum feasible longest edge
lo, hi = 0, max(e[2] for e in edges)
best_path, best_cost = [], float('inf')
while lo <= hi:
    mid = (lo + hi) / 2
    found, path, max_in_path = can_form_hamiltonian_path(mid)
    if found:
        if max_in_path < best_cost:
            best_cost = max_in_path
            best_path = path
        hi = mid - 1
    else:
        lo = mid + 1

# Calculate the total and maximum distances of the tour
total_travel_cost = sum(distance(cities[best_path[i]], cities[best_path[i + 1]]) for i in range(len(best_levelsolution) - 1))
maximum_distance = max(distance(cities[best_path[i]], cities[best_path[i + 1]]) for i in range(len(best_solution) - 1))

print(f"Tour: {best_path}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {maximum_distance}")