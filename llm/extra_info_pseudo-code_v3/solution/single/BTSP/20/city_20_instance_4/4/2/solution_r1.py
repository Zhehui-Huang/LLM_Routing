import math
from sys import maxsize

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def dfs(H, start, visited, path, n):
    if len(path) == n:
        if start == 0:  # Path must return to the depot
            return True
        return False
    
    for i in range(n):
        if not visited[i] and (start, i) in H:
            visited[i] = True
            path.append(i)
            if dfs(H, i, visited, path, n):
                return True
            path.pop()
            visited[i] = False
    return False

def find_hamiltonian_path(H, num_vertices):
    visited = [False] * num_vertices
    path = [0]
    visited[0] = True
    if dfs(H, 0, visited, path, num_vertices):
        # Add depot start to end if found a path
        path.append(0)
        return path
    return None

def bottleneck_tsp(cities):
    num_vertices = len(cities)
    distances = {}
    
    # Calculate and store all possible distances
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            distance = calculate_distance(cities[i], cities[j])
            distances[(i, j)] = distance
            distances[(j, i)] = distance
    
    # Sort distances based on the bottleneck value
    sorted_dist_list = sorted(distances.items(), key=lambda item: item[1])
    
    # Attempt to find minimum bottleneck value that contains a valid tour
    for index, ((i, j), dist) in enumerate(sorted_dist_list):
        possible_edges = {(a, b) for (a, b), d in distances.items() if d <= dist}
        path = find_hamiltonian_path(possible_edges, num_vertices)
        if path:
            max_edge_weight = max(
                calculate_distance(cities[path[k]], cities[path[k+1]]) 
                for k in range(len(path)-1)
            )
            total_cost = sum(
                calculate_distance(cities[path[k]], cities[path[k+1]]) 
                for k in range(len(path)-1)
            )
            return path, total_cost, max_edge_weight

    return None, None, None  # Return None if no solution found

# Input cities as coordinate pairs
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
          (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
          (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)]

# Invoke the bottleneck TSP solution function
tour_result, total_travel_cost, max_distance = bottleneck_tsp(cities)

# Display outputs
if tour_result:
    print(f"Tour: {tour_result}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("Failed to find a valid tour.")