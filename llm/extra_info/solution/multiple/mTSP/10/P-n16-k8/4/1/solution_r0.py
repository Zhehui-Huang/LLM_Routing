from math import sqrt
import itertools
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus

# Given coordinates of the cities including the depot (city 0)
city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
                    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
                    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
                    (37, 69)]
num_cities = len(city_coordinates)
num_robots = 8

# Helper function to compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create distance matrix
distance_matrix = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[(i, j)] = calculate_distance(i, j)

# Setting up the MIP Model with PuLP
model = LpProblem(name="multiple-tsp-robot-routing", sense=LpMinimize)
x = LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots) if i != j], cat='Binary')
u = LpVariable.dicts("u", [(i, k) for i in range(1, num_cities) for k in range(num_robots)], lowBound=0, upBound=num_cities-1, cat='Continuous')  # Position in tour if city is visited

# Objective Function
model += lpSum(distance_matrix[(i, j)] * x[(i, j, k)] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots) if i != j), "Total_Tour_Cost"

# Constraints
for k in range(num_robots):
    # Start from the depot
    model += lpSum(x[(0, j, k)] for j in range(1, num_cities) if (0, j) in x) == 1
    # Return to the depot
    model += lpSum(x[(i, 0, k)] for i in range(1, num_cities) if (i, 0) in x) == 1

for j in range(1, num_cities):
    # Each city is visited exactly once by any robot
    model += lpSum(x[(i, j, k)] for i in range(num_cities) for k in range(num_robots) if i != j) == 1
    # Each city is departed exactly once by any robot
    model += lpSum(x[(j, i, k)] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

for k in range(num_robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                model += u[(j, k)] - u[(i, k)] + (num_cities - 1) * x[(i, j, k)] <= num_cities - 2

# Solving the model
model.solve()

# Output tours and total costs
overall_cost = 0
tours = {k: [] for k in range(num_robots)}
costs = {k: 0 for k in range(num_robots)}

for k in range(num_robots):
    current_location = 0
    tours[k].append(0)
    while True:
        next_city = None
        for j in range(num_cities):
            if j != current_location and x[(current_location, j, k)].varValue == 1:
                next_city = j
                break
        if next_city is None:
            tours[k].append(0)
            break  
        tours[k].append(next_city)
        costs[k] += distance_matrix[(current_location, next_city)]
        current_location = next_city
    costs[k] += distance_matrix[(tours[k][-2], 0)]  # Return to depot
    tours[k].append(0)

for k in range(num_robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
    overall_cost += costs[k]

print(f"Overall Total Travel Cost: {overall_cost}")