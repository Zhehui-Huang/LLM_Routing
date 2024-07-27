import math
from itertools import combinations, permutations

# Define cities and their coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate total distance of a proposed tour
def total_tour_distance(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Explore potential tours and find the minimum distance tour using brute force
def find_optimal_tour():
    k = 10  # Total cities to visit include the depot
    all_tours = []
    min_distance = float('inf')
    optimal_tour = []

    # Generate all combinations of 9 other cities (removing the depot)
    for cities in combinations(range(1, len(coordinates)), k - 1):
        # Create possible tours including return to the depot
        potential_tours = permutations(cities)
        for tour in potential_tours:
            current_tour = [0] + list(tour) + [0]
            current_distance = total_tour_distance(current_tour)
            if current_distance < min_distance:
                min_distance = current_distance
                optimal_tour = current_tour

    return optimal_tour, min_distance

# Run the function and capture the results
optimal_tour, min_cost = find_optimal_tour()

# Print the optimal tour and associated cost
print("Tour:", optimal_tour)
print("Total travel cost:", min_cost)