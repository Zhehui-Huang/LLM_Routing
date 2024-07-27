import numpy as np
from math import sqrt

def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

# Implementing a simple greedy solution to split routes by demand and then optimize the route
def greedy_cvrp(coordinates, demands, num_robots, robot_capacity):
    unvisited = list(range(1, len(coordinates)))
    tours = [[] for _ in range(num_robots)]
    capacities = [robot_capacity] * num_robots
    
    for robot in range(num_robots):
        tours[robot].append(0)  # Start at the depot
        current_load = 0
        new_tour = []
        
        for city in unvisited[:]:  # Use [:] to make a copy of unvisited list
            if demands[city] + current_load <= capacities[robot]:
                new_tour.append(city)
                current_load += demands[city]
                unvisited.remove(city)
        
        # Append cities and end at the depot
        tours[robot] += new_tour + [0]
        capacities[robot] -= current_load

    return tours

tours = greedy_cvrp(coordinates, demands, num_robots, robot_capacity)

# Calculate costs and output the results
overall_cost = 0
for robot, tour in enumerate(tours):
    tour_cost = calculate_total_distance(tour, coordinates)
    overall_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")