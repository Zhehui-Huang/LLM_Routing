import math
from itertools import combinations

# Coordinates of cities including the depot
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53),
    12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41), 16: (28, 49),
    17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Generate all pairs of distances between the cities
edges = [(i, j, euclidean_istance(cities[i], cities[j])) for i in range(20) for j in range(i+1, 20)]

# Sort edges by weight
edges.sort(key=lambda x: x[2])

# Helper function to find the Hamiltonian path using DFS
def is_hamiltonian_path(n, edges_filtered):
    visited = [False]*n
    path = []
    
    def dfs(node):
        if len(path) == n:
            return path[0] == path[-1]
        for u, v, _ in edges_filtered:
            if u == node and not visited[v]:
                visited[v] = True
                path.append(v)
                if dfs(v):
                    return True
                visited[v] = False
                path.pop()
            elif v == node and not visited[u]:
                visited[u] = True
                path.append(u)
                if dfs(u):
                    return True
                visited[u] = False
                path.pop()
        return False
    
    for i in range(n):
        visited[i] = True
        path.append(i)
        if dfs(i):
            return True
        path.pop()
        visited[i] = False
    
    return False

# Main function to find the tour with minimized maximum edge weight
def find_bottleneck_tour():
    for max_dist in set(edge[2] for edge in edges):
        edges_filtered = [(u, v, d) for u, v, d in edges if d <= max_dist]
        if is_hamiltonian_path(20, edges_filtered):
            total_cost = sum(edge[2] for edge in edges_filtered)
            return path + [path[0]], total_cost, max_dist
    return None

# Execute the function
tour = find_bottleneck_tour()

if tour:
    tour_path, total_cost, max_edge_cost = tour
    print(f"Tour: {tour_path}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_edge_cost:.2f}")
else:
    print("No feasible solution found.")