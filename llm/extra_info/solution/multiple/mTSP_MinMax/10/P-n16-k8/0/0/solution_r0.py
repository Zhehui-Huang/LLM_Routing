import math
import numpy as np

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
num_robots = 8
depot = 0

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_distance(tour):
    """ Calculate the total travel distance for a given tour """
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = calculate_distance(i, j)

# Generate initial tours for each robot, starting and ending at the depot
tours = [[] for _ in range(num_robots)]
cities_to_visit = list(range(1, num_cities))  # exclude the depot city

# Distribute cities evenly to robots
for index, city in enumerate(cities_to_visit):
    tours[index % num_robots].append(city)

# Adding start and end at depot
for tour in tours:
    tour.insert(0, depot)  # start at the depot
    tour.append(depot)  # end at the depot

# Calculate costs and determine the max cost
tour_costs = []
for tour in tours:
    cost = calculate_total_distance(tour)
    tour_costs.append(cost)

max_tour_cost = max(tour_costs)

# Display the optimal solution
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_tour_cost}")