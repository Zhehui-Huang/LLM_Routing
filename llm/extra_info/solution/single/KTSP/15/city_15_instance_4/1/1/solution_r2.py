import itertools
import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_shortest_tour(cities):
    """Find the shortest tour, visiting exactly 12 cities including the depot city, starting and ending at the depot."""
    city_indices = list(range(1, len(cities)))  # Excluding the depot city index 0

    min_cost = float('inf')
    min_path = None

    # Generate combinations of 11 cities excluding the depot
    for combo in itertools.combinations(city_indices, 11):
        # Permutation of cities in the combination
        for perm in itertools.permutations(combo):
            # Construct the path: start at depot, visit each city in the permutation, return to depot
            path = [0] + list(perm) + [0]
            cost = sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))

            if cost < min_cost:
                min_cost = cost
                min_path = path

    return min_path, min_cost

# Coordinates of the cities including the depot city at index 0
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour(cities)

# Final output
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")