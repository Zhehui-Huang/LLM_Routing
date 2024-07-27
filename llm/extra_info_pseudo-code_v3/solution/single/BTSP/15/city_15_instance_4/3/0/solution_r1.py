import itertools
import math

# City coordinates
coordinates = [
    (35, 40),  # City 0
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all distance pairs and store them
num_cities = len(coordinates)
edges = []
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            edges.append((i, j, distance(coordinates[i], coordinates[j])))

# Sort edges by distance
edges.sort(key=lambda x: x[2])

def is_valid_path(cutoff, path):
    for i in range(len(path) - 1):
        if distance(coordinates[path[i]], coordinates[path[i + 1]]) > cutoff:
            return False
    return True

def find_hamiltonian_path(start, cutoff):
    # Attempt to find a Hamiltonian path using DFS
    stack = [(start, [start])]
    while stack:
        current, path = stack.pop()
        if len(path) == num_cities:
            if path[0] == 0:  # Ensuring it starts with the depot
                path.append(0)  # Making it a cycle by returning to the depot
                if is_valid_path(cutoff, path):
                    return path
        else:
            for i in range(num_cities):
                if i not in path:
                    if distance(coordinates[current], coordinates[i]) <= cutoff:
                        stack.append((i, path + [i]))
    return None

# Main algorithm to identify minimum bottleneck Hamiltonian cycle
def bottleneck_tsp():
    lower = 0
    upper = max(e[2] for e in edges)
    best_path = None
    while lower <= upper:
        mid = (lower + upper) / 2
        path = find_hamiltonian_path(0, mid)
        if path:
            best_path = path
            best_cutoff = mid
            upper = mid - 0.1
        else:
            lower = mid + 0.1
    return best_path, best_cutoff

tour, max_distance = bottleneck_tsp()
total_cost = sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Output results:
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)