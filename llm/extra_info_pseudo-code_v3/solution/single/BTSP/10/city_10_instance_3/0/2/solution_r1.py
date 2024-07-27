import itertools
import math

# Coordinates of the cities, including the depot city at index 0
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

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Number of cities
n = len(cities)

# Create a list of all distinct pairs of cities
edges = []
for i in range(n):
    for j in range(i+1, n):
        dist = calculate_distance(cities[i], cities[j])
        edges.append((i, j, dist))
        edges.append((j, i, dist))

# Sort edges by the distance
edges = sorted(edges, key=lambda x: x[2])

# Function to check if a set of cities form a Hamiltonian cycle using permutation
def is_hamiltonian_cycle(permutation):
    total_dist = 0
    max_edge_length = 0
    for i in range(1, len(permutation)):
        dist = calculate_distance(cities[permutation[i-1]], cities[permutation[i]])
        max_edge_length = max(max_edge_length, dist)
        total_dist += dist
    # Closing the tour by returning to start
    dist = calculate_distance(cities[permutation[-1]], cities[perception[0]])
    max_edge_length = max(max_edge_length, dist)
    total_dist += dist

    return total_dist, max_edge_length

# Find the optimal tour based on the bottleneck criteria
best_tour = None
best_max_distance = float('inf')
for perm in itertools.permutations(range(1, n)):
    tour_cost, max_distance = is_hamiltonian_cycle([0] + list(perm) + [0])
    if max_distance < best_max_distance:
        best_max_distance = max_distance
        best_tour = [0] + list(perm) + [0]
        best_total_cost = tour_cost

# Output the best tour found and the corresponding metrics
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", best_max_distance)