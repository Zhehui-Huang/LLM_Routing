import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Parameters
capacity = 35
n_cities = len(coordinates)
n_robots = 8
depot = 0

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n_cities)] for i in range(n_cities)]

# CVRP Solver
def cvrp_solver():
    routes = []
    total_costs = []
    
    # Available robots initially
    available_robots = set(range(n_robots))
    
    # Cities to visit (excluding the depot)
    cities_to_visit = list(range(1, n_cities))
    
    # Deploy robots until no cities are left
    while cities_to_visit and available_robots:
        current_capacity = capacity
        current_robot_index = available_robots.pop()
        current_route = [depot]
        current_route_load = 0
        last_visited = depot
        
        # Build route for current robot
        while cities_to_visit and current_capacity > 0:
            # Find nearest city within the capacity constraint
            next_city = None
            min_distance = float('inf')
            for city in cities_to_visit:
                if distance_matrix[last_visited][city] < min_distance and demands[city] <= current_capacity:
                    min_distance = distance_matrix[last_visited][city]
                    next_city = city
            
            if next_city is None:
                break
            
            # Add city to route and adjust parameters
            current_route.append(next_city)
            current_route_load += demands[next_city]
            current_capacity -= demands[next_city]
            cities_to_visit.remove(next_city)
            last_visited = next_city
        
        # Return to depot and calculate costs
        current_route.append(depot)
        total_route_cost = 0
        for i in range(len(current_route) - 1):
            total_route_cost += distance_matrix[current_route[i]][current_route[i+1]]
        
        routes.append((current_robot_index, current_route))
        total_costs.append(total_route_cost)
    
    return routes, total_costs

# Execute CVRP solver
routes, total_costs = cvrp_solver()

# Output result
overall_cost = sum(total_costs)
for index, (robot_id, tour) in enumerate(routes):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[index]}")
print(f"Overall Total Travel Cost: {overall_cost}")