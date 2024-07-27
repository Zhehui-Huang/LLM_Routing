import math
import itertools

# Given cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create all edges with distances
edges = []
for i in cities:
    for j in cities:
        if i < j:
            edges.append(((i, j), distance(cities[i], cities[j])))

# Sort edges based on the distance
edges = sorted(edges, key=lambda x: x[1])

# Helper function to find a path using DFS
def find_path(start, visited, path):
    if len(visited) == len(cities):
        if (path[-1], start) in g or (start, path[-1]) in g:  # to complete the circuit
            path.append(start)
            return path
        return None

    for neighbor in range(len(cities)):
        if neighbor in visited or (path[-1], neighbor) not in g and (neighbor, path[-1]) not in g:
            continue
        visited.add(neighbor)
        path.append(neighbor)
        result = find_path(start, visited, path)
        if result:
            return result
        visited.remove(neighbor)
        path.pop()

    return None

# Attempt to construct Hamiltonian paths for each graph produced by a given upper bound
for edge_idx in range(len(edges)):
    cutoff_distance = edges[edge_idx][1]
    g = {(u, v) for (u, v), d in edges if d <= cutoff_distance}

    # Attempt to build a Hamiltonian path
    path = find_path(0, {0}, [0])
    if path and len(path) == len(cities) + 1:
        # Calculate total distance and max consecutive distance
        total_cost = sum(distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
        max_consecutive_distance = max(distance(cities[path[i]], cities[path[i + 1]]) for i in range(len(path) - 1))
        print(f"Tour: {path}")
        print(f"Total travel cost: {total_cost}")
        print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")
        break