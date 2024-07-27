import itertools
import math

# Coordinates of 20 cities
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), 
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0), 
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Compute the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate a complete graph with distances between each pair of cities
distances = {}
edges = []
n = len(cities)
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(cities[i], cities[j])
        distances[(i, j)] = dist
        distances[(j, i)] = dist
        edges.append((dist, i, j))

# Sort edges based on the distance
edges.sort()

def is_hamiltonian_path_possible(threshold):
    # Create adjacency list for the subgraph with edges <= threshold
    adjacency_list = {i: [] for i in range(n)}
    for dist, u, v in edges:
        if dist > threshold:
            break
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Attempt to find any Hamiltonian cycle using simple backtracking
    for start in range(n):
        path = [start]
        visited = set([start])

        def backtrack(current):
            if len(path) == n:
                # Check if there's a link back to the start
                if start in adjacency_list[current]:
                    return path + [start]
                else:
                    return None
            for neighbor in adjacency_list[current]:
                if neighbor not in visited and distances[(current, neighbor)] <= threshold:
                    visited.add(neighbor)
                    path.append(neighbor)
                    result = backtrack(neighbor)
                    if result:
                        return result
                    path.pop()
                    visited.remove(neighbor)
            return None

        result = backtrack(start)
        if result:
            return result
    return None

# Binary search to find the minimum maximum distance that allows a Hamiltonian cycle
low, high = 0, max(dist[0] for dist in edges)
result = None
while low <= high:
    mid = (low + high) / 2
    tour = is_hamiltonian_path_possible(mid)
    if tour:
        result = tour, mid
        high = mid - 0.1
    else:
        low = mid + 0.1

if result:
    tour, max_dist = result
    total_travel_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
    print(f"Maximum distance between consecutive cities: {max_dist}")
else:
    print("No feasible solution found under the given constraints.")