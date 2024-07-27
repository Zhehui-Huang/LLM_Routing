import itertools
import math

# Coordinates for the cities
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all pairs of cities and their distances
edges = [(i, j, distance(i, j)) for i in range(15) for j in range(i+1, 15)]

# Sort edges based on distances
edges.sort(key=lambda x: x[2])

# Function to find if there's a Hamiltonian path in subset of edges with max edge distance capped
def has_hamiltonian_path(max_dist):
    # Subgraph with edges not exceeding max_dist
    subgraph = {i: [] for i in range(15)}
    for i, j, dist in edges:
        if dist <= max_dist:
            subgraph[i].append(j)
            subgraph[j].append(i)

    # Using a simple backtracking approach to check for Hamiltonian path
    def backtrack(node, visited, path):
        if len(path) == 15:
            return path + [path[0]]  # To include returning to the depot city 0

        for neighbor in subgraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = backtrack(neighbor, visited, path + [neighbor])
                if result is not None:
                    return result
                visited.remove(neighbor)
        return None
    
    # Start from depot city 0
    visited = {0}
    return backtrack(0, visited, [0])

# Main algorithm to find the Hamiltonian path with minimized maximum edge
for max_dist in (edge[2] for edge in edges):
    result = has_hamiltonian_path(max_dist)
    if result is not None:
        # Calculate total cost and maximum distance in the resulting tour
        total_cost = sum(distance(result[i], result[i+1]) for i in range(len(result)-1))
        max_distance = max(distance(result[i], result[i+1]) for i in range(len(result)-1))
        print(f"Tour: {result}")
        print(f"Total travel cost: {total_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
        break