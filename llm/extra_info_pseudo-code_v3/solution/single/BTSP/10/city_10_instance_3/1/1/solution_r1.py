import math
import itertools
from collections import defaultdict, deque

# City Coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Create sorted list of edges by weight
edges = []
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        distance = calc'distance(i, j)
        edges.append((distance, i, j))

edges.sort()  # Sort edges based on distances

# Function to check if Hamiltonian path possible with given max weight
def has_hamiltonian_path(max_weight, return_path=False):
    subgraph = defaultdict(list)
    for distance, u, v in edges:
        if distance <= max_weight:
            subgraph[u].append(v)
            subgraph[v].append(u)
    
    # Try to find a Hamiltonian path using backtracking
    all_visited = [False] * n
    path = []

    def backtrack(current, count):
        if count == n:
            if path[0] == 0:  # Should return to depot
                return True
            else:
                return False
        for neighbor in subgraph[current]:
            if not all_visited[neighbor]:
                all_visited[neighbor] = True
                path.append(neighbor)
                if backtrack(neighbor, count + 1):
                    return True
                path.pop()
                all_visited[neighbor] = False
        return False

    all_visited[0] = True
    path.append(0)
    if backtrack(0, 1):
        if return_path:
            return path
        return True
    return False

# Function to find minimal bottleneck path
def find_btsp_path():
    left, right = 0, len(edges) - 1
    while left <= right:
        mid = (left + right) // 2
        if has_hamiltonian_path(edges[mid][0]):
            best_weight = edges[mid][0]
            right = mid - 1
        else:
            left = mid + 1

    # After finding the best weight, extract the path
    return best_weight, has_hamiltonian_path(best_weight, return_path=True)

best_weight, path = find_btsp_path()

# Calculating the metrics for the tour
def calculate_tour_metrics(path):
    max_distance = 0
    total_travel_cost = 0
    last_city = path[0]
    for city in path[1:] + [path[0]]:
        distance = calc_distance(last_city, city)
        total_travel_cost += distance
        max_distance = max(max_distance, distance)
        last_city = city
    return path, total_travel_cost, max_distance

# Obtain tour and metrics
tour, total_cost, max_distance = calculate_tour_metrics(path)

# Printing the outputs as required
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")