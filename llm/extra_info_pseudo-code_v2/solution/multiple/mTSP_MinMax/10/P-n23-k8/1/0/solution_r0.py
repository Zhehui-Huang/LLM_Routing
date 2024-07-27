import numpy as np
import itertools
from math import sqrt

# Setting up the environment
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
num_robots = 8
depot = 0

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance between two points """
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initial naive partitioning of cities to robots ignoring optimization for now
city_indices = list(range(1, n))  # city indices except the depot
robot_cities = [city_indices[i::num_robots] for i in range(num_robots)]

# Functions to compute tour cost and output formatting
def compute_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def output_tour_and_cost(robot_tours):
    max_cost = 0
    for idx, tour in enumerate(robot_tours):
        tour_cost = compute_tour_cost(tour)
        max_cost = max(max_cost, tour_cost)
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")
    print(f"Maximum Travel Cost: {max_cost:.2f}")

# Construct tours for each robot starting and ending at the depot
robot_tours = [[depot] + rt + [depot] for rt in robot_cities]

# Output the results
output_tour_and_cost(robot_tours)