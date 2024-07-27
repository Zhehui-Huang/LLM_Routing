import numpy as np
from scipy.spatial import distance_matrix

# Coordinates of the cities
coordinates = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Calculating the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

def nearest_neighbour_tour(start_city, cities_left):
    tour = [start_city]
    current_city = start_dest
    total_cost = 0
    
    while cities_left:
        next_city = min(cities_left, key=lambda x: dist_matrix[current_city, x])
        total_cost += dist_matrix[current_city, next_city]
        tour.append(next_city)
        cities_left.remove(next_city)
        current_city = next_city
    
    return tour, total_cost

# Assign each robot a starting depot
cities = set(range(2, len(coordinates)))  # all cities except depot cities
robot_0_dest = 0  # robot 0 starts from city 0
robot_1_dest = 1  # robot 1 starts from city 1

# Generate tours for each robot
robot_0_tour, robot_0_cost = nearest_neighbour_tour(robot_0_dest, cities.copy())
robot_1_tour, robot_1_cost = nearest_neighbour_tour(robot_1_dest, cities.difference(set(robot_0_tour)))

# Output results
print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}\n")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}\n")
print(f"Overall Total Travel Cost: {robot_0_cost + robot_1_cost}")