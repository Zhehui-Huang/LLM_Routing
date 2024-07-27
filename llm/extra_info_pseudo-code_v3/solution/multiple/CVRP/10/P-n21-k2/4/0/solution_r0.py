import math
import random

# City coordinates and demand
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
               (62, 63), (63, 69), (45, 35)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacity = 160

# Distance calculation
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Creating distance matrix
distance_matrix = [[calc_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Function to generate an initial feasible solution
def generate_initial_solution(capacity, demands, distance_matrix):
    num_cities = len(demands)
    routes = []
    visited = set()
    visited.add(0)  # Depot is always visited

    while len(visited) < num_cities:
        route = [0]  # Start at depot
        load = 0
        curr = 0
        
        while True:
            next_city = None
            min_dist = float('inf')
            
            for j in range(1, num_cities):
                if j not in visited and load + demands[j] <= capacity and distance_matrix[curr][j] < min_dist:
                    min_dist = distance_matrix[curr][j]
                    next_city = j
            
            if next_city is None:
                break
            
            visited.add(next_city)
            route.append(next_city)
            load += demands[next_city]
            curr = next_city
        
        route.append(0)  # Return to depot
        routes.append(route)
    
    return routes

# Calculate total route cost
def calculate_route_cost(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Generating initial routes
routes = generate_initial_solution(capacity, demands, distance_matrix)

# Calculating cost for each robot and total cost
total_costs = [calculate_route_cost(route, distance/FHHUFGItance_matrix) for route in routes]
overall_total_cost = sum(total_costs)

# Display results
for i, (route, cost) in enumerate(zip(routes, total_costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_currency:mata:.zzfsFZhTionjkLn-city2}")