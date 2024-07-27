import math
import numpy as np

# Define locations of each city including depot
locations = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
             (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
             (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Demands of each city, excluding the depot
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Number of robots and their capacity
num_robots = 2
capacity = 160

def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

def find_nearest(current_city, remaining_cities, demands, current_load):
    min_distance = float('inf')
    nearest_city = None
    for city in remaining_cities:
        if demands[city] + current_load <= capacity:
            distance = euclidean_distance(locations[current_city], locations[city])
            if distance < min_distance:
                min_distance = distance
                nearest_city = city
    return nearest_city, min_distance

def solve_cvrp():
    remaining_cities = set(range(1, len(locations)))  # exclude the depot city
    tours = []
    total_costs = []

    for _ in range(num_robots):
        current_city = 0
        tour = [0]
        total_cost = 0
        current_load = 0
        
        while remaining_cities and current_load < capacity:
            next_city, travel_cost = find_nearest(current_city, remaining_cities, demands, current_load)
            if next_city is None:
                break
            
            tour.append(next_city)
            total_cost += travel_cost
            current_load += demands[next_city]
            remaining_cities.remove(next_city)
            current_city = next_city
        
        # Return to the depot
        total_cost += euclidean_distance(locations[current_city], locations[0])
        tour.append(0)
        tours.append(tour)
        total_costs.append(total_cost)
    
    return tours, total_costs, sum(total_costs)

tours, total_costs, overall_cost = solve_cvrp()

# Display the results
for i, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")