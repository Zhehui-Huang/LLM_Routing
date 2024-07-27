import numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Calculate distances using Euclidean formula
def distance(i, j):
    return np.linalg.norm(np.array(coordinates[i]) - np.array(coordinates[j]))

# Model
model = ConcreteModel()

# Indices for the cities
N = len(coordinates)
model.nodes = range(N)

# Variables
model.y = Var(model.nodes, model.nodes, within=Binary)  # Path decision variable
model.u = Var(model.nodes, within=NonNegativeReals, bounds=(0, N-1))  # Sequence decision variable

# Objective: Minimize total traveled distance
model.obj = Objective(
    expr=sum(distance(i, j) * model.y[i, j] for i in model.nodes for j in model.nodes if i != j),
    sense=minimize
)

# Constraints
# Enter each city exactly once
model.enter = ConstraintList()
for j in model.nodes:
    model.enter.add(expr=sum(model.y[i, j] for i in model.nodes if i != j) == 1)

# Leave each city exactly once
model.leave = ConstraintList()
for i in model.nodes:
    model.leave.add(expr=sum(model.y[i, j] for j in model.nodes if i != j) == 1)

# No sub-tours allowed
model.no_subtour = ConstraintList()
for i in model.nodes:
    for j in model.nodes:
        if i != j:
            model.no_subtour.add(model.u[i] - model.u[j] + N * model.y[i, j] <= N-1)

# Solve the model
solver = SolverFactory('glpk')
solver.solve(model)

# Extracting results
tour = []
current = 0
visited = [False] * N
while not visited[current]:
    visited[current] = True
    tour.append(current)
    # Find next node
    current = next(j for j in model.nodes if model.y[current, j]() == 1 and not visited[j])

# Tour cost computation
total_travel_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Display the results
print("Optimal tour:", tour)
print("Total travel cost:", total_travel.cost)

# If broken into two robots
# This is illustrative and might need adjustments based on actual results and robot revisiting rules
halve = len(tour) // 2
robot1_tour = [0] + tour[1:halve + 1]
robot2_tour = [1] + tour[halve + 1:]

robot1_cost = sum(distance(robot1_tour[i], robot1_tour[i + 1]) for i in range(len(robot1_tour) - 1))
robot2_cost = sum(distance(robot2_tour[i], robot2_tour[i + 1]) for i in range(len(robot2_tour) - 1))
overall_cost = robot1_cost + robot2_cost

print("\nRobot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", robot1_cost)

print("Robot 2 Tour:", robot2_tour)
print("Robot 2 Total Travel Cost:", robot2_cost)

print("Overall Total Travel Cost:", overall_cost)