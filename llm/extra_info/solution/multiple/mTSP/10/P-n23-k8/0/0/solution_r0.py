import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment

# Cities' coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Number of robots
number_of_robots = 8

# Calculate the distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Function to solve the Traveling Salesman Problem approximately
def solve_tsp(dists):
    row_ind, col_ind = linear_sum_assignment(dists)
    tour = [0] + [i for i in col_ind[1:] if i != 0] + [0]  # start and end at depot (city 0)
    cost = dists[0, col_ind[0]] + sum(dists[row_ind[i], col_ind[i]] for i in range(1, len(col_ind)))
    cost += dists[col_ind[-1], 0]  # return to depot cost
    return tour, cost

# Divide cities evenly (naive clustering by index). This can be improved by geographical clustering.
cities_per_robot = len(coordinates[1:]) // number_of_robots
assignments = []

# Assign cities to robot
start = 1
for i in range(number_of_robots - 1):
    assignments.append(list(range(start, start + cities_per_robot)))
    start += cities_per_robot
assignments.append(list(range(start, len(coordinates))))  # last robot takes the remaining cities

# Collect tour data
tours = []
overall_total_cost = 0
for robot_id, assigned_cities in enumerate(assignments):
    submatrix_indices = [0] + assigned_cities
    submatrix = dist_matrix[np.ix_(submatrix_indices, submatrix_indices)]
    tour, tour_cost = solve_tsp(submatrix)
    tours.append([submatrix_indices[i] for i in tour])
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tours[-1]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")