import math
import itertools

# City coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Calculate Euclidean distances
def distance(u, v):
    return math.sqrt((cities[u][0] - cities[v][0]) ** 2 + (cities[u][1] - cities[v][1]) ** 2)

# Number of cities
n = len(cities)

# Create a list of all edges with their distances
edges = []
for i in range(n):
    for j in range(i+1, n):
        edges.append((distance(i, j), i, j))

# Sort edges by distance
edges.sort()


# Check if a Hamiltonian path exists in the given graph using backtracking
def hamiltonian_path(bottleneck, start):
    path = [start]
    visited = [False] * n
    visited[start] = True
    
    def backtrack(current):
        if len(path) == n:
            path.append(start)  # Close the loop
            return True
        for d, u, v in edges:
            if d > bottleneck:
                break
            if u == current and not visited[v]:
                next_node = v
            elif v == current and not visited[u]:
                next_node = u
            else:
                continue
            path.append(next_node)
            visited[next_node] = True
            if backtrack(next_node):
                return True
            path.pop()
            visited[next_node] = False
        return False
    
    return backtrack(start), path

# Find the bottleneck Hamiltonian path
def find_bottleneck_hamiltonian_path():
    for d, u, v in edges:
        feasible, path = hamiltonian_path(d, 0)
        if feasible:
            max_dist = max(distance(path[i], path[i+1]) for i in range(len(path)-1))
            total_cost = sum(distance(path[i], path[i+1]) for i in range(len(path)-1))
            return path, total_cost, max_dist

# Execute the algorithm to find the result
tour, total_travel_cost, max_distance = find_bottleneck_hamiltonian_path()

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")