import math
import random
from itertools import permutations

# City information (indices, coordinates)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Demand per city, indexed similarly to coordinates
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19,
    11, 12, 26, 17, 6, 15, 5, 10
]

# Vehicle information
num_vehicles = 8
vehicle_capacity = 40

# Using a basic approach: Nearest Neighbor + Capacity Check
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Generate distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

def nearest_neighbor(current_city, unvisited, demands, remaining_capacity):
    eligible_cities = [(i, distance_matrix[current_city][i]) for i in unvisited if demands[i] <= remaining_capacity]
    return min(eligible_cities, key=lambda x: x[1], default=None)

def create_tour():
    tours = []
    total_costs = []
    all_visited = set(range(1, len(coordinates)))  # Exclude depot initially for visiting
    while all_visited:
        tour = [0]
        load = vehicle_capacity
        current_city = 0
        total_cost = 0
        
        while load > 0 and all_visited:
            next_city_info = nearest_neighbor(current_city, all_visited, demands, load)
            if next_city_info is not None:
                next_city, travel_cost = next_city_info
                tour.append(next_city)
                total_cost += travel_cost
                current_city = next_city
                load -= demands[next_city]
                all_visited.remove(next_city)
            else:
                break
        
        # Return to depot
        tour.append(0)
        total_cost += distance_matrix[current_city][0]
        tours.append(tour)
        total_costs.append(total_cost)
        
        if len(tours) >= num_vehicles:
            break
    
    return tours, total_costs

# Applying the nearest neighbor heuristic to generate tours
tours, total_costs = create_tour()
overall_total_cost = sum(total_costs)

# Output results as required
for i, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")