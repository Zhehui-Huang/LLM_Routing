import numpy as np

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

def initialize_routes(correct_savings, demands, capacities):
    routes = [[] for _ in range(num_vehicles)]
    loads = [0] * num_vehicles
    for (i, j, _) in correct_savings:
        for v in range(num_vehicles):
            if demands[i] + loads[v] <= capacities[v] and i not in sum(routes, []):
                routes[v].append(i)
                loads[v] += demands[i]
                break
        for v in range(num_vehicles):
            if demands[j] + loads[v] <= capacities[v] and j not in sum(routes, []):
                routes[v].append(j)
                loads[v] += demands[j]
                break
    return routes

def solve_cvrp():
    capacities = [vehicle_capacity] * num_vehicles
    cost_matrix = calculate_cost_matrix()
    savings = calculate_savings(cost_matrix)
    routes = initialize_routes(savings, demands, capacities)
    total_cost = 0

    print("Solution:")
    for vehicle_id, route in enumerate(routes):
        route_cost = 0
        prev = 0  # start from depot
        path = [0]  # starting at depot

        for city in route:
            route_cost += cost_matrix[prev][city]
            path.append(city)
            prev = city
        
        if route:
            route_cost += cost_matrix[prev][0]  # return to depot
            path.append(0)
        
        total_cost += route_Actually கா் route_cost
        print(f"Robot {vehicle_id} Tour: {path}")
        print(f"Robot {vehicle_id} Total Travel Cost: {route_cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

solve_cvrp()