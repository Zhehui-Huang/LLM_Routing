from math import sqrt
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, PULP_CBC_CMD, LpStatus

# Distances
def euclidean(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Constants
NUM_CITIES = 16
NUM_ROBOTS = 8
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

distances = [[euclidean(coordinates[i], coordinates[j]) for j in range(NUM_CITIES)] for i in range(NUM_CITIES)]

# Setup the problem
problem = LpProblem("MVRP", LpMinimize)
x = [[[LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for k in range(NUM_ROBOTS)] for j in range(NUM_CITIES)] for i in range(NUM_CITIES)]
u = [LpVariable(f"u_{i}", lowBound=1, upBound=NUM_CITIES-1, cat='Continuous') for i in range(NUM_CITIES)]

# Objective Function
problem += lpSum(distances[i][j] * x[i][j][k] for k in range(NUM_ROBOTS) for i in range(NUM_CITIES) for j in range(NUM_CITIES))

# Constraints
for j in range(1, NUM_CITIES):
    problem += lpSum(x[i][j][k] for i in range(NUM_CITIES) for k in range(NUM_ROBOTS) if i != j) == 1

for k in range(NUM_ROBOTS):
    problem += lpSum(x[0][j][k] for j in range(1, NUM_CITIES)) == 1
    problem += lpSum(x[j][0][k] for j in range(1, NUM_CITIES)) == 1

for k in range(NUM_ROBOTS):
    for j in range(1, NUM_CITIES):
        problem += lpSum(x[i][j][k] for i in range(NUM_CITIES) if i != j) - lpSum(x[j][i][k] for i in range(NUM_CITIES) if i != j) == 0

for i in range(1, NUM_CITIES):
    for j in range(1, NUM_CITIES):
        if i != j:
            problem += (u[i] - u[j] + (NUM_CITIES-1) * lpSum(x[i][j][k] for k in range(NUM_ROBOTS)) <= NUM_CITIES - 2)

# Solve the problem
solver = PULP_CBC_CMD(msg=True)
problem.solve(solver)

# Check the solution
if LpStatus[problem.status] == "Optimal":
    total_cost = 0
    for k in range(NUM_ROBOTS):
        current_city = 0
        path = [0]  # Robot starts at the depot
        tour_cost = 0
        for _ in range(1, NUM_CITIES):
            for j in range(NUM_CITIES):
                if x[current_city][j][k].varValue > 0.5:
                    path.append(j)
                    tour_cost += distances[current_city][j]
                    current_city = j
                    break
        path.append(0)  # Return to depot
        tour_cost += distances[current_city][0]
        total_cost += tour_cost
        print(f"Robot {k} Tour: {path}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No Optimal Solution Found.")