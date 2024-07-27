import math
import itertools

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Build a list of all pairwise connections and their distances
edges = [(i, j, euclidean_distance(i, j)) for i in range(len(cities)) for j in range(i+1, len(cities))]
edges.sort(key=lambda x: x[2])  # Sort by distance

# Helper function to try to find a Hamiltonian path within a threshold
def is_valid_tour(threshold, vertices):
    # Attempt to create a Hamiltonian Cycle with an upper bound on edge weights
    def backtrack(path):
        if len(path) == len(vertices):
            if path[0] in adj_list[path[-1]]:  # Check if we can return to the start
                return path
            return None
        last = path[-1]
        for next_vertex in adj_list[last]:
            if next_vertex not in path:
                result = backtrack(path + [next_vertex])
                if result:
                    return result
        return None

    # Adjacency list for the current threshold
    adj_list = {i: [] for i in vertices}
    for u, v, d in edges:
        if d <= threshold:
            adj_list[u].append(v)
            adj_list[v].append(u)

    # Try to find a Hamiltonian path using backtracking
    for start in vertices:
        path = backtrack([start])
        if path:
            return path
    return None

# Main logic to incrementally test increasing distance thresholds
for dist in sorted(set(e[2] for e in edges)):  # Unique sorted distances
    tour = is_valid_tour(dist, cities.keys())
    if tour:
        # Calculate total distance and max segment distance
        total_distance = sum(euclidean_distance(tour[i], tour[(i+1) % len(tour)]) for i in range(len(tour)))
        max_distance = max(euclidean_distance(tour[i], tour[(i+1) % len(tour)]) for i in range(len(tour)))
        # Output the results
        print("Tour:", tour + [tour[0]])
        print("Total travel cost:", total_distance)
        print("Maximum distance between consecutive cities:", max_distance)
        break  # We found the minimal maximum, stop here