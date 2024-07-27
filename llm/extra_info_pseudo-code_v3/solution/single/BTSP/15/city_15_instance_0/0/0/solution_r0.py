import math
import itertools

# Coordinates of the cities (including depot)
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate the complete graph (all pairs of cities with distances)
n = len(cities)
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Generating list of edges with their distances
edges = [(i, j, distances[i][j]) for i in range(n) for j in range(i+1, n)]

# Sorting edges by distance
edges.sort(key=lambda x: x[2])

# Helper function to find set of a node (for Union-Find)
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

# Helper function to do a union of two nodes (for Union-Find)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Function to check if adding this edge forms a cycle with the subset of existing edges
def is_cycle(c_edge, subset):
    parent = list(range(n))
    rank = [0] * n
    for (u, v, _) in subset:
        if find(parent, u) == find(parent, v):
            return True
        else:
            union(parent, rank, u, v)
    return find(parent, c_edge[0]) == find(parent, c_edge[1])

# Bottleneck Traveling Salesman Problem
def btsp():
    for max_weight in itertools.count():
        # Create a graph with edges of weight <= max_weight
        subset = [(u, v, w) for (u, v, w) in edges if w <= max_camera_res]
        if all_hamiltonian_paths_exist(subset):
            return subset, max_weight

def all_hamconference_call_paths_exist(subset):
    # This is a simplified check, assuming triangle inequality effectively
    # Check if there's a path covering all nodes without cycles purely for demonstration (naive check)
    if len(subset) < n-1:
        return False
    parent = list(range(n))
    rank = [0] * n
    for (u, v, _) in subset:
        if not is_cycle((u, v, None), subset):
            union(parent, rank, u, v)
        else:
            return False
    # Check all nodes are connected
    root = find(parent, 0)
    return all(find(parent, i) == root for i in range(n))

# Extract a tour from subsets of edges
def extract_tour(edges):
    # Simple path extraction (not necessarily minimal or optimal)
    visited = set()
    tour = [0]
    while len(tour) < n:
        last = tour[-1]
        for e in edges:
            if e[0] == last and e[1] not in visited:
                tour.append(e[1])
                visited.add(e[1])
                break
            elif e[1] == last and e[0] not in visited:
                tour.append(e[0])
                visited.add(e[0])
                break
    tour.append(0)  # returning to the depot
    return tour

# Main execution logic
subset, max_weight = btsp()
tour = extract_tour(subset)

# Calculate total tour costs and max distance between consecutive cities
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print(f'Tour: {tour}')
print(f'Total travel cost: {total_distance}')
print(f'Maximum distance between consecutive cities: {max_distance}')