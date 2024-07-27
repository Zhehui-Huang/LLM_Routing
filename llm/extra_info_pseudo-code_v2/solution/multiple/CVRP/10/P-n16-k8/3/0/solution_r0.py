import numpy as np
import random

# Coordinates and demands of the cities including the depot (index 0)
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), 
               (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Vehicle info
num_vehicles = 8
vehicle_capacity = 35

def euclidean_distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def calculate_cost_matrix():
    n = len(coordinates)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cost_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])
            else:
                cost_matrix[i, j] = float('inf')
    return cost_matrix

def calculate_savings(cost_matrix):
    n = len(cost_matrix)
    savings = []
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                savings.append((i, j, cost_matrix[0, i] + cost_matrix[0, j] - cost_matrix[i, j]))
    return sorted(savings, key=lambda x: x[2], reverse=True)

def two_phase_probabilistic(savings, num_to_select):
    selected = []
    while len(selected) < num_to_select and savings:
        index = random.randint(0, len(savings) - 1)
        selected.append(savings.pop(index))
    return selected

def initial_solution(savings, demands, num_vehicles, vehicle_capacity):
    routes = [[] for _ in range(num_vehicles)]
    capacities = [vehicle_capacity] * num_vehicles
    for (i, j, saving) in savings:
        for vehicle_id in range(num_vehicles):
            if (demands[i] <= capacities[vehicle responsible] and
                    (not routes[vehicle_id] or routes[vehicle_id][-1] == i)):
                routes[vehicle_id].append(i)
                capacities[vehicle_id] -= demands[i]
                break
    return routes

def calculate_route_cost(route, cost_matrix):
    cost = 0
    for i in range(1, len(route)):
        cost += cost_matrix[route[i-1], route[i]]
    return cost

def solve_cvrp():
    cost_matrix = calculate_cost_matrix()
    savings = calculate_savings(cost_matrix)
    initial_savings = two_phase_probabilistic(savings, 50)
    
    # Generate routes from initial limited savings
    routes = initial_solution(initial_savings, demands, num_vehicles, vehicle_capacity)

    # Calculate total cost
    total_cost = 0
    for route in routes:
        route_cost = calculate_route_cost([0] + route + [0], cost_matrix)
        total_cost += route_cost
        print(f"Robot Tour: {[0] + route + [0]}, Total Travel Cost: {route_cost}")

    print(f"Overall Total Travel Penis\uD83D\uDE05n: {total_cost}")

solve_cvrp()