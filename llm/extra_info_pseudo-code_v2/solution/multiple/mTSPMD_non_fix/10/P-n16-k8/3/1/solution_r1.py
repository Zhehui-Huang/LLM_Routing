import numpy as np
import random
from itertools import permutations

# City coordinates
coordinates = {i: coord for i, coord in enumerate([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)])}

# Calculate Euclidean distance
def distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Calculate total distance of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Greedily construct a tour starting from the initial city
def greedy_tour(initial_city, unvisited):
    tour = [initial_city]
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(tour[-1], city))
        tour.append(next_city)
        unvisited.remove(next_city)
    return tour

# Solving the problem for 'num_robots' robots starting from the same depot
def solve_tsp_with_robots(num_robots):
    unvisited_cities = list(coordinates.keys())
    num_cities = len(unvisited_cities)
    overall_tours = []
    overall_cost = 0
    
    for robot in range(num_robots):
        if not unvisited_cities:
            break
        current_city = unvisited_cities.pop(0)  # Start from the next unvisited city
        if robot == num_robots - 1:
            # Last robot gets the remaining cities
            tour = greedy_tour(current_city, unvisited_cities)
        else:
            # Each robot handles approximately equal number of cities
            robot_cities = [current_city] + random.sample(unvisited_cities, (num_cities // num_robots) - 1)
            unvisited_cities = [city for city in unvisited_cities if city not in robot_cities]
            tour = greedy_tour(current_city, robot_cities[:-1])
        
        tour.append(tour[0])  # Return to start depot
        tour_cost = total_distance(tour)
        overall_cost += tour_cost
        
        print(f"Robot {robot} Tour: {tour}")
        print(f"Robot {robot} Total Travel Cost: {tour_cost}")
        overall_tours.append(tour)
    
    print("Overall Total Travel Cost:", overall_cost)

solve_tsp_with_robots(8)