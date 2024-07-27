import math

# Coordinates of cities including the depot
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_travel_plan(coordinates):
    from scipy.spatial import distance_matrix
    import numpy as np
    import sys

    # Create distance matrix
    dist_matrix = distance_matrix(coordinates, coordinates)

    # List to store the visited cities, starting with the depot city
    num_cities = len(coordinates)
    tour = [0]
    visited = set(tour)
    
    # Current city, start with the depot
    current_city = 0
    
    # Total distance and maximum distance initialization
    total_distance = 0
    max_distance = 0

    while len(tour) < num_cities:
        # Find the closest city that has not yet been visited
        next_city = None
        min_dist = sys.maxsize
        
        for city in range(num_cities):
            if city not in visited and dist_matrix[current_city][city] < min_dist:
                next_city = city
                min_dist = dist_matrix[current_city][city]
        
        # Visit the next city
        tour.append(next_city)
        visited.add(next_city)
        total_distance += min_dist
        max_distance = max(max_distance, min_dist)
        current_city = next_city

    # Return to the depot
    last_to_depot_distance = dist_matrix[current_city][0]
    tour.append(0)
    total_distance += last_to_depot_distance
    max_distance = max(max_distance, last_to_depot_distance)

    return tour, total_distance, max_distance

# Retrieve the outputs
tour, total_travel_cost, max_distance_between_consecutive_cities = calculate_travel_plan(coordinates)

# Display results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance_between_consecutive_cities:.2f}")