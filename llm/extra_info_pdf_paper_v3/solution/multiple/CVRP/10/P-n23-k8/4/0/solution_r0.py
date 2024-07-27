import math
import random
from collections import namedtuple

City = namedtuple("City", ["index", "x", "y", "demand"])

def euclidean_distance(city1, city2):
    return math.sqrt((city1.x-city2.x)**2 + (city1.y-city2.y)**2)

def load_cities():
    cities = [
        City(0, 30, 40, 0),
        City(1, 37, 52, 7),
        City(2, 49, 49, 30),
        City(3, 52, 64, 16),
        City(4, 31, 62, 23),
        City(5, 52, 33, 11),
        City(6, 42, 41, 19),
        City(7, 52, 41, 15),
        City(8, 57, 58, 28),
        City(9, 62, 42, 8),
        City(10, 42, 57, 8),
        City(11, 27, 68, 7),
        City(12, 43, 67, 14),
        City(13, 58, 48, 6),
        City(14, 58, 27, 19),
        City(15, 37, 69, 11),
        City(16, 38, 46, 12),
        City(17, 61, 33, 26),
        City(18, 62, 63, 17),
        City(19, 63, 69, 6),
        City(20, 45, 35, 15),
        City(21, 32, 39, 5),
        City(22, 56, 37, 10)
    ]
    return cities

def greedy_partition(cities, num_robots, max_capacity):
    routes = [[] for _ in range(num_robots)]
    demands = [0] * num_robots
    city_queue = sorted(cities[1:], key=lambda c: c.demand, reverse=True)
    
    for city in city_queue:
        best_robot = min(range(num_robots), key=lambda i: demands[i] if demands[i] + city.demand <= max_capacity else float('inf'))
        if demands[best_robot] + city.demand <= max_capacity:
            routes[best_robot].append(city.index)
            demands[best_robot] += city.demand
    
    return routes

def compute_route_cost(route, cities):
    cost = 0
    last_city = cities[0]  # depot
    for city_index in route:
        current_city = next(city for city in cities if city.index == city_index)
        cost += euclidean_distance(last_city, current_city)
        last_city = current_city
    cost += euclidean_distance(last_city, cities[0])  # return to depot
    return cost

cities = load_cities()
num_robots = 8
max_capacity = 40
routes = greedy_partition(cities, num_robots, max_capacity)

overall_cost = 0

# Output format adjustment
for robot_id, route in enumerate(routes):
    full_route = [0] + route + [0]
    route_cost = compute_route_cost(route, cities)
    overall_cost += route_cost
    print(f"Robot {robot_id} Tour: {full_route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")