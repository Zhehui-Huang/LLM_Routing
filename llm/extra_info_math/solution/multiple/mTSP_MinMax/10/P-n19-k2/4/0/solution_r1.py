import math
import numpy as np
from pulp import *

# Define the cities' coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of cities, including the depot
num_cities = len(coordinates)

# Number of robots
num_robots = 2

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Create the distance matrix
dist_matrix = {(i, j): distance(i, j) for i in range(num_cities) for j in range(num_cities)}

# Create the problem variable to contain the problem data
problem = LpProblem("TSP_with_Multiple_Robots", LpMinimize)

# Create problem variables
x = LpVariable.dicts("x", [(i, j , k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)], cat='Binary')
u = LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat='Continuous')

# The objective function is added to 'problem' first
problem += lpSum(dist_matrix[(i, j)] * x[i, j, k] for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots)), "Total_Distance"

# Constraints
for j in range(1, num_cities):
    problem += lpSum(x[i, j, k] for i in range(num_cities) if i != j for k in range(num_robots)) == 1, f"One_Depart_from_{j}"

for i in range(1, num_cities):
    problem += lpSum(x[i, j, k] for j in range(num_cities) if i != j for k in range(num_robots)) == 1, f"One_Arrival_to_{i}"

for k in range(num_robots):
    for i in range(num_cities):
        problem += lpSum(x[i, j, k] for j in range(num_cities) if i != j) - lpSum(x[j, i, k] for j in range(num_cities) if i != j) == 0, f"Flow_Conservation_{i}_{k}"

for k in range(num_robots):
    problem += lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Subtour Elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# Solve the problem
problem.solve()

# Create a function to extract the solution and format it
def extract_solution():
    routes = [[] for _ in range(num_robots)]
    costs = [0 for _ in range(num_robots)]
    
    for k in range(num_robots):
        tour = []
        for i in range(num_cities):
            for j in range(num_cities):
                if x[i, j, k].value() == 1:
                    tour.append((i, j))
        # Start forming the final route
        if tour:
            start = 0
            nextCity = dict(tour)[start]
            route = [0]
            cost = 0
            while nextCity != 0:
                route.append(nextCity)
                cost += dist_matrix[(route[-2], nextCity)]
                nextCity = dict(tour)[nextCity]
            route.append(0)
            cost += dist_matrix[(route[-2], 0)]
            routes[k] = route
            costs[k] = cost
    
    max_cost = max(costs)
    
    # Print the solution
    for k in range(num_robots):
        print(f"Robot {k} Tour: {routes[k]}")
        print(f"Robot {k} Total Travel Cost: {costs[k]}")
    
    print(f"Maximum Travel Cost: {max_cost}")

# Extract and display the solution
extract_solution()