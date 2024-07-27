import math
from itertools import permutations

# Coordinates for cities including depot city
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

# Brute force approach using permutations to find an optimal tour minimizing the maximum leg distance
def find_optimal_tour():
    best_tour = None
    min_max_distance = float('inf')
    best_total_distance = float('inf')

    # Generate all permutations of city indices, excluding the starting point (city 0)
    city_indices = list(cities.keys())
    city_indices.remove(0)

    for perm in permutations(city_indices):
        # Complete the tour by returning to the starting city
        tour = [0] + list(perm) + [0]
        total_distance = 0
        max_leg_distance = 0

        # Calculate the total distance and the maximum distance between consecutive cities
        for i in range(len(tour) - 1):
            leg_distance = distance(tour[i], tour[i + 1])
            total_distance += leg_distance
            if leg_distance > max_leg_distance:
                max_leg_distance = leg_distance

        # Update the best tour if a new better one is found
        if max_leg_distance < min_max_distance:
            min_max_distance = max_leg_distance
            best_tour = tour
            best_total_distance = total_distance

    return best_tour, best_total_distance, min_max_distance

# Execute the function and print results
optimal_tour, best_total_distance, min_max_distance = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", best_total_distance)
print("Maximum distance between consecutive cities:", min_max_distance)