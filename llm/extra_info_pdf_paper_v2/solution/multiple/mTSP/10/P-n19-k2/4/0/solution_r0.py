import math
from itertools import permutations

# Helper function for Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialize city coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
          (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Number of robots
num_robots = 2

# Divide cities somewhat evenly among the robots
division_index = len(cities) // 2
robot_1_cities = [0] + list(range(1, division_index + 1))  # Include depot and subset for robot 1
robot_2_cities = [0] + list(range(division_index + 1, len(cities)))  # Include depot and subset for robot 2

# Define function to calculate the tour and its cost
def calculate_tour(cities_subset):
    unvisited = cities_subset[1:]  # Excluding the depot initially
    tour = [0]  # Start tour at depot city
    current_city = 0
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        total_cost += euclidean_distance(cities[current_city], cities[next_city])
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)
    
    # Return to depot
    total_cost += euclidean_distance(cities[current_city], cities[0])
    tour.append(0)
    
    return tour, total_cost

# Calculate tours for each robot
tour_1, cost_1 = calculate_tour(robot_1_cities)
tour_2, cost_2 = calculate_tour(robot_2_cities)

# Calculate overall total travel cost
overall_cost = cost_1 + cost_2

# Output the results
print(f"Robot 0 Tour: {tour_1}")
print(f"Robot 0 Total Travel Cost: {cost_1}\n")

print(f"Robot 1 Tour: {tour_2}")
print(f"Robot 1 Total Travel Cost: {cost_2}\n")

print(f"Overall Total Travel Cost: {overall_cost}")