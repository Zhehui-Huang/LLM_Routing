import numpy as np
import random

# Coordinates for each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Calculate distance between two cities
def calculate_distance(idx1, idx2):
    x1, y1 = coordinates[idx1]
    x2, y2 = coordinates[idx2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of robots (equals to the number of depots)
num_robots = 8

# Get the initial and final positions of robots (here, same as depots)
depots = list(range(num_robots))

# Initialize distance matrix
num_cities = len(coordinates)
distance_matrix = np.array([[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)])

# Divide cities among robots as evenly as possible considering depots
cities_per_robot = [list(range(num_robots, num_cities))[(i * (num_cities-num_robots)) // num_robots:((i + 1) * (num_cities-num_robots)) // num_robots] for i in range(num_robots)]

# Helper function to find a TSP route for a single robot
def find_tsp_route(start, cities, distance_matrix):
    from scipy.optimize import linear_sum_assignment
    size = len(cities) + 1
    cost_matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i == j:
                cost_matrix[i][j] = float('inf')
            elif i == 0:
                cost_matrix[i][j] = distance_matrix[start][cities[j-1]]
            elif j == 0:
                cost_matrix[i][j] = distance_matrix[cities[i-1]][start]
            else:
                cost_matrix[i][j] = distance_matrix[cities[i-1]][cities[j-1]]
    
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    route = [start] + [cities[i-1] for i in col_ind if i != 0]
    return route + [start]

# Solve each robot's route independently
tours = {}
total_travel_cost = 0

for i in range(num_robots):
    tour = find_tsp_route(depots[i], cities_per_robot[i], distance_matrix)
    tour_cost = sum(distance_matrix[tour[j]][tour[j + 1]] for j in range(len(tour) - 1))
    tours[i] = (tour, tour_cost)
    total_travel_cost += tour_cost

    # Output each robot's tour and cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

# Output the overall total travel cost
print(f"Overall Total Travel Cost: {total_travel_cost}")