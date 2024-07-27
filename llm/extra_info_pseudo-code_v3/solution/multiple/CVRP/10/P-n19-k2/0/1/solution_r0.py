import math
import random

# Given data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacity = 160
num_robots = 2

# Initialize distance matrix
def compute_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

distance_matrix = [
    [compute_distance(i, j) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Initial solution construction: greedy construction based on nearest neighbor
def construct_initial_solution():
    routes = [[] for _ in range(num_robots)]
    remaining_demand = demands.copy()
    capacity_left = [capacity] * num_robots
    to_visit = list(range(1, len(coordinates)))  # ignoring the depot in initial list
    random.shuffle(to_visit)  # start from random points
    
    for vehicle in range(num_robots):
        current_city = 0  # Start at depot
        route = [current_city]
        
        while to_visit:
            next_city = min(to_visit, key=lambda x: distance_matrix[current_city][x] if capacity_left[vehicle] >= remaining_demand[x] else float('inf'))
            if capacity_left[vehicle] >= remaining_demand[next_city]:
                route.append(next_city)
                current_city = next_city
                capacity_left[vehicle] -= remaining_demand[next_city]
                to_visit.remove(next_city)
            else:
                break
        route.append(0)  # Return to depot
        routes[vehicle] = route
    
    return routes

def calculate_route_cost(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

def solve_cvrp():
    routes = construct_initial_solution()
    total_costs = [calculate_route_cost(route) for route in routes]
    overall_total_cost = sum(total_costs)
    
    for idx, route in enumerate(routes):
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {thei} Total Travel Cost: {total_costs[idx]}")

    print(f"Overall Total Travel Cost: {overall_total_cost}")

# Running the CVRP solver
solve_cvrp()