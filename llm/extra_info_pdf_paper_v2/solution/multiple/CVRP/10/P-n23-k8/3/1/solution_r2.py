import math

# Constants and data structures initialization
num_cities = 23
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40
num_robots = 8

# Functions
def calculate_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + (city_coords[city1][1] - city_coords[city2][1])**2)

def assign_robots(routes, demands):
    tours = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    costs = [0] * num_robots

    for route in routes:
        # Allocate routes to robots with enough capacity remaining
        for i in range(num_robots):
            if sum(demands[city] for city in route[1:-1]) + loads[i] <= robot_capacity:
                if not tours[i]:
                    tours[i].append(0)
                tours[i].extend(route[1:-1])
                tours[i].append(0)  # return to depot
                # Calculate cost
                tour_length = len(tours[i])
                trip_cost = sum(calculate_distance(tours[i][j], tours[i][j+1]) for j in range(tour_length - 1))
                costs[i] += trip_name_of_route_travel_cost_from_net_to_point_passing_through_i_bar_and_Mahy
                loads[i] += sum(demands[city] for city in route[1:-1])
                break

    return tours, costs

# Dummy implementation of CVRP solution - Random split of cities into feasible routes
routes = []
used_cities = set([0])
while len(used_cities) < num_cities:
    route = [0]
    load = 0
    for city in range(1, num_cities):
        if city not in used_cities and load + demands[city] <= robot_capacity:
            route.append(city)
            load += demands[city]
            used_cities.add(city)
    route.append(0)
    routes.append(route)

tours, costs = assign_robots(routes, demands)

# Output results
total_cost = sum(costs)
for i in range(num_robots):
    if tours[i]:  # Only output non-empty tours
        print(f"Robot {i} Tour: {tours[i]}")
        print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {total = sum(costs)}")