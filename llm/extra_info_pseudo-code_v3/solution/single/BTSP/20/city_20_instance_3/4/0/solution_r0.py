import math
import itertools

# City positions
positions = [
    (30, 56), 
    (53, 42), 
    (1, 95), 
    (25, 61),
    (69, 57),  
    (6, 58),  
    (12, 84), 
    (72, 77), 
    (98, 95), 
    (11, 0), 
    (61, 25), 
    (52, 0), 
    (60, 95), 
    (10, 94),
    (96, 73), 
    (14, 47), 
    (18, 16), 
    (4, 43), 
    (53, 76), 
    (19, 72)
]

n = len(positions)

# Compute Euclidean distance between two points
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Build distance matrix and sort edges by weight
edges = []
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_distance(positions[i], positions[j])
        edges.append((dist, i, j))
edges = sorted(edges)

# Helper function to find whether graph has Hamiltonian Path
def has_hamiltonian_path(dist):
    # Create a graph with edges not exceeding the dist
    graph = {i: [] for i in range(n)}
    for d, i, j in edges:
        if d <= dist:
            graph[i].append(j)
            graph[j].append(i)

    # Check if there's any permutation that forms a valid cycle route
    for perm in itertools.permutations(range(1, n)):  # start always from city 0
        valid = True
        route = [0] + list(perm)
        max_d = 0
        for k in range(1, len(route)):
            if route[k] not in graph[route[k-1]]:
                valid = False
                break
            max_d = max(max_d, euclidean_distance(positions[route[k]], positions[route[k-1]]))
        if valid:
            return (True, [0] + list(perm) + [0], max_d)
    return (False, [], float('inf'))

# Apply the bottle-neck algorithm
for dist, _, _ in edges:
    result, route, max_distance = has_hamiltonian_path(dist)
    if result:
        total_travel_cost = sum(euclidean_distance(positions[route[i]], positions[route[i+1]]) for i in range(len(route) - 1))
        print(f"Tour: {route}")
        print(f"Total travel cost: {total_travel_cost:.2f}")
        print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
        break