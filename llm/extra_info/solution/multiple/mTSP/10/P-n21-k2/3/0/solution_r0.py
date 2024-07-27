import math
from itertools import permutations

# City coordinates, including the depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Calculate Euclidean distance between two city coordinates
def distance(city1, city2):
    return math.sqrt((coordinates[city2][0] - coordinates[city1][0]) ** 2 + (coordinates[city2][1] - coordinates[city1][1]) ** 2)

# Using Nearest Neighbor Strategy to solve TSP for individual robot
def nearest_neighbor_tour(start, cities):
    unvisited = set(cities)
    tour = [start]
    current = start
    
    while len(unvisited) > 0:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    tour.append(start)  # return to the depot
    return tour

def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Splitting the cities roughly into two equal parts (simplest heuristic)
robot_0_cities = [1, 2, 3, 4, 5, 6, 9, 13, 17, 18, 19]
robot_1_cities = [7, 8, 10, 11, 12, 14, 15, 16, 20]

# Calculating tours for each robot
robot_0_tour = nearest_neighbor_tour(0, robot_0_cities)
robot_1_tour = nearest_neighbor_tour(0, robot_1_cities)

# Calculating the costs for each tour
robot_0_cost = calculate_tour_cost(robot_0_tour)
robot_1_cost = calculate_tour_cost(robot_1_tour)

# Displaying the results
print("Robot 0 Tour:", robot_0_tour)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("\nRobot 1 Tour:", robot_1_tour)
print("Robot 1 Total Travel Cost:", robot_1_cost)

overall_total_cost = robot_0_cost + robot_1_cost
print("\nOverall Total Travel Cost:", overall_total_cost)