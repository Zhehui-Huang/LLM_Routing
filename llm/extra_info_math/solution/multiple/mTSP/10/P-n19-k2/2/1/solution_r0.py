import pulp
from math import sqrt

# Define coordinates and number of cities
coords = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), 
          (62, 63), (63, 69), (45, 35)]
num_cities = len(coords)
num_robots = 2

# Function to calculate Euclidean Distance
def distance(city1, city2):
    return sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# Create the problem variable
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), 
                          cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat=pulp.LpContinuous)

# Objective
problem += pulp.lpSum(distance(i, j) * x[i][j][k] for i in range(num_cities) 
                      for j in range(num_cities) if i != j for k in range(num_robots)), "Total_Cost"

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i][j][k] for i in range(num_cities) 
                          for k in range(num_robots) if i != j) == 1

# Each salesman leaves and enters each city exactly once
for k in range(num_robots):
    for i in range(1, num_cities):
        problem += pulp.lpSum(x[i][j][k] for j in range(num_cities) if i != j) \
                   == pulp.lpSum(x[j][i][k] for j in range(num_cities) if i != j)

# Each salesman leaves the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0][j][k] for j in range(1, num_cities)) == 1
    
# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i][j][k] <= num_cities - 1

# Solve the problem
status = problem.solve()

# Output the routes and costs
total_cost = 0
for k in range(num_robots):
    tour = [0]
    while True:
        for j in range(num_cities):
            if pulp.value(x[tour[-1]][j][k]) == 1:
                tour.append(j)
                break
        if tour[-1] == 0:
            break
    tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_page}")

print(f"Overall Total Travel Cost: {total_cost}")