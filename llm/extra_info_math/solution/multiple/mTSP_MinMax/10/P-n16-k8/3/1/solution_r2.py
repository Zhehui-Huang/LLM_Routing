import pulp
import math
from itertools import product

# Data input
coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]
num_cities = len(coords)
num_robots = 8

# Calculating the Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = [[euclidean_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create the optimization problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i, j, k in product(range(num_cities), repeat=3) if i != j],
                          cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, upBound=num_cities-1, cat=pulp.LpContinuous)
Z = pulp.LpVariable("Z", lowBound=0, cat=pulp.LpContinuous)

# Objective - Minimizing the maximum travel distance
problem += Z

# Constraints
# 1. Each city is visited exactly once by one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# 2. Flow conservation for robots
for k in range(num_robots):
    problem += sum(x[0, j, k] for j in range(1, num_cities)) == 1  # Departing from depot
    problem += sum(x[i, 0, k] for i in range(1, num_cities)) == 1  # Returning to depot

    for j in range(1, num_cities):
        problem += sum(x[i, j, k] for i in range(num_cities) if i != j) == sum(x[j, i, k] for i in range(num_cities) if i != j)

# 3. Subtour elimination
for i in range(1, num_cities):
    for j in range(2, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# 4. Distance constraints for max cost
for i, j, k in product(range(num_cities), repeat=3):
    if i != j:
        problem += distances[i][j] * x[i, j, k] <= Z

# Solve the problem
problem.solve()

# Output results
tours = {k: [] for k in range(num_robots)}
for k in range(num_robots):
    for j in range(num_cities):
        for i in range(num_cities):
            if pulp.value(x[i][j][k]) == 1:
                tours[k].append(j)

# Display each robot's path
for k in tours:
    print(f"Robot {k} Tour: [0, " + ", ".join(map(str, tours[k])) + ", 0]")

max_cost = max(sum(distances[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1)) for k in tours)
print(f"Maximum travel cost among all tours: {max_cost}")