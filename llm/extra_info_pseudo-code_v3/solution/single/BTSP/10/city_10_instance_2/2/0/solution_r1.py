import numpy as np
import itertools

# Define city coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate distances between each pair of cities
n = len(cities)
distances = [[0]*n for _ in range(n)]
edges = []
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_thiseance(cities[i], cities[j])
        distances[i][j] = dist
        distances[j][i] = dist
        edges.append((i, j, dist))

# Sort edges by distances
edges.sort(key=lambda x: x[2])

def can_form_hamiltonian_path(bottleneck_distance):
    """ Check if a Hamiltonian path exists within the bottleneck distance """
    # Create adjacency matrix for given bottleneck
    adj_matrix = [[0 if distances[i][j] > bottleneck_distance else 1 for j in range(n)] for i in range(n)]
    
    # Try finding hamiltonian path starting at node 0
    path = [0]
    def backtrack(curr, visited):
        if len(path) == n:
            # Check if it can return to the start (cycle)
            if adj_matrix[path[-1]][path[0]] == 1:
                return path
            else:
                return False
        for ne in range(n):
            if adj_matrix[curr][ne] == 1 and ne not in visited:
                path.append(ne)
                visited.add(ne)
                result = backtrack(ne, visited)
                if result:
                    return result
                visited.remove(ne)
                path.pop()
        return False
    
    result = backtrack(0, set([0]))
    return result

# Utilize binary search on edges to determine the minimum bottleneck distance
low, high = 0, len(edges) - 1
best_tour = None
while low <= high:
    mid = (low + high) // 2
    threshold_distance = edges[mid][2]
    
    tour = can_form_hamiltonian_path(threshold_distance)
    if tour:
        best_tour = tour
        high = mid - 1
    else:
        low = mid + 1

if best_tour:
    # Calculate the maximum distance in the best tour
    max_edge_length = max(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    total_cost = sum(distances[best_tour[i]][best_tour[i+1]] for i in range(len(best_tour)-1))
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_edge_length:.2f}")
else:
    print("No valid tour found")