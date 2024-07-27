import math
import itertools

# Coordinates of cities
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate the total travel cost of a tour
def calculate_total_travel_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Initial distribution of cities to robots
cities_per_robot = [[] for _ in range(num_robots)]
current_robot = 0
for city_index in range(1, len(cities)):  # start from 1 to skip the depot
    cities_per_robot[current_robot].append(city_index)
    current_robot = (current_robot + 1) % num_robots

# Function to create a tour for each robot using initial greedy approach
def initial_tour(cities_indices):
    tour = [0]  # start at the depot
    tour.extend(cities_indices)
    tour.append(0)  # end at the depot
    return tour

# Generate and calculate tours for each robot
tours = [initial_tour(robot_cities) for robot_cities in cities_per_robot]
tour_costs = [calculate_total_travel_cost(tour) for tour in tours]
overall_total_cost = sum(tour_costs)

# Output results
for robot_id, tour in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")