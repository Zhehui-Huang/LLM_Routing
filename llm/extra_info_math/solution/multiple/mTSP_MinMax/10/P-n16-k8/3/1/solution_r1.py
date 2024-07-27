import pulp
import math
from itertools import product

# Define the data
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 48), (58, 27), (37, 69)]
num_cities = len(coords)
num_robots = 8

# Distance calculation
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = [[euclidean_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create the problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i, j, k in product(range(num_cities), repeat=3) if i != j],
                          cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, upBound=num_cities-1, cat=pulp.LpContinuous)
Z = pulp.LpVariable("Z", lowBound=0, cat=pulp.LpContinuous)

# Objective
problem += Z, "Minimize the maximum distance traveled by any robot"

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# Each robot leaves the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1

# Each robot returns to the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, num_cities)) == 1

# Flow conservation
for k in range(num_robots):
    for j in range(1, num_cities):
        problem += (pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) -
                    pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j)) == 0

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Maximize the single longest distance constraint
for i in range(num_cities):
    for j in range(1, num_cities):
        for k in range(num_robots):
            if i != j:
                problem += distances[i][j] * x[i, j, k] <= Z

# Solve the problem
problem.solve()

# Print out the results
total_costs = [0] * num_robots
tours = {k: [0] for k in range(num_robots)}

for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i, j, k]) == 1:
                tours[k].append(j)
                total_costs[k] += distances[i][j]
                break
    tours[k].append(0)  # Complete the tour by returning to the depot
    total_costs[k] += distances[tours[k][-2]][0]  # Add the return to the depot

max_cost = max(total_costs)

for k in range(num_robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {total_costs[k]}")

print(f"Maximum Travel EstCost: {max_cost}")