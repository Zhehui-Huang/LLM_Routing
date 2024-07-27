import math
from itertools import combinations

# Define the cities with their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Compute Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Generate distances between all pairs
n = len(cities)
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[frozenset([i, j])] = euclidean_distance(cities[i], cities[j])

# Determine all possible weights
all_weights = sorted(distances.values())

# Function to find a tour with a given max edge weight
def find_tour(max_edge_weight):
    from collections import defaultdict, deque
    
    # Create a graph with edges not exceeding the max_edge_weight
    graph = defaultdict(list)
    for pair, dist in distances.items():
        if dist <= max_edge_weight:
            a, b = tuple(pair)
            graph[a].append(b)
            graph[b].append(a)
            
    # Try to create a Hamiltonian cycle starting at node 0
    def bfs(start):
        queue = deque([[start]])
        visited = set()
        visited.add(start)
        while queue:
            path = queue.popleft()
            current = path[-1]
            if len(path) == n and path[0] == start:
                if start in graph[current]:
                    return path
                else:
                    continue
            for neighbor in graph[current]:
                if neighbor not in visited or (neighbor == start and len(path) == n):
                    queue.append(path + [neighbor])
                    visited.add(neighbor)
        return None
    
    return bfs(0)

# Binary search the smallest maximum edge length that allows a tour
low, high = 0, len(all_weights) - 1
best_tour = None

while low <= high:
    mid = (low + high) // 2
    tour = find_tour(all_weights[mid])
    if tour:
        best_tour = tour
        high = mid - 1
    else:
        low = mid + 1

if best_tour:
    # Calculate total cost and maximum distance in the found tour
    total_cost, max_distance = 0, 0
    for i in range(len(best_tour)-1):
        dist = euclidean_distance(cities[best_tour[i]], cities[best_tour[i + 1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    dist = euclidean_distance(cities[best_tour[-1]], cities[best_tour[0]])
    total_cost += dist
    if dist > max_dist:
        max_dist = dist
    print("Tour:", best_tour + [best_tour[0]])
    print("Total travel cost:", round(total_cost, 2))
    print("Maximum distance between consecutive cities:", round(max_distance, 2))
else:
    print("No valid tour found")