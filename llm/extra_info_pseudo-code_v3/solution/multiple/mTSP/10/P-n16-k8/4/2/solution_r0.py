import numpy as np
import math
from itertools import permutations

# City coordinates with the depot as the first city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

def calculate_distance(c1, c2):
    return math.dist(c1, c2)

# Calculate the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Number of robots
num_robots = 8

# Function to calculate the cost of a tour
def tour_cost(tour, distance_matrix):
    cost = 0
    for k in range(len(tour) - 1):
        cost += distance_matrix[tour[k]][tour[k+1]]
    return cost

# Initial solution: Split the cities roughly equally among robots
def initial_solution(num_robots, num_cities):
    cities_per_robot = (num_cities - 1) // num_robots
    tours = []
    for i in range(num_robots):
        if i == num_robots - 1:  # last robot takes remaining cities
            tour = list(range(i * cities_per_robot + 1, num_cities))
        else:
            tour = list(range(i * cities_per_robot + 1, (i + 1) * cities_per_robot + 1))
        tour = [0] + tour + [0]  # add depot at the start and end
        tours.append(tour)
    return tours

# Initial tours assignment
tours = initial_solution(num_robots, num_cities)

# Attempt to optimize each tour using a simple improvement heuristic
def optimize_tour(tour, distance_matrix):
    best_tour = tour
    best_cost = tour_cost(tour, distance_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if i != 1 or j != len(tour) - 2:  # don't reverse the path between depot cities
                    new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                    new_cost = tour_cost(new_tour, distance_matrix)
                    if new_cost < best_cost:
                        best_tour = new_tour
                        best_cost = new_cost
                        improved = True
    return best_tour

# Optimize each robot's tour
optimized_tours = [optimize_tour(tour, distance_matrix) for tour in tours]
total_travel_cost = 0

# Print results
for idx, tour in enumerate(optimized_tours):
    cost = tour_cost(tour, distance_matrix)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
    total_travel_cost += cost

print(f"Overall Total Travel Cost: {total_travel_cost}")