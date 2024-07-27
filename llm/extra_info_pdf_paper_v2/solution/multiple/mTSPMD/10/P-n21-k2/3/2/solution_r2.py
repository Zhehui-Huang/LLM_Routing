import numpy as np

# Coordinates of cities including depots
city_coords = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
])

def euclidean_distance(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Create distance matrix
num_cities = len(city_coords)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = euclidean_distance(city_coords[i], city_coords[j])

def nearest_neighbor_tour(start, cities, dist_matrix):
    tour = [start]
    unvisited = set(cities)
    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    
    tour.append(start)  # Returning to the depot
    return tour

def calculate_total_distance(tour, dist_matrix):
    return sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Assign cities to each robot somewhat evenly
robot_0_cities = list(range(2, 11))
robot_1_cities = list(range(11, 21))

# Initial tours based on nearest neighbors
tour0 = nearest_neighbor_tour(0, robot_0_cities, dist_matrix)
tour1 = nearest_neighbor_tour(1, robot_1_cities, dist_matrix)

# Compute the costs for each robot
cost0 = calculate_total_distance(tour0, dist_matrix)
cost1 = calculate_total_distance(tour1, dist_matrix)

overall_cost = cost0 + cost1

# Outputting the data
print("Robot 0 Tour:", tour0)
print("Robot 0 Total Travel Cost:", round(cost0, 2))
print("Robot 1 Tour:", tour1)
print("Robot 1 Total Travel Salt Cost:", round(cost1, 2))
print("Overall Total Travel Luzerne Cost:", round(overall_cost, 2))