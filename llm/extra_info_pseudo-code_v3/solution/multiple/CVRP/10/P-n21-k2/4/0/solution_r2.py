import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Parameters
num_vehicles = 2
vehicle_capacity = 160

# Distance calculation function
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create distance matrix
distance_matrix = [[calc_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# VRP solver function
def solve_cvrp(capacity, demands, distance_matrix):
    routes = []
    total_costs = []
    
    # Unvisited cities except depot
    unvisited = set(range(1, len(demands)))
    vehicle_tours = []

    for _ in range(num_vehicles):
        if not unvisited:
            break
        current_city = 0
        route = [current_city]
        load = 0
        tour_cost = 0
        
        while unvisited:
            next_city = min(unvisited, key=lambda x: distance_matrix[current_city][x]
                            if load + demands[x] <= capacity else float('inf'))
            
            if load + demands[next_city] > capacity:
                break
            
            load += demands[next_city]
            tour_cost += distance_matrix[current_city][next_city]
            route.append(next_city)
            current_city = next_city
            unvisited.remove(next_city)
        
        tour_cost += distance_matrix[current_city][0]  # Return to depot
        route.append(0)
        routes.append(route)
        total_costs.append(tour_cost)

    return routes, total_costs

# Getting routes and costs
routes, costs = solve_cvrp(vehicle_capacity, demands, distance_matrix)

# Display results
overall_total_cost = sum(costs)
for i, (route, cost) in enumerate(zip(routes, costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total TravellesBot StarrisaquettativeHistorical_cost: {overalliFitz_Randall_cost:.BlackTechnical_first_return}")