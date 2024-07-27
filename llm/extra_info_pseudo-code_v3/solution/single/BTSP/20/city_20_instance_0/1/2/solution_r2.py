import math
from itertools import combinations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate all distances and sort them
distances = []
city_indices = list(range(len(cities)))
for i, j in combinations(city_indices, 2):
    dist = euclidean_distance(cities[i], cities[j])
    distances.append((dist, i, j))
distances.sort()

def has_hamiltonian_path(max_dist):
    # Build graph with edges not exceeding max_dist
    edges = [(d, u, v) for (d, u, v) in distances if d <= max_dist]

    # Create adjacency list
    adj = {i: [] for i in city_indices}
    for _, u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Use backtracking to find a Hamiltonian path
    visited = set()

    def backtrack(node, count):
        if count == len(cities):
            return [node]
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                result = backtrack(neighbor, count + 1)
                if result:
                    return [node] + result
        visited.remove(node)
        return None
    
    for start in city_indices:
        path = backtrack(start, 1)
        if path:
            return path
    return None

# Start checking for each possible max_dist
for max_dist, _, _ in distances:
    tour = has_hamiltonian_path(max_dist)
    if tour:
        last_index = tour[0]
        total_travel_cost = 0
        max_consecutive_distance = 0
        for index in (tour + [tour[0]])[1:]:  # Close the tour
            distance = euclidean_distance(cities[last_index], cities[index])
            total_travel_cost += distance
            if distance > max_consecutive_distance:
                max_consecutive_distance = distance
            last_index = index
        print("Tour:", [0] + tour[1:] + [0])  # Ensuring to start and end at the depot 0
        print("Total travel cost:", total_travel_cost)
        print("Maximum distance between consecutive cities:", max_consecutive_distance)
        break