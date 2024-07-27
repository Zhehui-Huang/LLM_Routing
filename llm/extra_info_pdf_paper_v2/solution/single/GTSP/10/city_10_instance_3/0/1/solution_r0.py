import math
import random

# Coordinates of all the cities
coordinates = [
    (84, 67),  # Depot
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# City groups
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Function to calculate the total distance of the given tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

# Heuristic Solution Method: Simple Nearest Neighbour Approach Customized for GTSP
def find_best_tour(groups, start_city):
    current_city = start_city
    tour = [current_city]
    remaining_groups = groups[:]
    while remaining_groups:
        next_city = None
        min_distance = float('inf')
        current_group = random.choice(remaining_groups)
        # Choose the closest city in the current group
        for city in current_group:
            dist = euclidean_distance(current_city, city)
            if dist < min_distance:
                min_distance = dist
                next_city = city
        tour.append(next_city)
        current_city = next_city
        remaining_groups.remove(current_group)
    tour.append(start_city)  # Return to the start
    return tour

# Generate a tour and calculate the distance
best_tour = find_best_tour(groups, 0)
best_distance = calculate_total_distance(best_tour)

# Output the solution
print("Tour:", best_tour)
print("Total travel cost:", best_distance)