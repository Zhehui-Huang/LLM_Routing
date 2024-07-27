from concorde.tsp import TSPSolver
from math import sqrt
import numpy as np

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    x1, y1 = cities[c1]
    x2, y2 = cities[c2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create a symmetric matrix of distances
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(i, j)

# Instantiate and solve the TSP
solver = TSPSolver.from_data(distance_matrix, norm="EUC_2D")
solution = solver.solve()

# Helper function to split the tour into two approx equal parts
def split_tour(tour):
    midpoint = len(tour) // 2
    return tour[:midpoint], tour[midpoint:]

# Extract and split the tour
complete_tour = solution.tour
robot_tour1, robot_tour2 = split_tour(complete_tour)

# Function to calculate the travel cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i + 1])
    return cost

# Append the depot to the tours for each robot and calculate total costs
robot_tour1.append(0)
robot_tour1.insert(0, 0)
robot_tour2.append(0)
robot_tour2.insert(0, 0)

robot_1_cost = calculate_tour_cost(robot_tour1)
robot_2_cost = calculate_tour_cost(robot_tour2)

# Print the results
print("Robot 0 Tour:", robot_tour1)
print("Robot 0 Total Travel Cost:", robot_1_cost)
print("\nRobot 1 Tour:", robot_tour2)
print("Robot 1 Total Travel Cost:", robot_2_cost)

overall_total_cost = robot_1_cost + robot_2_cost
print("\nOverall Total Travel Cost:", overall_total_cost)