import gurobipy as gp
from gurobipy import GRB
import math

# Define the cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
}

# Function to calculate Euclidean distance between two points
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Number of depots and robots per depot
depots = {0: 1, 1: 1}  # Depot 0 has 1 robot, Depot 1 has 1 robot
total_cities = len(cities)

# Create a new model
model = gp.Model("TSP_MVRP")

# Create variables: x[i, j, k], where i, j are cities and k is the depot number
x = model.addVars(total_cities, total_cities, len(depots), vtype=GRB.BINARY, name="x")

# Objective: Minimize the total travel distance
obj = gp.quicksum(x[i, j, k] * distance(cities[i], cities[j]) 
                  for i in cities for j in cities if i != j for k in depots for _ in range(depots[k]))
model.setObjective(obj, GRB.MINIMIZE)

# Each city must be visited exactly once excluding depots
for j in cities:
    if j not in depots:
        model.addConstr(sum(x[i, j, k] for i in cities for k in depots if i != j) == 1)

# Each robot starts and ends at its starting depot
for k in depots:
    model.addConstr(sum(x[k, j, k] for j in cities if j != k) == sum(x[j, k, k] for j in cities if j != k) == depots[k])

# Continuity constraints to eliminate subtours
for k in depots:
    for i in cities:
        if i != k:
            model.addConstr(sum(x[i, j, k] for j in cities if j != k) == sum(x[j, i, k] for j in cities if j != i))

# Solve the model
model.optimize()

# Retrieve the tours for each robot
tours = []
total_cost = 0
for k in depots:
    for robot in range(depots[k]):
        tour = [k]
        curr = k
        while True:
            next_city = next(j for j in cities if x[curr, j, k].X > 0.5 and j != curr)
            if next_city == k:
                break
            tour.append(next_city)
            curr = next_city
        tour.append(k)  # Return to the depot
        tours.append((tour, model.ObjVal))

# Output the solution
for idx, (tour, cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {model.ObjVal}")