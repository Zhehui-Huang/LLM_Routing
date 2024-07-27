import math
from itertools import permutations

# City coordinates including the depot city
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Compute all pairwise distances
num_cities = len(city_coords)
distances = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Sorting edges by weight (distance)
edges = []
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        edges.append((distances[i][j], i, j))
edges.sort()

# Function to check if hamiltonian path exists
def has_hamiltonian_path(bottleneck):
    graph = {i: [] for i in range(num_cities)}
    for dist, u, v in edges:
        if dist > bottleneck:
            break
        graph[u].append(v)
        graph[v].append(u)

    # Using simple backtrack to find a Hamiltonian path
    for start in range(num_classes):
        if find_path(graph, [start], set([start])):
            return True
    return False

def find_path(graph, path, visited):
    if len(path) == num_cities:
        return path

    current = path[-1]
    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            path.append(neighbor)
            result = find_path(graph, path, visited)
            if result:
                return result
            visited.remove(neighbor)
            path.pop()
    return None

# Iterate over sorted distances to find the smallest bottleneck that allows a Hamiltonian path
for dist, u, v in edges:
    if has_hamiltonian_path(dist):
        # Construct the path
        optimal_path = find_path({i: [] for i in range(num_cities)}, [0], set([0]))
        break

# Calculate the tour information: total cost and maximum distance
total_cost = sum(distances[optimal_path[i]][optimal_path[i + 1]] for i in range(len(optimal_path) - 1))
max_distance = max(distances[optimal_path[i]][optimal_path[i + 1]] for i in range(len(optimal_path) - 1))

# Output results
print("Tour:", optimal_path + [optimal_path[0]])
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)