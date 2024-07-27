import numpy as np
from scipy.spatial.distance import euclidean
from pulp import LpProblem, LpMinimize, lpSum, LpVariable, LpBinary, value

# Define the coordinates for each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_cities = len(coordinates)

# Create the distance matrix
distances = [[euclidean(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Parameters
num_robots = 8
start_depot = 0

# Initialize the problem
problem = LpProblem("TSP", LpMinimize)

# Variables
x = [[LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in range(num_cities)] for i in range(num_cities)]

# Objective
problem += lpSum(distances[i][j] * x[i][j] for i in range(num_cities) for j in range(num_cities))

# Constraints
# Each city is visited exactly once
for j in range(1, num_cities):
    problem += lpSum(x[i][j] for i in range(num_cities) if i != j) == 1

# Each city is left exactly once
for i in range(1, num_cities):
    problem += lpSum(x[i][j] for j in range(num_cities) if i != j) == 1

# Amount of robots leaving the start depot
problem += lpSum(x[start_depot][j] for j in range(1, num_cities)) == num_robots

# Solve the problem
problem.solve()

# Extract the solution
tours = {i: [] for i in range(num_robots)}
current_positions = [start_depot] * num_robots
used = [False] * num_cities
used[start_depot] = True

for _ in range(1, num_cities):
    for robot_id in range(num_robots):
        current_city = current_positions[robot_id]
        for next_city in range(num_cities):
            if value(x[current_city][next_city]) == 1 and not used[next_city]:
                tours[robot_id].append(next_city)
                current_positions[robot_id] = next_city
                used[next_city] = True
                break

# Output the tours and costs
total_cost = 0
for robot_id, tour in tours.items():
    tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: [{start_depot}] + {tour}")
    print(f"Robot {robotid} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")