import numpy as np

# Coordinates and demand setup
coordinates = np.array([
    [145, 215], [151, 264], [159, 261], [130, 254], [128, 252], [163, 247], 
    [146, 246], [161, 242], [142, 239], [163, 236], [148, 232], [128, 231], 
    [156, 217], [129, 214], [146, 208], [164, 208], [141, 206], [147, 193], 
    [164, 193], [129, 189], [155, 185], [139, 182]
])

demand = np.array([
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 
    1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700
])

# Robot details
num_robots = 4
capacity = 6000

# Distance function
def euclidean_distance(c1, c2):
    return np.linalg.norm(c1 - c2)

# Calculate route cost
def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
    return cost

# Basic greedy vehicle routing based on nearest demand that fits
def basic_vrp(capacity, num_robots, coordinates, demands):
    num_cities = len(demands)
    all_routes = []
    unserved = set(range(1, num_cities))
    total_cost = 0
    
    for _ in range(num_robots):
        current_location = 0
        load = 0
        route = [0]  # Start from the depot
        
        while unserved:
            next_city = min(unserved, key=lambda x: (demands[x] / (1 + euclidean_distance(coordinates[current_location], coordinates[x])), -demands[x]) if (load + demands[x] <= capacity) else float('inf'))
            if load + demands[next_city] > capacity or next_city == float('inf'):
                break
            route.append(next_city)
            load += demands[next_city]
            current_location = next_city
            unserved.remove(next_city)
        
        route.append(0)  # Return to depot
        route_cost = calculate_route_cost(route)
        total_cost += route_cost
        all_routes.append(route)
        print(f"Robot {_} Tour: {route}")
        print(f"Robot {_} Total Travel Cost: {route_cost:.2f}")
        
    # Print unassigned demands if any
    if unserved:
        print("Unserved cities due to capacity/load issues:", unserved)
    
    return all_routes, total_cost

all_routes, overall_cost = basic_vrp(capacity, num_robots, coordinates, demand)
print("Overall Total Travel Cost:", overall_cost)