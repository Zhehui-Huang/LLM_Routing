import math
from itertools import permutations

# City coordinates provided
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), 
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), 
          (83, 96), (60, 50), (98, 1)]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all edges with their respective distances
edges = []
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        dist = distance(cities[i], cities[j])
        edges.append(((i, j), dist))
        edges.append(((j, i), dist))

# Sort edges based on distances
edges.sort(key=lambda x: x[1])

# Function to check if there exists a Hamiltonian path in the constructed graph
def has_hamiltonian_path(max_dist):
    # Construct a graph where edges only exist if their weights are <= max_dist
    graph = {i: set() for i in range(len(cities))}
    for (i, j), dist in edges:
        if dist <= max_dist:
            graph[i].add(j)
            graph[j].add(i)

    # Try to find any Hamiltonian path using backtracking
    for start_node in range(len(cities)):
        stack = [(start_node, [start_node])]
        visited = set([start_node])
        while stack:
            current, path = stack.pop()
            if len(path) == len(cities):
                path.append(path[0])  # Make it a cycle
                return path
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))
                    visited.remove(neighbor)
    return None

# Attempt to find the best (minimum longest edge) Hamiltonian tour
for max_dist in [edge[1] for edge in edges]:
    result = has_hamiltonian_path(max_dist)
    if result:
        # Calculate total travel cost and the maximum edge in the tour
        total_cost = sum(distance(cities[result[i]], cities[result[i + 1]]) for i in range(len(result) - 1))
        max_edge = max(distance(cities[result[i]], cities[result[i + 1]]) for i in range(len(result) - 1))
        print(f"Tour: {result}")
        print(f"Total travel cost: {total_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_edge:.2f}")
        break