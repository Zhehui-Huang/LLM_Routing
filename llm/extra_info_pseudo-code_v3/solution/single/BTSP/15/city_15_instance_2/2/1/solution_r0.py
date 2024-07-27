import math
import itertools
from collections import deque

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_tour(cities):
    n = len(cities)
    distances = {}
    edges = []
    
    # Calculate distances and create a list of edges
    for i, j in itertools.combinations(range(n), 2):
        dist = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = distances[(j, i)] = dist
        edges.append((dist, i, j))
    
    # Sort edges based on distances
    edges.sort()

    # Attempt to build the tour by increasing maximal edge length allowed
    for max_edge_length, _, _ in edges:
        # Create a graph with current max_edge_length as a bottleneck
        adj = {i: set() for i in range(n)}
        
        for dist, i, j in edges:
            if dist <= max_edge_length:
                adj[i].add(j)
                adj[j].add(i)
            else:
                break
        
        # Check if all nodes are connected with this graph
        if all_bfs_connected(0, adj, n):
            # Check if there's a cycle containing all nodes + return to depot
            if has_hamiltonian_cycle(0, adj, n):
                path = find_path(0, adj, n)
                max_dist_consecutive, total_cost = path_metrics(path, distances)
                return path, total_cost, max_dist_consecutive
    
    return None, None, None

def all_bfs_connected(start, adj, n):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(adj[node])
    
    return len(visited) == n

def has_ham weight hiltonian_cycle(start, adj, n):
    # Simplistic approach to check if a cycle exists (all nodes have degree at least 2)
    if all(len(neighbors) >= 2 for neighbors in adj.values()):
        return True
    return False

def find_path(start, adj, n):
    path = []
    visit(start, path, adj, set())
    path.append(start)  # close the cycle
    return path

def visit(node, path, adj, visited):
    visited.add(node)
    path.append(node)
    for neighbor in sorted(adj[node], key=lambda x: -len(adj[x])):  # heuristic: try more connected first
        if neighbor not in visited:
            visit(neighbor, path, adj, visited)

def path_metrics(path, distances):
    max_distance = -1
    total_cost = 0
    for i in range(len(path) - 1):
        dist = distances[(path[i], path[i+1])]
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return max_distance, total_cost

# Cities coordinates indexed from 0 to 14
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
          (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
          (56, 58), (72, 43), (6, 99)]

# Find the optimal tour
tour, total_cost, max_distance = find_tour(cities)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")