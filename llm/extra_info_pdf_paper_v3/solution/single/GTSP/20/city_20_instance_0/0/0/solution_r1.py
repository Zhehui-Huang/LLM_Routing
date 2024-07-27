import math
from itertools import product

# Defined city positions and groups
positions = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 31),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
    (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Compute Euclidean distance between any two cities
def euclidean_distance(city1, city2):
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Evaluates a given tour's distance
def evaluate_tour(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Find and return the shortest possible tour that fulfills the constraints
def find_shortest_tour():
    depot = 0
    best_distance = float('inf')
    best_tour = None

    # Generate all possible combinations of visiting one city from each group
    for cities in product(*city_groups):
        # Generate all permutations of city visitation order
        for permutation in permutations(cities):
            # Build the tour: start at depot, visit the cities, and return to depot
            tour = [depot] + list(permutation) + [depot]
            # Calculate the distance of this tour
            current_distance = evaluate_tour(tour)
            # If the new tour is shorter, record it
            if current_distance < best_distance:
                best_distance = current_distance
                best_tour = tour

    return best_tour, best_distance

# Execute the tour search and display the results
best_tour, shortest_distance = find_shortest_tour()
print("Tour:", best_tour)
print("Total travel cost:", round(shortest_distance, 2))