from pulp import *
import math

# Coordinates for the different cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of salesmen
m = 2
# Number of nodes including the depot
n = len(coordinates)

# Create the problem variable to contain the problem data
problem = LpProblem("Robot_Routing_Problem", LpMinimize)

# X[i][j][k] = 1 if robot k travels from i to j
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], cat='Binary')

# Subtour prevention auxiliary variables
u = LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# Maximize the maximum distance traveled amongst all robots
max_cost = LpVariable("max_cost", lowBound=0)
problem += max_cost

# Objective Function
problem += max_cost

# Distance Calculation Function
def dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Constraints
# Ensure each city is visited exactly once
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Each robot should leave each city at most once
for k in range(m):
    for i in range(n):
        problem += lpSum(x[i, j, k] for j in range(n) if i != j) == lpSum(x[j, i, k] for j in range(n) if i != j)

# Starting and ending at the depot
for k in range(m):
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Eliminate subtours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n*x[i, j, k] <= n-1

# Minimize the maximum tour length 
for k in range(m):
    problem += lpSum(dist(i, j) * x[i, j, k] for i in range(n) for j in range(n)) <= max_cost

# Solve the problem
problem.solve()

# Check if the problem is solved correctly
if LpStatus[problem.status] == 'Optimal':
    # Extract results
    tours = {}
    costs = {}
    for k in range(m):
        tour = [0]
        current_location = 0
        while True:
            next_locations = [j for j in range(n) if j != current_location and value(x[current_location, j, k]) == 1]
            if not next_locations:
                break
            next_location = next_locations[0]
            tour.append(next_location)
            current_location = next_location
            if current_location == 0:
                tours[k] = tour
                break
        costs[k] = sum(dist(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    # Output tours and costs
    for k in tours:
        print(f"Robot {k} Tour: {tours[k]}")
        print(f"Robot {k} Total Travel Cost: {costs[k]}")
    
    print(f"Maximum Travel Cost: {value(max_cost)}")
else:
    print(f"The problem could not be solved to optimality. Status: {LpStatus[problem.status]}")