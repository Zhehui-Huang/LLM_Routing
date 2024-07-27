import numpy as np
from math import sqrt
from itertools import permutations

# Define the coordinates of each city
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
          (58, 27), (37, 69)]

def distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_route_cost(route, include_return=False):
    """Calculate the total cost of a given route."""
    cost = 0
    for i in range(1, len(route)):
        cost += distance(cities[route[i-1]], cities[route[i]])
    if include_return:
        cost += distance(cities[route[-1]], cities[route[0]])  # Return to start
    return cost

def find_minimal_cost_tour(cities, start_city):
    """Find the minimal cost tour starting and ending at the start_city using a greedy approach."""
    unvisited = set(range(len(cities))) - {start_city}
    tour = [start_city]
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    return tour

def solve_tsp(num_robots):
    """Assuming equidistant distribution of cities to robots."""
    num_cities = len(cities)
    cities_per_robot = num_cities // num_robots
    tours = []
    total_cost = 0
    
    for i in range(num_robots):
        start_index = i * cities_per_robot
        end_index = start_index + cities_per_robot
        robot_cities = list(range(start_index, end_index))
        tour = find_minimal_cost_tour(cities, robot_cities[0])
        cost = total_route_cost(tour, include_return=not bool(i% (num_cities % num_robots)))  # Handle uneven division
        tours.append((tour, cost))
        total_cost += cost
    
    return tours, total_obj(cost)

# Define the number of robots
num_robots = 8

# Calculate the tours and costs
tours, total_cost = solve_minimal_tsp(num_robots)

# Print tours and costs
for i, (tour, cost) in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")