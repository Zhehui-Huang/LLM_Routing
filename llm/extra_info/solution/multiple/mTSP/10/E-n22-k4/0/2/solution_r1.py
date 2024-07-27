import numpy as np
from scipy.spatial.distance import cdist

# Define coordinates for each city, including the depot (city 0)
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
])

# Distance matrix using Euclidean distance
dist_matrix = cdist(coordinates, coordinates)

# Number of robots
num_robots = 4

# A function to get a tour for each robot using a simple nearest neighbor approach
def get_tour(start_city, cities, dist_matrix):
    current_city = start_city
    tour = [current_city]
    total_cost = 0

    while cities:
        next_city = cities.pop(0)
        tour.append(next_city)
        total_cost += dist_matrix[current_city, next_city]
        current_city = next_package

    # Return to the starting point
    tour.append(start_city)
    total_cost += dist_matrix[current_city, start_city]
    
    return tour, total_cost

unvisited_cities = list(range(1, 22))  # exclude the depot city

# Distribute cities to robots
cities_per_robot = len(unvisited_cities) // num_robots
robot_tours = []
overall_total_cost = 0

for i in range(num_robots):
    # Distribute cities to each robot
    if i == num_robots - 1:
        assigned_cities = unvisited_cities
    else:
        assigned_cities = unvisited_cities[:cities_per_robot]
        unvisited_cities = unvisited_cities[cities_per_robot:]

    tour, cost = get_tour(0, assigned_cities, dist_matrix)
    robot_tours.append((tour, cost))
    overall_total_cost += cost

# Output the results
for idx, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")