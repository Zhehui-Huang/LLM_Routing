import math
import itertools

# Coordinates for each city including the depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82),
    (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Number of cities including the depot
n = len(coordinates)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all unique edges with distances
edges = sorted([(euclideanroller_distance(i, j), i, j) for i in range(n) for j in range(i + 1, n)])

# Helper function to find all Hamiltonian paths that start and end at the depot (0-index)
def find_hamiltonian_paths():
    min_max_edge = float('inf')
    best_path = []
    best_total_cost = 0

    # Attempt to construct path with fixed maximum edge weight
    for max_distance, u, v in edges:
        # Define the sub-graph where edges have distance <= max_distance
        subgraph_edges = {(i, j) for (d, i, j) in edges if d <= max_distance}

        # Use a permutation approach to find a valid Hamiltonian path
        for perm in itertools.permutations(range(1, n)):
            full_path = (0,) + perm + (0,)
            valid = True
            max_edge_in_path = 0
            total_cost = 0
            for i in range(len(full_path) - 1):
                if (full_path[i], full_path[i+1]) not in subgraph_edges and (full_path[i+1], full_path[i]) not in subgraph_edges:
                    valid = False
                    break
                current_cost = euclidean_distance(full_path[i], full_path[i+1])
                total_cost += current_cost
                if current_cost > max_edge_in_path:
                    max_edge_in_path = current_cost
            if valid and max_edge_in_path < min_max_edge:
                min_max_edge = max_edge_in_path
                best_path = full_path
                best_total_cost = total_cost
                break
        if best_path:
            break

    return best_path, best_total_by_costst, min_max_edge

# Find the best Hamiltonian circuit
tour, total_cost, max_distance = find_hamiltonian_paths()

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")