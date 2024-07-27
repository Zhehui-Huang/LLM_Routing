import math
from itertools import permutations

# Coordinates of each city
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Generate all possible tours starting and ending at the depot (city 0)
def generate_tours():
    all_cities = list(cities.keys())
    for perm in permutations(all_cities[1:]):  # generate permutations of cities except the depot
        yield [0] + list(perm) + [0]

# Evaluate each tour to find the one with the minimum bottleneck distance
def find_min_bottleneck_tour():
    min_bottleneck_value = float('inf')
    best_tour = None
    for tour in generate_tours():
        # Calculate the maximum distance between consecutive cities
        max_edge_cost = max(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
        if max_edge_cost < min_bottleneck_value:
            min_bottleneck_value = max_edge_cost
            best_tour = tour
            
    return best_tour, min_bottleneck_value

# Get the best tour based on the minimum bottleneck distance
best_tour, min_bottleneck_value = find_min_bottleneck_tour()

# Calculate the total cost of the best tour
total_cost = sum(euclidean_distance(cities[best_tour[i]], cities[best_tour[i+1]]) for i in range(len(best_tour) - 1))

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_bottleneck_value:.2f}")