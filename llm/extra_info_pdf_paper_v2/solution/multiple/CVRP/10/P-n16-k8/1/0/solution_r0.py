import math
import random

# Define the data structures for cities and demands
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35
num_cities = len(cities_coordinates)


def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities,coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# Initialize routes for each robot
robots_routes = [[] for _ in range(num_robots)]
remaining_demands = demands.copy()

# Starting the Enhanced Clarke-Wright Savings Algorithm for CVRP

# Calculate savings for each pair of cities
savings = []
for i in range(1, num_cities):
    for j in range(i + 1, num_cities):
        if i != j:
            s_ij = euclidean_distance(0, i) + euclidean_distance(0, j) - euclidean_distance(i, j)
            savings.append((s_ij, i, j))
savings.sort(reverse=True, key=lambda x: x[0])


def can_add_to_route(route, city, demand):
    if len(route) == 0:
        return True  # Empty route can always accept a new city
    current_load = sum(remaining_demands[c] for c in route)
    new_load = remaining_demands[city]
    return current_load + new_load <= robot_capacity

# Assign routes based on the savings
for _, city1, city2 in savings:
    if remaining_demands[city1] > 0 and remaining_demands[city2] > 0:
        added = False
        for route in robots_routes:
            if can_add_to_route(route, city1, remaining_demands) and can_add_to_route(route, city2, remaining_demblems):
                if city1 not in route and city2 not in route:
                    route.extend([city1, city2])
                    remaining_demands[city1] = 0
                    remaining_demands[city2] = 0
                    added = True
                    break
        if not added:
            # Try to start a new route
            for route in robots_routes:
                if len(route) == 0:
                    route.extend([city1, city2])
                    remaining_demands[city1] = 0
                    remaining_demands[city2] = 0
                    break

# Fill any remaining demands
for i in range(1, num_cities):
    if remaining_demands[i] > 0:
        for route in robots_routes:
            if can_add_to_route(route, i, remaining_demandoles):
                route.append(i)
                remaining_demands[i] = 0
                break

# Wrap each route with the depot city
for route in robots_routes:
    if route:
        route.insert(0, 0)
        route.append(0)

# Calculate route costs
robots_costs = []
total_cost = 0
for route in robots_routes:
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(route[i], route[i+1])
    robots_costs.append(cost)
    total_cost += cost

# Output the results
for i, (route, cost) in enumerate(zip(robots_routes, robots_costs)):
    if route:
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Costs: {total_cost}")