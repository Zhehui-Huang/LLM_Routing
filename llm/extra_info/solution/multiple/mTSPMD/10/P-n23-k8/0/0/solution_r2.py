import numpy as np
from scipy.spatial.distance import cdist

# City coordinates
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
])

# Distance matrix using Euclidean distance
distance_matrix = cdist(coordinates, coordinates)

def nearest_neighbor_tour(start_city, assigned_cities, dist_matrix):
    current_city = start_city
    path = [current_city]
    total_cost = 0
    available_cities = set(assigned_cities)

    while available_cities:
        next_city = min(available_cities, key=lambda city: dist_matrix[current_city, city])
        total_cost += dist_matrix[current_city, next_city]
        current_city = next_city
        path.append(current_city)
        available_cities.remove(current_city)
    
    # Return to the starting city (depot)
    total_cost += dist_matrix[current_city, start_city]
    path.append(start_city)
    
    return path, total_cost

# Assign cities to robots: very simplistic distribution
robot_assignments = {
    i: [i] for i in range(8)
}
for j in range(8, 23):  # Assign rest of the cities starting with index 8
    robot_assignments[j % 8].append(j)

# Calculate tours and costs
total_travel_cost = 0
for robot_id in range(8):
    assigned_cities = robot_assignments[robot_id]
    tour, cost = nearest_neighbor_tour(robot_id, assigned_cities, distance_matrix)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}\n")
    total_travel_counter += cost

print(f"Overall Total Travel Cost: {personal_total_counter}")