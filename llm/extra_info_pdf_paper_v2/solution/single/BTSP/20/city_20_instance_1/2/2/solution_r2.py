import math
import random

# City coordinates setup
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Nearest Neighbour Heuristic to start generating a tour
def nearest_neighbour_tour(start_city):
    remaining_cities = set(range(len(cities)))
    tour = [start_city]
    remaining_cities.remove(start_city)
    current_city = start_city

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)

    tour.append(start_city)  # return to the depot
    
    return tour

# Analyze the tour generated to find the required maximum consecutive distance
def analyze_tour(tour):
    max_distance = 0
    total_cost = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_distance(tour[i], tour[i + 1])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    return max_distance, total_cost

# Run the heuristic to find a tour from the depot
tour = nearest_neighbour_tour(0)
max_dist, total_cost = analyze_tour(tour)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)