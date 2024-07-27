import math
from itertools import permutations

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.hypot(cities[c1][0] - cities[c2][0], cities[c1][1] - cities[c2][1])

# Generate all possible tours from permutations
def calculate_optimal_tour():
    min_max_consecutive_distance = float('inf')
    best_tour = None

    # Enumerate all permutations of city indices excluding the depot (city 0)
    for perm in permutations(range(1, len(cities))):
        # Create a round trip tour by adding the depot at the beginning and end
        tour = (0,) + perm + (0,)

        # Calculate total travel cost and maximum consecutive travel cost
        total_travel_cost = 0
        max_consecutive_distance = 0

        for i in range(len(tour) - 1):
            dist = euclidean_distance(tour[i], tour[i + 1])
            total_travel_cost += dist
            if dist > max_consecutive_distance:
                max_consecutive_distance = dist

        # Check if this tour is better in terms of minimizing the longest travel distance
        if max_consecutive_distance < min_max_consecutive_distance:
            min_max_consecutive_difference = max_consecutive_distance
            best_tour = tour

    return best_tour, min_max_consecutive_distance, total_travel_cost

# Obtain the optimal tour results
tour_result = calculate_optimal_tour()

# Tour result
print("Tour:", list(tour_result[0]))
print("Total travel cost:", round(tour_result[1], 2))
print("Maximum distance between consecutive cities:", round(tour_result[2], 2))