import itertools
import math
from sys import maxsize

# Cities coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Number of cities
n = len(cities)

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all pairwise city distances
dist_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Generate list of all edges and sort by weight
edges = [(i, j, dist_matrix[i][j]) for i in range(n) for j in range(n) if i != j]
edges.sort(key=lambda x: x[2])

# Helper function to check if a valid tour exists
def check_hamiltonian_path(max_distance):
    def dfs(vertex, visited, path):
        if len(path) == n:
            return path + [path[0]]  # make a cycle by connecting back to the depot
        
        for i in range(n):
            if (vertex, i) in valid_edges and i not in visited:
                new_path = dfs(i, visited | {i}, path + [i])
                if new_path:
                    return new_path
        return []

    # Create a graph with edges that do not exceed the max_distance
    valid_edges = {(min(i, j), max(i, j)) for i, j, d in edges if d <= max_distance}
    
    # Using DFS to find a Hamiltonian cycle from node 0
    result = dfs(0, {0}, [0])
    return result

# Main function to determine the minimal bottleneck distance for a valid tour
def find_min_bottleneck_tour():
    left, right = 0, max(dist_matrix[i][j] for i in range(n) for j in range(n) if i != j)
    
    best_path = None
    while left <= right:
        mid = (left + right) // 2
        path = check_hamiltonian_path(mid)
        if path:
            best_path = path
            right = mid - 1
        else:
            left = mid + 1
    
    return best_path

# Find the best tour path minimizing the largest inter-city travel
tour = find_min_bottleneck_tour()

# Calculate the total cost and the bottleneck of the tour
if tour:
    total_travel_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(n))
    max_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(n))

    print("Tour:", tour)
    print("Total travel cost:", round(total_travel_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No valid tour found.")