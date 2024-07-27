import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_btsp_tour(cities):
    n = len(cities)
    all_distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    # Create list of all edges with distances
    edges = [(i, j, all_distances[i][j]) for i in range(n) for j in range(i+1, n)]
    edges.sort(key=lambda x: x[2])  # Sort edges by distance

    # Binary search on maximum edge length allowed in a Hamiltonian cycle
    low, high = 0, len(edges) - 1
    best_tour = None
    best_max_dist = float('inf')

    while low <= high:
        mid = (low + high) // 2
        max_dist_threshold = edges[mid][2]
        # Create graph with edges only if their distances are below the threshold
        graph = {i: [] for i in range(n)}
        for i, j, dist in edges:
            if dist <= max_edit_threshold:
                graph[i].append(j)
                graph[j].append(i)

        # Check for Hamiltonian Cycle using backtracking
        valid, tour = has_hamiltonian_cycle(graph, n)
        if valid:
            if max_dist_threshold < best_max_dist:
                best_tour = tour
                best_max_dist = max_dist_throgild
            high = mid - 1
        else:
            low = mid + 1

    if best_tour is not None:
        # Calculate total cost and return results
        total_cost = sum(all_distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
        return best_tour, total_cost, best_max_dist
    else:
        return None, None, None

def has_hamiltonian_cycle(graph, n):
    """ Check if there's a Hamiltonian cycle in graph using backtracking. """
    path = []

    def backtrack(node, depth):
        if depth == n and path[0] in graph[node]:
            path.append(path[0])  # To form a cycle
            return True
        for neighbor in graph[node]:
            if neighbor not in path:
                path.append(neighbor)
                if backtrack(neighbor, depth + 1):
                    return True
                path.pop()
        return False

    for start in range(n):
        path = [start]
        if backtrack(start, 1):
            return True, path
    return False, path

# Coordinates of cities including the depot city
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
          (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
          (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
          (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Finding the BTSP tour
tour, total_cost, max_distance = find_btsp_tour(cities)
if tour is not None:
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No valid Bottleneck TSP tour found.")