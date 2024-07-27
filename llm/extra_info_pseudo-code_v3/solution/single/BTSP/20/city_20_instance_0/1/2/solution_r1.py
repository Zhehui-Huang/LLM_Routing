import math
import itertools
from sys import maxsize

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize cities
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23), 6: (97, 32),
    7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87), 12: (20, 97),
    13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Compute all distances and sort edges by distance
edges = []
for i in cities:
    for j in cities:
        if i < j:
            distance = euclidean_model(cities[i], cities[j])
            edges.append((distance, i, j))

edges.sort()

# Find minimum bottleneck Hamiltonian cycle
def find_hamiltonian_cycle(cap):
    # Backtracking to check for Hamiltonian cycle
    path = []
    visited = set()
    
    def backtrack(current_node):
        if len(path) == len(cities) and (path[0], current_node) in cap:
            return path + [current_node]
        for (dist, u, v) in cap:
            if u == current_node and v not in visited:
                path.append(v)
                visited.add(v)
                result = backtrack(v)
                if result:
                    return result
                path.pop()
                visited.remove(v)
        return False

    # Try to find a Hamiltonian cycle from each node
    for start in cities:
        path = [start]
        visited = {start}
        result = backtrack(start)
        if result:
            return result
    return None

# Try each edge weight as threshold and attempt to find a cycle
for threshold, u, v in edges:
    cap = {(d, a, b) for (d, a, b) in edges if d <= threshold}
    result = find_hamiltonian_cycle(cap)
    if result:
        max_distance = threshold
        break

# Compute total travel cost and output the result
tour = result if result else []
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[(i+1) % len(tour)]]) for i in range(len(tour)))
max_edge_cost = max(euclidean_distance(cities[tour[i]], cities[tour[(i+1) % len(tour)]]) for i in range(len(tour)))

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_edge_cost
}

print(output)