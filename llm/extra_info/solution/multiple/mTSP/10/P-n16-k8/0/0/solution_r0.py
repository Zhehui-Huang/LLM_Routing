import numpy as np
from scipy.spatial import distance_matrix
from itertools import permutations

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}
number_of_robots = 8

# Calculate distance matrix
points = np.array(list(cities.values()))
dist_mat = distance_matrix(points, points)

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Generate initial tour guesses
best_tours = None
best_total_cost = float('inf')

# Iterating over all permutations of splitting the cities into 8 tours can be combinatorially large and impractical.
# Here we create a very naive initial solution by equally dividing the cities among the robots, as a heuristic.

city_indices = list(cities.keys())[1:]  # excluding depot city
np.random.shuffle(city_indices)  # shuffle cities to randomly assign to robots
split_tours = [city_indices[i::number_of_robots] for i in range(number_of_robots)]

# Compute initial tours with the depot city added
robot_tours = [[0] + split_tours[i] + [0] for i in range(number_of_robots)]

# Calculate the cost of these initial tours
tour_costs = [calculate_tour_cost(tour, dist_mat) for tour in robot_tours]
total_cost = sum(tour_costs)

# Output generation
for i, (tour, cost) in enumerate(zip(robot_tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total TravelStack Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")