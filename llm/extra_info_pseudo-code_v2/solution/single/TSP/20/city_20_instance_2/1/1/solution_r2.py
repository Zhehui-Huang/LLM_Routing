import math
from itertools import permutations

# City coordinates
cities = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance between two city indices
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all city indices excluding the depot
city_indices = list(range(1, len(cities)))

# Function to find the optimal tour using permutations
def find_optimal_tour():
    min_distance = float('inf')
    optimal_tour = None

    # Evaluate all permutations of city visits
    for perm in permutations(city_indices):
        # Form a tour starting and ending at the depot (city index 0)
        tour = [0] + list(perm) + [0]
        # Calculate the total distance of this tour
        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

        # Check if the found tour has a smaller distance than the current best
        if tour_distance < min_distance:
            min_distance = tour_distance
            optimal_tour = tour

    return optimal_tour, min_distance

# Find the optimal tour and its distance
optimal_tour, total_travel_cost = find_optimal_tour()

# Print the calculated optimal tour and its corresponding travel cost
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_travel_cost, 2))