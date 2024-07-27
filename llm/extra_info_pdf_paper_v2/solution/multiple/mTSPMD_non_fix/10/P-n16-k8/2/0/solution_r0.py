import math
import random

# Constants
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]
num_robots = 8
start_depot = 0

# Helper Functions
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_total_cost(tours):
    total_cost = 0
    for robot_id, tour in enumerate(tours):
        cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
        total_cost += cost
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {round(cost, 2)}")
    return total_cost

# Distance matrix for faster computations
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(16)] for i in range(16)]