import math
from itertools import permutations

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Define cities
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate all distances and get the ordered list of distances without duplicates
edges = []
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(cities[i], cities[j])
        edges.append((i, j, dist))
        edges.append((j, i, dist))

# Sort edges based on distance
edges.sort(key=lambda x: x[2])

# Function to attempt to extract a tour limiting to max_edge
def get_tour(max_edge):
    # Create adjacency list for edges under max_edge
    adj = {i: [] for i in range(n)}
    for e in edges:
        if e[2] <= max_edge:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
    
    # Attempt to find a Hamiltonian path starting and ending at the depot (0)
    def dfs(current, path, visited):
        if len(path) == n and path[-1] == 0:
            return path
        if len(path) != 0 and path[-1] == 0:
            return None

        for neighbor in adj[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = dfs(neighbor, path + [neighbor], visited)
                if result is not None:
                    return result
                visited.remove(neighbor)
        return None

    # Start DFS from the node 0
    return dfs(0, [0], {0})

# Binary search over the sorted list of unique distances
unique_distances = sorted(set(e[2] for e in edges))
left, right = 0, len(unique_distances) - 1
best_tour = None

while left <= right:
    mid = (left + right) // 2
    tour = get_tour(unique_distances[mid])
    if tour:
        best_tour = tour
        right = mid - 1
    else:
        left = mid + 1

if best_tour is not None:
    # Compute the max edge weight in the best tour and the total travel cost
    max_edge_weight = max(euclidean_distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour) - 1))
    total_distance = sum(euclidean_distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour) - 1))
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_edge_weight}")
else:
    print("No suitable tour was found.")