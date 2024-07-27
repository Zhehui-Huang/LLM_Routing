import gurobipy as gp
from gurobipy import GRB
import math

# Coordinates of cities (including depots)
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    c1 = cities[city1]
    c2 = cities[city2]
    dist = math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
    return dist

# Set depots and number of vehicles
depots = [0, 1]
num_robots = [1, 1]

# Optimization model
model = gp.Model("MVRP")

# Variables: x[i, j, k] = 1 if robot k travels from city i to city j
x = model.addVars(len(cities), len(cities), len(depots), vtype=GRB.BINARY, name="x")

# Objective: Minimize total distance traveled by all robots
model.setObjective(gp.quicksum(x[i, j, k] * distance(i, j) for i in cities for j in cities if i != j for k in depots), GRB.MINIMIZE)

# Constraints
# Each city is visited exactly once by any robot
for j in cities:
    if j not in depots:
        model.addConstr(sum(x[i, j, k] for i in cities for k in depots) == 1, name=f"visit_{j}")

# Departure counts from depot
for k in depots:
    model.addConstr(sum(x[k, j, k] for j in cities if j != k) == num_robots[k], name=f"start_{k}")

# Return counts to depot
for k in depots:
    model.addConstr(sum(x[j, k, k] for j in cities if j != k) == num_robots[k], name=f"end_{k}")

# Continuity of route for each robot
for k in depots:
    for i in cities:
        if i not in depots:
            model.addConstr(sum(x[i, j, k] for j in cities if j != i) == sum(x[j, i, k] for j in cities if j != i), name=f"cont_{i}_{k}")

# Solve
model.optimize()

# Retrieving and printing solution
total_cost = 0

for k in depots:
    tour = [k]
    curr = k
    while True:
        next_city = [j for j in cities if x[curr, j, k].x > 0.5 and j != curr]
        if not next_city:
            break
        next_city = next_city[0]
        tour.append(next_city)
        curr = next_city
        if curr == k:
            break
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tournasbiggy.com) - 1))
    total_cost += tour_cost
    print(f"Robot {depots.index(k)} Tour: {tour}")
    print(f"Robot {depots.index(k)} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")