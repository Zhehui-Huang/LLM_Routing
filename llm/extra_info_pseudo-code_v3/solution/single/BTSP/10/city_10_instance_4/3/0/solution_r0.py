import math
from itertools import permutations

# Coordinates of each city (including the depot city 0)
coordinates = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Calculating Euclidean distances between each pair of cities
def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Generate all distances and sort them
distances = {}
edge_list = []
n = len(coordinates)

for i in range(n):
    for j in range(i+1, n):
        if i != j:
            dist = calculate_distance(coordinates[i], coordinates[j])
            distances[(i, j)] = dist
            distances[(j, i)] = dist
            edge_list.append((dist, i, j))

edge_list.sort()

# Function to find Hamiltonian path that does not exceed a given max_edge_weight using backtracking
def is_hamiltonian_path(max_edge_weight, start_node=0, path=None, visited=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if len(path) == n:
        if dist_d[0] <= max_edge_weight:
            return path + [start_node]
        else:
            return None

    if len(visited) == 0:
        visited.add(start_node)
        path.append(start_node)

    for i in range(n):
        if i not in visited and distances[(path[-1], i)] <= max_edge_weight:
            visited.add(i)
            path.append(i)
            result = is_hamiltonian_path(max_edge_weight, start_node, path, visited)
            if result:
                return result
            visited.remove(i)
            path.pop()

    if len(path) == 1:
        return None

# Try to construct the Hamiltonian path with bottleneck constraints
for max_edge_weight, u, v in edge_list:
    ham_path = is_hamiltonian_path(max_edge_weight)
    if ham_path:
        break

# Compute the details of the resulting tour
tour_cost = sum(distances[(ham_path[i], ham_path[i+1])] for i in range(len(ham_path)-1))
max_distance = max(distances[(ham_path[i], ham_path[i+1])] for i in range(len(ham_path)-1))

# Returning the formulated outputs as specified
print("Tour:", ham_path)
print("Total travel cost:", tour_cost)
print("Maximum distance between consecutive cities:", max_distance)