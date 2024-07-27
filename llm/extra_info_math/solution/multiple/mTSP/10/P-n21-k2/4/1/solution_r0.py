import gurobipy as gp
from gurobipy import GRB
import math

# Define euclidean distance calculator
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Input data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}
num_robots = 2
num_cities = len(cities)

# Calculate distances matrix
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities}

# Create model
model = gp.Model()

# Variables
x = model.addVars(num_cities, num_cities, num_robots, vtype=GRB.BINARY, name='x')
u = model.addVars(num_cities, vtype=GRB.CONTINUOUS, name='u')

# Objective
model.setObjective(gp.quicksum(distances[i, j] * x[i, j, k] for i in cities for j in cities if i != j for k in range(num_robots)), GRB.MINIMIZE)

# Constraints
# Each city except the depot is visited exactly once
model.addConstrs(gp.quicksum(x[i, j, k] for i in cities for k in range(num_robots) if i != j) == 1 for j in range(1, num_cities))

# Each robot starts and ends at the depot
model.addConstrs(gp.quicksum(x[0, j, k] for j in cities if j != 0) == 1 for k in range(num_robots))

# Flow conservation for each salesman
model.addConstrs(gp.quicksum(x[i, j, k] for i in cities if i != j) - gp.quicksum(x[j, i, k] for i in cities if i != j) == 0 for j in range(1, num_cities) for k in range(num_robots))

# Subtour elimination
model.addConstrs(u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1 for i in range(1, num_cities) for j in range(1, num_cities) if i != j for k in range(num_robots))

# Solve model
model.optimize()

# Extract tours
tours = [[0] for _ in range(num_robots)]
costs = [0] * num_robots

for k in range(num_robots):
    tour = []
    current = 0
    while True:
        next_city = [j for j in cities if j != current and x[current, j, k].x > 0.5]
        if not next_city:
            break
        next_city = next_city[0]
        tour.append(next_city)
        costs[k] += distances[current, next_city]
        current = next_city
        if current == 0:
            break
    tours[k] += tour + [0]

# Display results
total_cost = sum(costs)
for k in range(num_robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Cost: {total(s)}")