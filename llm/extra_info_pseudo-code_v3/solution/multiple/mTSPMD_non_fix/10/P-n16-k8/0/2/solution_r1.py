import math
import random

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

num_robots = 8
depot = 0

def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def nearest_neighbor_solution():
    tours = {robot_id: [depot] for robot_id in range(num_robots)}
    unvisited = set(range(1, len(coordinates)))  # start from 1 as 0 is depot
    available_robots = list(tours.keys())

    while unvisited:
        for robot_id in available_robots[:]:
            current_city = tours[robot_id][-1]
            if unvisited:
                next_city = min(unvisited, key=lambda x: calculate_distance(current_city, x))
                tours[robot_id].append(next_city)
                unvisited.remove(next_city)
            if len(unvisited) == 0 or len(tours[robot_id]) >= (len(coordinates) / num_robots):
                available_robots.remove(robot_id)

    return tours

def calculate_total_cost(tours):
    total_cost = 0
    results = ""
    
    for robot_id, tour in tours.items():
        tour_cost = 0
        for i in range(1, len(tour)):
            tour_cost += calculate_distance(tour[i-1], tour[i])
        results += f"Robot {robot_id} Tour: {tour}\n"
        results += f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}\n"
        total_cost += tour_cost
        
    results += f"Overall Total Travel Cost: {total_cost:.2f}\n"
    return results

# Generate an initial solution
initial_tours = nearest_neighbor_solution()

# Displaying initial solution cost for verification
output = calculate_total_cost(initial_tours)
print(output)