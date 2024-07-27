import math
import numpy as np

# City coordinates with the depot first
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_path(coordinates[i], coordinates[j])

# Heuristic to initialize robot tours: Sequentially assigning cities to robots
num_robots = 2
robot_tours = [[] for _ in range(num_robots)]
for city_index in range(1, num_cities):
    closest_robot_tour = min([(sum(distance_matrix[tour[-1]][city_index]
                                  for tour in robot_tours if tour else 0), i)
                              for i, tour in enumerate(robot_tours)])[1]
    robot_tours[closest_robot_tour].append(city_index)

# Adding the depot to the start and end of tours
for tour in robot_tours:
    tour.insert(0, 0)
    tour.append(0)

# Calculate tour costs
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

total_travel_cost = 0

for i, tour in enumerate(robot_tours):
    cost = calculate_tour_cost(tour)
    total_travel_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")