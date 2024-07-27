import numpy as np
from scipy.spatial.distance import cdist
from collections import namedtuple

# Define the City with attributes id, coordinates (x, y), and demand.
City = namedtuple('City', 'id coordinates demand')

# Define the cities and their demand.
cities = [
    City(0, (30, 40), 0),
    City(1, (37, 52), 7),
    City(2, (49, 49), 30),
    City(3, (52, 64), 16),
    City(4, (31, 62), 23),
    City(5, (52, 33), 11),
    City(6, (42, 41), 19),
    City(7, (52, 41), 15),
    City(8, (57, 58), 28),
    City(9, (62, 42), 8),
    City(10, (42, 57), 8),
    City(11, (27, 68), 7),
    City(12, (43, 67), 14),
    City(13, (58, 48), 6),
    City(14, (58, 27), 19),
    City(15, (37, 69), 11),
    City(16, (38, 46), 12),
    City(17, (61, 33), 26),
    City(18, (62, 63), 17),
    City(19, (63, 69), 6),
    City(20, (45, 35), 15)
]

robot_capacity = 160
number_of_robots = 2

# Calculate the distance matrix.
coordinates = [city.coordinates for city in cities]
distance_matrix = cdist(coordinates, coordinates, metric='euclidean')

def initial_solution_construction(depot, cities, robot_capacity, number_of_robots):
    routes = [[] for _ in range(number_of_robots)]
    loads = [0] * number_of_robots
    remaining_cities = set(cities[1:])  # Exclude the depot
    active_robot = 0

    while remaining_cities:
        current_city = cities[depot] if not routes[active_robot] else routes[active_robot][-1]
        next_city = min(remaining_cities, key=lambda city: distance_matrix[current_city.id][city.id])
        
        if loads[active_robot] + next_city.demand <= robot_capacity:
            routes[active_robot].append(next_city)
            loads[active_robot] += next_city.demand
            remaining_cities.remove(next_city)
        else:
            active_robot = (active_robot + 1) % number_of_robots
            if all(loads[i] + next_city.demand > robot_capacity for i in range(number_of_robots)):
                break
    
    # Add depot to start and end of each route.
    for route in routes:
        route.insert(0, cities[depot])
        route.append(cities[depot])

    return routes

# Construct the initial solution
routes = initial_solution_construction(0, cities, robot_capacity, number_of_robots)

# Function to calculate the travel cost of each route.
def calculate_travel_cost(route):
    return sum(distance_matrix[route[i].id][route[i+1].id] for i in range(len(route)-1))

# Calculate the total cost and print the route information.
total_cost = 0

for i, route in enumerate(routes):
    route_indices = [city.id for city in route]
    route_cost = calculate_travel_temp(route)
    total_cost += route_cost
    print(f'Robot {i} Tour: {route_indices}')
    print(f'Robot {i} Total Travel Cost: {route_cost:.2f}')

print(f'Overall Total Travel Cost: {total_cost:.2f}')