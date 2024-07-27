import pulp
import math

# Define the cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Define the number of robots (salesmen)
num_robots = 4

# Define the problem
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Number of cities including the depot
num_cities = len(coordinates)

# Decision variable x_ijk where i, j are cities and k is the robot
x = pulp.LpVariable.dicts("x", [(i, j, k) for k in range(num_robots)
                                for i in range(num_cities) for j in range(num_cities)], cat='Binary')

# Position in the tour (to eliminate subtours)
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Cost matrix
cost = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            cost[i, j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            cost[i, j] = float('inf')  # No loops

# Objective Function
problem += pulp.lpSum(cost[i, j] * x[i, j, k] for k in range(num_robots) for i in range(num_cities) for j in range(num_cities))

# Constraints:

# Each city is visited exactly once by exactly one salesman
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for k in range(num_robots) for i in range(num_cities)) == 1

# Every salesman leaves and enters each city at most once
for k in range(num_robots):
    for j in range(num_cities):
        problem += pulp.lpSum(x[j, i, k] for i in range(num_cities)) == pulp.lpSum(x[i, j, k] for i in range(num_cities))

# Each salesman leaves the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1

# Each salesman returns to the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            problem += (u[i] - u[j] + (num_cities - 1) * pulp.lpSum(x[i, j, k] for k in range(num_robots))) <= num_cities - 2

# Solve the problem
status = problem.solve()

# Print the results
if pulp.LpStatus[status] == 'Optimal':
    print("Solution Found:")
    for k in range(num_robots):
        tour = [0]
        next_city = 0
        total_cost = 0
        while True:
            found_next = False
            for j in range(num_cities):
                if x[next_city, j, k].varValue == 1:
                    tour.append(j)
                    total_cost += cost[next_city, j]
                    next_city = j
                    found_next = True
                    break
            if not found_next or next_city == 0:
                break
        print(f"Robot {k} Tour: {tour + [0]}")
        print(f"Robot {k} Total Travel Cost: {total_cost}")
    overall_cost = sum(cost[i, j] * x[i, j, k].varValue for k in range(num_robots) for i in range(num_cities) for j in range(num_cities))
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("No optimal solution found.")