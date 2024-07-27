import math
from itertools import permutations

# Define the cities and their coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# City demands
city_demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28,
    8, 8, 7, 14, 6, 19, 11, 12, 26,
    17, 6, 15
]

# Number of robots and their capacity
number_of_robots = 2
robot_capacity = 160

def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

# Compute distance matrix
distance_matrix = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(len(city_coords))] for i in range(len(city_coords))]

def find_routes():
    # Each robot will start its route from the depot
    all_routes = []
    remaining_cities = set(range(1, len(city_coords)))  # city 0 is the depot
    while remaining_cities:
        current_route = [0]  # start from depot
        total_demand = 0
        cities_to_remove = []
        
        for city in remaining_cities:
            if total_demand + city_demands[city] <= robot_capacity:
                if len(current_route) > 1:   # Checks connection with last city in route
                    last_city = current_route[-1]
                else:   # First connection from depot
                    last_city = 0
                # Add city to current route
                current_route.append(city)
                total_demand += city_demands[city]
                cities_to_remove.append(city)
        
        # Closing the route to the depot
        current_route.append(0)
        
        # Remove the cities from remaining
        for city in cities_to_remove:
            remaining_cities.remove(city)
        
        # Store the completed route
        all_routes.append(current_route)
    
    return all_routes

def calculate_total_cost(routes):
    total_costs = []
    for route in routes:
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_costs.append(route_cost)
    return total_costs

routes = find_routes()
costs = calculate_total_cost(routes)

overall_total_cost = sum(costs)

for idx, (route, cost) in enumerate(zip(routes, costs)):
    robot_id = idx % number_of_robots
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")