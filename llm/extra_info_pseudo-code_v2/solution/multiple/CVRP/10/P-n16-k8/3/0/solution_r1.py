import numpy as, np

# Coordinates and demands (includes the Depot at index 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Vehicle information
num_vehicles = 8
vehicle_capacity = 35

def euclidean_distance(c1, c2):
    return np.linalg.norm(np.array(c1) - np.array(c2))

def calculate_cost_matrix():
    num_cities = len(coordinates)
    cost_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                cost_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
            else:
                cost_matrix[i][j] = float('inf')
    return cost_matrix

def calculate_savings(cost_matrix):
    num_cities = len(cost_matrix)
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append((s, i, j))
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

def greedy_vehicle_assignment(num_vehicles, vehicle_capacity, savings, demands):
    routes = [[] for _ in range(num_vehicles)]  # Vehicle routes
    remaining_capacity = [vehicle_capacity] * num_vehicles  # Capacity tracking
    assigned = set()  # Track assigned cities

    for _, i, j in savings:
        for v in range(num_vehicles):
            if demands[i] <= remaining_capacity[v] and i not in assigned:
                if demands[j] <= remaining_capacity[v] - demands[i] and j not in assigned:
                    routes[v].extend([i, j])
                    remaining_capacity[v] -= (demands[i] + demands[j])
                    assigned.update([i, j])
                    break
                elif j not in assigned:
                    routes[v].append(i)
                    remaining_capacity[v] -= demands[i]
                    assigned.add(i)
                    break

    # Assign remaining unassigned cities
    for city in range(1, len(demands)):
        if city not in assigned:
            for v in range(num_vehicles):
                if demands[city] <= remaining_capacity[v]:
                    routes[v].append(city)
                    remaining_capacity[v] -= demands[city]
                    assigned.add(city)
                    break

    return routes

def print_solution(routes, cost_matrix):
    total_cost = 0
    for i, route in enumerate(routes):
        route_cost = sum(cost_matrix[route[j]][route[j + 1]] for j in range(len(route) - 1))
        route = [0] + route + [0]
        route_cost += cost_matrix[0][route[1]] + cost_matrix[route[-2]][0]
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Total Travel Cost: {route_cost:.2f}")
        total_cost += route_cost
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

def solve_cvrp():
    cost_matrix = calculate_cost_matrix()
    savings = calculate_savings(cost_matrix)
    routes = greedy_vehicle_assignment(num_vehicles, vehicle_capacity, savings, demands)
    print_solution(routes, cost_matrix)

solve_cvrp()