import math
import numpy as np

# Given cities and their coordinates
city_positions = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}

# Given demand list for each city excluding depot
demands = {
   1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19,
   15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15, 21: 5, 22: 10
}

num_robots = 8
robot_capacity = 40

def euclidean_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Calculate the cost matrix and saving matrix
def compute_cost_and_savings():
    num_cities = len(city_positions)
    cost_matrix = [[0] * num_cities for _ in range(num_cities)]
    savings = []

    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                cost_matrix[i][j] = cost_matrix[j][i] = euclidean_distance(city_positions[i], city_positions[j])
                if i != 0 and j != 0:  # Calculate savings only for non-depot pairs
                    savings.append((cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j], i, j))

    return cost_matrix, sorted(savings, reverse=True, key=lambda x: x[0])

cost_matrix, savings = compute_cost_and_savings()

# Clarke-Wright algorithm implementation
def clarke_wright():
    routes = [[0, i, 0] for i in range(1, len(city_positions))]
    vehicle_loads = {i: demands[i] for i in range(1, len(cityy_positions))}

    while savings:
        s, i, j = savings.pop(0)
        # Find routes containing i and j
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        
        if route_i != route_j:
            # Check if they can be merged
            i_index = route_i.index(i)
            j_index = route_j.index(j)
            i_demand = sum(demands.get(k, 0) for k in route_i)
            j_demand = sum(demands.get(k, 0) for k in route_j)
            
            if i_index == len(route_i) - 2 and j_index == 1 and i_demand + j_demand - demands[0] <= robot_capacity:
                # Merge into one route
                new_route = route_i[:-1] + route_j[1:]
                routes.remove(route_i)
                routes.remove(route_j)
                routes.append(new_route)

    return routes

# Optimizing routes after initial creation
def optimize_routes(routes):
    # Simple optimization by checking the demand and swapping nodes if beneficial (for simplicity)
    optimized = True
    while optimized:
        optimized = False
        for r in range(len(routes)):
            route = routes[r]
            for i in range(1, len(route) - 2):
                for j in range(i + 2, len(route) - 1):
                    if cost_matrix[route[i - 1]][route[j]] + cost_matrix[route[i]][route[j + 1]] < cost_matrix[route[i - 1]][route[i]] + cost_matrix[route[j]][route[j + 1]]:
                        route[i:j + 1] = route[i:j + 1][::-1]
                        optimized = True
    return routes

routes = clarke_wright()
routes = optimize_routes(routes)

# Calculating the cost of the tours and printing them
def calculate_costs(routes):
    total_cost = 0
    for idx, route in enumerate(routes):
        cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        total_cost += cost
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

    print(f"Overall Total Travel Cost: {total_cost:.2f}")

calculate_costs(routes)