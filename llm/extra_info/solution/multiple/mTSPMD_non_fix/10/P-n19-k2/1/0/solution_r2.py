import numpy as np
from scipy.spatial.distance import cdist

# Coordinates of cities
coordinates = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
])

# Distance matrix creation
distance_matrix = cdist(coordinates, coordinates)

def nearest_neighbor_tour(start, unvisited):
    tour = [start]
    current_city = start
    total_cost = 0

    while unvisited:
        next_city = unvisited[np.argmin(distance_matrix[current_city][unvisited])]
        total_cost += distance_matrix[current_city][next_city]
        current_city = next_city
        tour.append(next_city)
        unvisited.remove(next_city)

    return tour, total_cost

# Cities list without depots
cities = list(range(2, len(coordinates)))

# City lists for each robot starting from different depots
cities_0 = cities.copy()
cities_1 = cities.copy()

# Tours for each robot
robot_0_tour, robot_0_cost = nearest_neighbor_tour(0, cities_0)
robot_1_tour, robot_1_cost = nearest_neighbor_tour(1, cities_1)

# Eliminate visit to the same city by both robots by reassigning non-depot cities
shared_cities = set(robot_0_tour).intersection(set(robot_1_tour))
for city in shared_cities:
    if city in robot_0_tour:
        robot_0_tour.remove(city)
        robot_0_cost -= distance_matrix[robot_0_tour[robot_0_tour.index(city) - 1]][city]
    else:
        robot_1_tour.remove(city)
        robot_1_cost -= distance_matrix[robot_1_tour[robot_1_tour.index(city) - 1]][city]

print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}\n")
print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}\n")
print(f"Overall Total Travel Cost: {robot_0_cost + robot_1_cost}")