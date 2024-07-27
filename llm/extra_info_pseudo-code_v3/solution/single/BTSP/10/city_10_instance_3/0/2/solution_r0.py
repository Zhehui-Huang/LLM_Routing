from itertools import permutations
import math

# City coordinates as tuples
cities = [
    (84, 67),  # Depot 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute all inter-city distances
n = len(cities)
distances = {(i, j): calculate_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Sorting edges based on distances
sorted_edges = sorted(distances.items(), key=lambda item: item[1])

# Find a valid tour using a simple heuristic approach based on sorting edges
def find_valid_tour():
    threshold = sorted_edges[0][1]
    for weight, dist in sorted_edges:
        if valid_tour_exists(weight[0], weight[1], threshold):
            return weight, dist

# Function to check if a valid tour exists by trying to find a path, brute forcing permutations
def valid_tour_exists(start, end, max_dist):
    path = [start]
    visited = set(path)
    return find_path(path, visited, max_dist)

def find_path(path, visited, max_dist):
    current = path[-1]
    if len(path) == n:
        if distances.get((current, 0), float('inf')) <= max_dist:
            path.append(0)
            return path
        return False
    for i in range(n):
        if i not in visited and distances[(current, i)] <= max_dist:
            visited.add(i)
            path.append(i)
            result = find_path(path, visited, max_dist)
            if result:
                return result
            path.pop()
            visited.remove(i)
    return False

# Running the algorithm to find the valid tour
tour, max_distance = find_valid_tour()

# Calculating the total travel cost
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)