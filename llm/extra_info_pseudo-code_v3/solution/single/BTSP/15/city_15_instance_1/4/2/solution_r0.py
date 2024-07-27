import math
import itertools

# Calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Cities' coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Number of cities
n = len(cities)

# Calculate all pairwise distances and generate list of edges with weights
edges = []
for i in range(n):
    for j in range(i+1, n):
        dist = distance(cities[i], cities[j])
        edges.append((i, j, dist))
        edges.append((j, i, dist))

# Sort edges based on distance
edges.sort(key=lambda x: x[2])

# Method to check if adding an edge creates a cycle
def causes_cycle(connections, max_vertices, u, v):
    if connections[u] == connections[v]:
        return True

    # Union
    old_conn = connections[v]
    for i in range(max_vertices):
        if connections[i] == old_conn:
            connections[i] = connections[u]
    return False

# Bottleneck TSP Approximate Solver
def bottleneck_tsp(edges, n):
    connections = list(range(n))
    best_tour = None
    min_max_distance = float('inf')

    for max_dist in set(edge[2] for edge in edges):
        # Create bottleneck graph at current max_dist
        current_edges = [(u, v) for u, v, d in edges if d <= max_dist]
        graph = {i: [] for i in range(n)}
        for u, v in current_edges:
            graph[u].append(v)
            graph[v].append(u)

        # Check if all vertices have at least one connection (connected graph)
        if all(graph[i] for i in range(n)):
            # Try to find a Hamiltonian path using backtracking
            path = [0]
            visited = set([0])

            def backtrack(node):
                if len(path) == n:
                    if 0 in graph[node]:  # Path needs to end at the starting node (cycle)
                        # Check if the path's max distance is minimized
                        max_edge = max(distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))
                        nonlocal min_max_distance, best_tour
                        if max_edge < min_max_distance:
                            min_max_distance = max_edge
                            best_tour = path + [0]
                        return True
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        path.append(neighbor)
                        if backtrack(neighbor):
                            return True
                        path.pop()
                        visited.remove(neighbor)
                return False
            
            backtrack(0)

    return best_tour, min_max_distance

# Find the optimal Hamiltonian path using the Bottleneck TSP algorithm
tour, max_distance = bottleneck_tsp(edges, n)

# Calculate total travel cost
total_cost = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")