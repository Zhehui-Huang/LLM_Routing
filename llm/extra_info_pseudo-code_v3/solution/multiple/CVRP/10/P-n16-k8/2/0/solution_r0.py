import numpy as np
from math import sqrt
from random import sample, randint, random
from sklearn.utils import shuffle

# Given data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35

# Distance matrix calculation
def euclidean(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = np.array([[euclidean(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))])

# Initial feasible solution generator
def generate_initial_solution(demand_list, robot_cap, num_vehicles, dist_matrix):
    routes = [[] for _ in range(num_vehicles)]
    current_capacity = [0] * num_vehicles
    available_cities = set(range(1, len(demand_list)))  # exclude depot initially
    
    # Round-robin assignment based on capacity
    vehicle_idx = 0
    while available_cities:
        current_city = available_cities.pop()
        if current_capacity[vehicle_idx] + demand_list[current_city] <= robot_cap:
            if not routes[vehicle_idx]:
                routes[vehicle_idx].append(0)  # starting from depot if empty
            routes[vehicle_idx].append(current_city)
            current_capacity[vehicle_idx] += demand_list[current_city]
            routes[vehicle_idx].append(0)  # return to depot
        else:
            available_cities.add(current_city)  # Put it back, try next vehicle
        vehicle_idx = (vehicle_idx + 1) % num_vehicles
        
    # Making sure each route is valid by checking capacities
    for idx in range(num_vehicles):
        if sum(demand_list[city] for city in routes[idx] if city > 0) > robot_cap:
            return generate_initial_solution(demand_list, robot_cap, num_vehicles, dist_matrix)  # regenerate if invalid
    return routes

initial_routes = generate_initial_solution(demands, robot_capacity, num_robots, distance_matrix)

# Calculate route costs
def calculate_route_cost(route, dist_matrix):
    return sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

def print_solution(routes, dist_matrix):
    total_cost = 0
    for idx, route in enumerate(routes):
        cost = calculate_route_cost(route, dist_matrix)
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")
        total_cost += cost
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

print_solution(initial_routes, distance_matrix)