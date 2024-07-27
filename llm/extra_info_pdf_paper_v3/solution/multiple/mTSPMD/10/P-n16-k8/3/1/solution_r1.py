import numpy as np
import random
from math import sqrt

# Define cities by coordinates [id: (x, y)]
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

def calculate_distance(city1, city2):
    """ Calculates Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def initial_population(number_of_salesmen):
    """ Generates initial routes for each robot starting and ending at their respective depots """
    all_cities = set(cities.keys())
    depot_cities = set(range(number_of_salesmen))
    worker_cities = list(all_cities - depot_cities)
    random.shuffle(worker_cities)

    # Slice the worker cities for each salesman evenly
    chunk_size = len(worker_cities) // number_of_salesmen
    routes = {i: [i] for i in range(number_of_salesmen)}
    chunks = [worker_cities[i:i + chunk_size] for i in range(0, len(worker_cities), chunk_size)]

    for i, chunk in enumerate(chunks):
        routes[i] += chunk + [i]  # Start and end at the depot

    return routes

def calculate_route_distance(route):
    """ Calculates total distance for a given route """
    return sum(calculate_distance(route[i], route[i + 1]) for i in range(len(route) - 1))

def total_route_costs(routes):
    """ Calculates costs for all routes and returns individual and combined costs """
    individual_costs = {}
    total_cost = 0
    for salesman, route in routes.items():
        cost = calculate_route_distance(route)
        individual_costs[salesman] = (route, cost)
        total_cost += cost
    return individual_costs, total_cost

# Number of salesmen (robots)
number_of_salesmen = 8

# Generate initial population
routes = initial_population(number_of_salesmen)

# Calculate and print routes with costs
individual_costs, total_cost = total_route_costs(routes)

for robot, (route, cost) in individual_costs.items():
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Spitfire Cost: {total_cost}")