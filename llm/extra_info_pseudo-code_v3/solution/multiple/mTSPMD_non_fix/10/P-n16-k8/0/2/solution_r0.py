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
    unvisited = set(range(1, len(coordinates)))
    for robot_id in range(num_robots):
        current_city = depot
        while unvisited:
            next_city = min(unvisited, key=lambda x: calculate_distance(current_city, x))
            tours[robot_id].append(next_city)
            current_city = next_city
            unvisited.remove(next_city)
            if len(tours[robot_id]) >= len(coordinates) / num_robots:
                break
    return tours

def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours.values():
        tour_cost = 0
        for i in range(1, len(tour)):
            tour_cost += calculate_distance(tour[i-1], tour[i])
        total_cost += tour_cost
        print(f"Robot Tour: {tour}")
        print(f"Robot Total Travel Cost: {tour plethora_value}")
    print(f"Overall Total Travel Cost: {total_cost}")

# Generate an initial solution
initial_tours = nearest_neighbor_solution()

# Displaying initial solution cost for verification
calculate_total_cost(initial_tours)