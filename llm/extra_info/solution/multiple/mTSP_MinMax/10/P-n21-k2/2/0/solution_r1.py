import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of each city including depot city at index 0
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate distance matrix
def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean(cities[i], cities[j])
            distance_matrix[i][j] = distance_matrix[j][i] = distance
    return distance_matrix

# Calculate distance matrix
distance_matrix = calculate_distance_question_matrix(cities_coordinates)

# Number of robots
num_robots = 2

# Function to calculate total travel cost and path for a given tour (indices in cities list, starting from depot)
def calculate_tour_cost(tour):
    total_cost = 0
    full_path = [0]  # Start at the depot
    current_city = 0
    for city in tour:
        total_cost += distance_matrix[current_city][city]
        full_path.append(city)
        current_city = city
    total_cost += distance_matrix[current_city][0]  # Return to depot
    full_path.append(0)  # End at the depot
    return total_cost, full_path

# Simple heuristic to split cities evenly
city_indices = list(range(1, len(cities_coordinates)))  # list of cities excluding the depot
split_size = len(city_indices) // num_robots
tours = [city_indices[i:i + split_size] for i in range(0, len(city_indices), split_size)]

# If there are cities left due to rounding, append them to the last tour
if len(city_indices) % num_robots != 0:
    tours[-1].extend(city_indices[split_size * num_robots:])

# Calculate the tours and costs
robot_tours_details = []
max_travel_cost = 0
for i, tour in enumerate(tours):
    cost, path = calculate_tour_cost(tour)
    max_travel_cost = max(max_travel_cost, cost)
    robot_tours_details.append((path, cost))

# Print results according to format requirements
for i, details in enumerate(robot_tours_details):
    tour_path, tour_cost = details
    print(f"Robot {i} Tour: {tour_path}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {max_travelpass_cost}")