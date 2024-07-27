import math
import random

# Cities coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Function to compute Euclidean distance
def euclidean_dist(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialize distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_dist(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Number of robots
num_robots = 8

# Initial greedy assignment of cities to robots (simple round robin)
assignments = [[] for _ in range(num_robots)]
for i in range(1, num_cities):  # start from 1 to avoid including the depot
    assignments[i % num_robots].append(i)

# Function to calculate the cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]
    cost += distance_matrix[tour[-1]][tour[0]]  # Back to depot
    return cost

# Function to optimize tours using GVNS
def optimize_tours(assignments):
    # This function only provides a placeholder for a deeper GVNS implementation
    return assignments

# Optimize initial assignments
optimized_assignments = optimize_tours(assignments)

# Calculate costs and format the output
tours = []
max_cost = 0

for index, cities in enumerate(optimized_assignments):
    tour = [0] + cities + [0]
    cost = calculate_tour_cost(tour)
    tours.append((tour, cost))
    max_cost = max(max_cost, cost)
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Maximum Travel Travel Cost: {max_cost}")