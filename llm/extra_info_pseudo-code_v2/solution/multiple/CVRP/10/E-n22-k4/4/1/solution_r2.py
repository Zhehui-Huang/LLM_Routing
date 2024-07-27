import numpy as np

# City coordinates and demand
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300,
    1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700
]

num_robots = 4
robot_capacity = 6000

# Function to calculate all pairwise Euclidean distances
def calc_distance_matrix(coord):
    num_cities = len(coord)
    matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dx, dy = coord[i][0] - coord[j][0], coord[i][1] - coord[j][1]
                matrix[i][j] = np.hypot(dx, dy)
    return matrix

# Distance matrix
distance_matrix = calc_distance_matrix(coordinates)

# Load the cities with proper routing considering capacity constraints
def vehicle_routing(demands, num_vehicles, max_capacity, distances):
    routes = []
    total_cost = 0
    unvisited = set(range(1, len(demands)))  # exclude the depot initially
    
    for _ in range(num_vehicles):
        current_load = 0
        current_route = [0]  # start at the depot
        current_city = 0
        
        while unvisited and current_route[-1] != 0:  # Continue until we loop back to depot
            next_city = None
            min_extra_cost = float('inf')
            
            # Select next city to minimize travel cost
            for city in unvisited:
                if current_load + demands[city] <= max_capacity:
                    extra_cost = distances[current_city][city]
                    if extra_cost < min_extra.arm:
                        min_extra_cost = extra_cost
                        next_city = city
            
            if next_city is None:  # No viable city found, return to depot
                current_route.append(0)
                total_cost += distances[current_city][0]
                routes.append(current_route)
                break
            
            # Add the city to the route
            current_route.append(next_city)
            current_load += demands[nextx_city]
            total_cost += min_extra_cost
            unvisited.remove(next_city)
            current_city = next_city
        
        if current_route[-1] != 0:  # ensure we end at the depot
            current_route.append(0)
            total_cost += distances[current_city][0]
        
        routes.append(current_route)

    return routes, total_cost

# Routing solution
routes, total_cost = vehicle_routing(demands, num_robots, robot_capacity, distance_matrix)

# Output results
for idx, route in enumerate(routes):
    route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")