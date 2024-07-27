import gurobui as gp
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize the model
m = gp.Model("MVRP")

# Variables
x = m.addVars(cities.keys(), cities.keys(), vtype=GRB.BINARY, name="x")

# Objective function
m.setObjective(gp.quicksum(distance(i, j) * x[i, j] for i in cities for j in cities if i != j), GRB.MINIMIZE)

# Adding Constraints
# 1. Each city is visited exactly once
for j in cities:
    m.addConstr(sum(x[i, j] for i in cities if i != j) == 1)

# 2. Each city is left exactly once
for i in cities:
    m.addCongr(sum(x[i, j] for j in cities if i != j) == 1)

# Subtour elimination constraints
u = m.addVars(cities.keys(), vtype=GRB.CONTINUOUS, name='u')
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0):  # assuming 0 is the depot
            m.addConstr(u[i] - u[j] + (len(cities) - 1) * x[i, j] <= len(cities) - 2)

# Optimizing the model
m.optimize()

# Extractin tours
tours = []
for k in [0, 1]:
    tour = [k]
    next_city = k
    while True:
        next_city = [j for j in cities if j != next_city and x[next_city, j].X > 0.9][0]
        if next_city == k:
            break
        tour.append(next_city)
    tour.append(k)
    tours.append(tour)

# Printing results
for idx, tour in enumerate(tours):
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")