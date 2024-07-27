import math
import numpy as np

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Parameters
vehicle_capacity = 160
num_vehicles = 2
num_cities = len(coordinates)

# Calculate Euclidean distances between cities
distance_matrix = [[0]*num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

def clarke_and_wright():
    vehicle_tours = [[] for _ in range(num_vehicles)]
    vehicle_loads = [0]*num_vehicles
    vehicle_costs = [0]*num_vehicles

    # Compute savings
    savings = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            sij = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings.append((sij, i, j))
    
    savings.sort(reverse=True, key=lambda x: x[0])

    # Initialize tours with trips from depot to each city
    for i in range(1, num_cities):
        found = False
        for v in range(num_vehicles):
            if demands[i] + vehicle_loads[v] <= vehicle_capacity:
                vehicle_tours[v].append([0, i])
                vehicle_loads[v] += demands[i]
                vehicle_costs[v] += 2 * distance_matrix[0][i]
                found = True
                break
        if not found:
            raise Exception("All vehicles are full!")

    # Merge tours based on savings list
    for saving, i, j in savings:
        tour_i = tour_j = -1
        position_i = position_j = -1
        for v in range(num_vehicles):
            for tour in range(len(vehicle_tours[v])):
                if i in vehicle_tours[v][tour]:
                    tour_i, position_i = v, tour
                if j in vehicle_tours[v][tour]:
                    tour_j, position_j = v, tour
        
        if tour_i != tour_j and tour_i != -1 and tour_j != -1 and \
            vehicle_loads[tour_i] + vehicle_loads[tour_j] <= vehicle_capacity:
            # Can merge
            new_tour = vehicle_tours[tour_i][position_i] + vehicle_tours[tour_j][position_j]
            new_cost = vehicle_costs[tour_i] + vehicle_costs[tour_j] - saving

            if new_cost < vehicle_costs[tour_i] + vehicle_costs[tour_j]:
                vehicle_tours[tour_i].append(new_tour)
                vehicle_tours[tour_j].remove(vehicle_tours[tour_j][position_j])
                vehicle_tours[tour_i].remove(vehicle_tours[tour_i][position_i])
                vehicle_costs[tour_i] = new_cost
                vehicle_loads[tour_i] += vehicle_loads[tour_j]
                vehicle_loads[tour_j] = 0

    # Ensure tours are closed at depot
    for v in range(num_vehicles):
        for tour in vehicle_tours[v]:
            if tour[-1] != 0:
                tour.append(0)
                vehicle_costs[v] += distance_matrix[tour[-2]][0]

    return vehicle_tours, vehicle_costs

vehicle_tours, vehicle_costs = clarke_and_wright()
total_cost = sum(vehicle_costs)

for v in range(num_vehicles):
    print(f"Robot {v} Tour: {vehicle_tours[v]}")
    print(f"Robot {v} Total Travel Cost: {vehicle_costs[v]}")

print(f"Overall Total Travel Cost: {total_cost}")