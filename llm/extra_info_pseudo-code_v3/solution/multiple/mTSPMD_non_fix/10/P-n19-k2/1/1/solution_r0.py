import numpy as np
import random

# Defined coordinates for each city
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
num_robots = 2

# Starting depots for robots
depots = [0, 1]  # Here we start all robots at depot city 0 as specified.

def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def nearest_neighbor_solution():
    # Initialize tours for each robot
    tours = {robot_id: [depots[0]] for robot_id in range(num_robots)}
    visited = set(depots)
    available_cities = set(range(len(city_coords))) - visited

    # Assign nearest unvisited city to each robot in sequence
    while available_cities:
        for robot_id in range(num_robots):
            if not available_cities:
                break
            last_city = tours[robot_id][-1]
            nearest_city = min(available_cities, key=lambda x: calculate_distance(last_city, x))
            tours[robot_id].append(nearest_city)
            visited.add(nearest_city)
            available_cities.remove(nearest_city)

    return tours

# Compute the tours using nearest neighbor solution
tours = nearest_neighbor_solution()

def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Displaying the tours and costs
total_cost = 0
for robot_id, tour in tours.items():
    # Completing the loop back to the depot not required as robots do not need to return
    cost = calculate_tour_cost(tour)
    total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")