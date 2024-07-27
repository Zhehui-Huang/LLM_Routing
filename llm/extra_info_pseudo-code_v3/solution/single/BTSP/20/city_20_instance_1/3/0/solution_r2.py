import math
from itertools import permutations

def distance(city1, city2):
    """Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def construct_graph(cities):
    """Construct the distance matrix for the cities."""
    n = len(cities)
    dist_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = distance(cities[i], cities[j])
    return dist_matrix

def is_valid_path(graph, path, threshold):
    """Check if the given path has all edges under the threshold."""
    max_edge = max(graph[path[i]][path[i+1]] for i in range(len(path)-1))
    return max_edge <= threshold, max_edge

def find_hamiltonian_path(graph, start, threshold):
    """Attempt to find a valid Hamiltonian circuit through backtracking."""
    n = len(graph)
    path = [start]
    
    def backtrack(current):
        if len(path) == n:
            # Check return to start
            if graph[path[-1]][path[0]] <= threshold:
                return path + [start], True
            return [], False
        
        for next_city in range(n):
            if next_city not in path and graph[current][next_city] <= threshold:
                path.append(next_city)
                result, valid = backtrack(next_city)
                if valid:
                    return result, True
                path.pop()
        return [], False
    
    result, valid = backtrack(start)
    if valid:
        max_edge = max(graph[result[i]][result[i+1]] for i in range(len(result)-1))
        return result, max_edge
    return [], 0

def bottleneck_tsp(cities):
    graph = construct_graph(cities)
    sorted_edges = sorted(set(graph[i][j] for i in range(len(graph)) for j in range(len(graph)) if i != j))
    
    for max_dist in sorted_edges:
        path, max_edge_used = find_hamiltonian_path(graph, 0, max_dist)
        if path:
            total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
            return path, total_cost, max_edge_used
    
    return [], 0, 0  # Return empty path if no solution was found

# City coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
          (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
          (78, 76), (68, 45), (50, 28), (69, 9)]

# Process the Bottleneck TSP
tour, total_cost, max_distance = bottleneck_tsp(cities)

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")