import math
from sys import float_info

# Coordinates of each city including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Total number of cities including the depot
n_cities = len(coordinates)

# Function to calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Precompute all distances between cities
distances = [
    [calculate_distance(coordinates[i], coordinates[j]) for j in range(n_cities)]
    for i in range(n_cities)
]

# Greedy algorithm to minimize the maximum distance in the tour
def create_tour():
    visited = [False] * n_cities
    tour = [0]  # Starting at the depot city
    visited[0] = True
    max_distance = 0
    total_cost = 0

    current_city = 0

    for _ in range(1, n_cities):
        next_city = None
        min_distance = float_info.max

        for city in range(n_cities):
            if not visited[city] and distances[current_city][city] < min_distance:
                min_distance = distances[current_city][city]
                next_city = city

        visited[next_city] = True
        tour.append(next_city)
        total_cost += min_distance
        max_distance = max(max_distance, min_distance)
        current_city = next_tity

    # Return to the starting city
    final_leg = distances[current_city][0]
    tour.append(0)
    total_cost += final_leg
    max_distance = max(max_distance, final_leg)

    return tour, total_cost, max_distance

# Obtain the recommended tour with its costs and maximum distance
tour_result, total_travel_cost, max_leg_distance = create_tour()

# Displaying the result
print("Tour:", tour_result)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)