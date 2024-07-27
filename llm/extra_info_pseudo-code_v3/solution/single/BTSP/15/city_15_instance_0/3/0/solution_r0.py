import math
from itertools import permutations

# Define the cities as a list of tuples
cities = [
    (9, 93),    # Depot city 0
    (8, 51),    # City 1
    (74, 99),   # City 2
    (78, 50),   # City 3
    (21, 23),   # City 4
    (88, 59),   # City 5
    (79, 77),   # City 6
    (63, 23),   # City 7
    (19, 76),   # City 8
    (21, 38),   # City 9
    (19, 65),   # City 10
    (11, 40),   # City 11
    (3, 21),    # City 12
    (60, 55),   # City 13
    (4, 39)     # City 14
]

# Function to calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Sorting edges by weight
edges = []
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        dist = distance(cities[i], cities[j])
        edges.append((dist, i, j))

edges.sort()  # Sort by distance

# Helper function to find a Hamiltonian path with maximum edge weight below or equal to max_weight
def can_form_hamiltonian_path(max_weight):
    graph = {i: [] for i in range(len(cities))}
    for dist, u, v in edges:
        if dist <= max_weight:
            graph[u].append(v)
            graph[v].append(u)
        else:
            break
    
    # Check for Hamiltonian path via simple backtracking (not efficient for large graphs)
    def backtrack(curr_path):
        if len(curr_path) == len(cities):
            return curr_path
        last_node = curr_path[-1]
        for next_node in graph[last_node]:
            if next_node not in curr_path:
                result = backtrack(curr_path + [next_node])
                if result:
                    return result
        return None

    # Attempt to find a Hamiltonian path starting from the depot
    for start_node in [0]:  # Start at the depot
        path = backtrack([start_node])
        if path:
            path.append(0)  # return to the depot
            return path
    return None

# Main algorithm execution
best_path = None
for dist, _, _ in edges:
    path = can_form_hamiltonian_path(dist)
    if path:
        best_path = path
        max_dist_between_consecutive_cities = dist
        break

if best_path:
    total_cost = sum(distance(cities[best_path[i]], cities[best_path[i+1]]) for i in range(len(best_path)-1))
    print(f"Tour: {best_path}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist_between_consecutive_cities:.2f}")
else:
    print("No feasible tour found")