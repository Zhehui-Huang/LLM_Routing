from math import sqrt
import random

# Define the cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

depots = [0, 1, 2, 3]
num_of_robots = 4
robot_start_locations = [0 for _ in range(num_of_robots)]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Nearest Neighbor Search for initial tour construction
def nearest_neighbor_solution(start_city):
    unvisited = set(range(len(coordinates)))
    tour = [start_city]
    unvisited.remove(start_city)

    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    return tour

# Generate initial tours for each robot, starting from the first depot
tours = {i: nearest_neighbor_solution(robot_start_locations[i]) for i in range(num_of_robots)}

# Assign remaining cities to the nearest robot tour
remaining_cities = set(range(len(coordinates))) - set(depots)
assigned_cities = set(x for tour in tours.values() for x in tour)
remaining_cities -= assigned_cities

while remaining_cities:
    for tour_id, tour in tours.items():
        if not remaining_cities:
            break
        # Find the closest city to the last city in the current tour
        last_city = tour[-1]
        next_city = min(remaining_cities, key=lambda city: distance(last_city, city))
        tour.append(next_city)
        remaining_cities.remove(next_city)

# Calculate the cost of each tour and the overall cost
total_cost = 0
result_output = ""
for robot_id, tour in tours.items():
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    # Append the depot to make them end where they start
    tour.append(robot_start_locations[robot_id])
    tour_cost += distance(tour[-2], tour[-1])
    result_output += f"Robot {robot_id} Tour: {tour}\n"
    result_output += f"Robot {robot_id} Total Travel Cost: {round(tour_cost, 2)}\n\n"
    total_cost += tour_cost

result_output += f"Overall Total Travel Cost: {round(total_cost, 2)}"

# Print the outputs
print(result_output)