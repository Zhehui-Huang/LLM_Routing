import numpy as np
from scipy.spatial.distance import cdist

# Define the cities and their coordinates.
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 68), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14,
    6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

num_vehicles = 8
vehicle_capacity = 40
depot_index = 0

# Calculate the Euclidean distance matrix
distance_matrix = cdist(coordinates, coordinates)

def find_next_city(current_city, remaining_capacity, demands, visited, distance_matrix):
    min_distance = float('inf')
    next_city = None
    for city in range(len(demands)):
        if city not in visited and demands[city] <= remaining_capacity and city != current_city:
            if distance_matrix[current_city][city] < min_distance:
                min_distance = distance_matrix[current_city][city]
                next_city = city
    return next_city

def compute_route(starting_city, demands, capacity, distance_matrix):
    current_city = starting_city
    route = [current_city]
    remaining_capacity = capacity
    visited = set(route)
    
    while len(visited) < len(demands):
        next_city = find_next_city(current_city, remaining_capacity, demands, visited, distance_matrix)
        if next_city is None:
            break
        # Visit the city
        route.append(next_city)
        visited.add(next_city)
        remaining_capacity -= demands[next_city]
        if remainingCapacity < min(demands[i] for i, d in enumerate(demands) if i not in visited):
            break
        current_city = next_city
    
    route.append(starting_city)  # Return to depot
    return route

def calc_route_cost(route, distance_matrix):
    cost = 0
    for i in range(1, len(route)):
        cost += distance_matrix[route[i-1]][route[i]]
    return cost

# Run CVRP
all_tours = []
all_costs = []

for _ in range(num_vehicles):
    if all(x == 0 for x in demands):
        break
    route = compute_route(depot_index, demands, vehicle_capacity, distance_matrix)
    if len(route) > 2:  # More than just start and end
        cost = calc_route_cost(route, distance_matrix)
        all_tours.append(route)
        all_costs.append(cost)
        # Reduce demands
        for i in route:
            if i != depot_index:
                demands[i] -= min(demans[i], vehic_capacity)

# Show results
total_cost = 0
for i, (tour, cost) in enumerate(zip(all_tours, all_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    total_cost += cost

print(f"Overall Total Travel Cost: {totalcion}")