import math
import itertools

# City positions
positions = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Step 1: Calculate distances and sort edges
num_cities = len(positions)
edges = []
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = calculate_distance(i, j)
        edges.append((dist, i, j))

# Sort edges by distance
edges.sort()

def check_hamiltonian_path(max_dist):
    """ Check if there exists a Hamiltonian path under the given max_dist. """
    # Create adjacency matrix respecting the max_dist constraint
    adj_matrix = [[False] * num_cities for _ in range(num_cities)]
    for d, i, j in edges:
        if d > max_dist:
            break
        adj_matrix[i][j] = adj_matrix[j][i] = True
    
    # Try to find a Hamiltonian path using backtracking
    for start in range(num_cities):
        path = [start]
        visited = [False] * num_cities
        visited[start] = True
        
        if hamiltonian_backtrack(path, visited, adj_matrix):
            return path
    return None

def hamiltonian_backtrack(path, visited, adj_matrix):
    """ Helper recursive function to find a Hamiltonian path. """
    if len(path) == num_cities:
        # Ensure it's a circuit returning to the start
        if adj_matrix[path[-1]][path[0]]:
            path.append(path[0])  # Complete the cycle
            return True
        else:
            return False
    current = path[-1]
    for next_city in range(num_cities):
        if not visited[next_city] and adj_matrix[current][next_city]:
            visited[next_city] = True
            path.append(next_city)
            if hamiltonian_backtrack(path, visited, adj_matrix):
                return True
            path.pop()
            visited[next_city] = False
    return False

# Step 3: Use binary search on the edge distances to find the minimum bottleneck
low, high = 0.0, edges[-1][0]
tour = []
while low <= high:
    mid = (low + high) / 2
    path = check_hamiltonian_path(mid)
    if path:
        tour = path
        high = mid - 0.1
    else:
        low = mid + 0.1

# Calculate maximum edge and total cost in the tour
max_edge = 0
total_cost = 0
for i in range(1, len(tour)):
    dist = calculate_distance(tour[i-1], tour[i])
    total_cost += dist
    if dist > max_edge:
        max_edge = dist

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_edge, 2)}")