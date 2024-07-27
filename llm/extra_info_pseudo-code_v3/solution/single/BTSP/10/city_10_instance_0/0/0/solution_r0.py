import math
from itertools import permutations

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Cities information
cities_coordinates = [
    (50, 42),  # City 0 - Depot
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Function to compute all pairs edge weights
def compute_edges(cities):
    n = len(cities)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            edges.append((dist, i, j))
    edges.sort()  # Sort by distance
    return edges

# Function to find a feasible tour
def find_tour(edges, n):
    for max_edge_length, _, _ in edges:
        if check_feasible_tour(n, max_edge_length):
            return max_edge_line_length

def check_feasible_tour(n, max_distance):
    for perm in permutations(range(1, n)):
        perm = [0] + list(perm) + [0]
        valid = True
        max_edge_length = 0
        total_distance = 0
        for i in range(len(perm)-1):
            dist = euclidean_distance(cities_coordinates[perm[i]], cities_coordinates[perm[i+1]])
            if dist > max_distance:
                valid = False
                break
            max_edge_length = max(max_edge_length, dist)
            total_distance += dist
        if valid:
            return {"tour": perm, "total_cost": total_distance, "max_distance": max_edge_length}
    return None  # No feasible tour

# Simulation starts here
n = len(cities_coordinates)
edges = compute_edges(cities_coordinates)
result = find_tour(edges, n)
if result:
    print(f"Tour: {result['tour']}")
    print(f"Total travel cost: {result['total_cost']}")
    print(f"Maximum distance between consecutive cities: {result['max_distance']}")
else:
    print("No feasible tour found.")