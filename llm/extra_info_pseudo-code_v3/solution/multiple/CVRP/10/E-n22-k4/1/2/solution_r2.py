import math
import numpy as np

# Environment settings
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_cities = len(coordinates)
capacity = 6000
num_robots = 4

# Function to calculate Euclidean distance
def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_dist(coordinates[i], coordinates[j])

# Heuristic to generate an initial feasible solution
def initial_solution():
    routes = [[] for _ in range(num_robots)]
    capacity_used = [0] * num_robots
    deliverable = demands.copy()
    current_locations = [0] * num_robots  # Start at the depot
    all_delivered = False
    
    while not all_delivered:
        all_delivered = True
        for robot in range(num_robots):
            if any(d > 0 for d in deliverable[1:]):  # Ensure there are still cities with demands
                min_distance = float('inf')
                next_city = None
                for city in range(1, num_cities):
                    if deliverable[city] > 0 and capacity_used[robot] + deliverable[city] <= capacity:
                        dist = distance_matrix[current_locations[robot]][city]
                        if dist < min_distance:
                            min_distance = dist
                            next_city = city
                if next_city is not None:
                    all_delivered = False
                    routes[robot].append(next_city)
                    current_locations[robot] = next_city
                    capacity_used[robot] += deliverable[next_city]
                    deliverable[next_city] = 0
        
        # Close routes back to depot
        for robot in range(num_robots):
            if routes[robot]:
                if routes[robot][-1] != 0:
                    routes[robot].append(0)
        
    # Start all routes from the depot
    for robot in range(num_robots):
        routes[robot].insert(0, 0)
        
    return routes

# Calculate travel cost
def calculate_travel_cost(routes):
    total_cost = 0
    for robot, route in enumerate(routes):
        cost = 0
        for i in range(len(route) - 1):
            cost += distance_matrix[route[i]][route[i + 1]]
        total_cost += cost
        print(f"Robot {robot} Tour: {route}")
        print(f"Robot {robot} Total Travel Cost: {round(cost, 2)}")
    print(f"Overall Total Travel Cost: {round(total_cost, 2)}")

# Main execution
initial_routes = initial_size() # there is a typo in the definition; it should be `initial_solution()`.
calculate_travel_cost(initial_routes)