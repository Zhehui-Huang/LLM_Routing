import gurobipy as gp
from gurobipy import GRB
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Cities with coordinates (index 0 is the depot city)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

num_robots = 2
num_cities = len(cities)

# Distance matrix
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(num_cities) for j in range(num_cities)}

model = gp.Model()

# Variables
x = model.addVars(num_cities, num_cities, num_robots, vtype=GRB.BINARY, name='x')
u = model.addVars(num_cities, vtype=GRB.CONTINUOUS, lb=0.0, name='u')

# Objective
model.setObjective(gp.quicksum(x[i, j, k] * distances[i, j] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)), GRB.MINIMIZE)

# Each city is visited exactly once by one robot
model.addConstrs(gp.quicksum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1 for j in range(1, num_cities))

# Each robot starts and ends at the depot
model.addConstrs(gp.quicksum(x[0, j, k] for j in range(1, num_cities)) == 1 for k in range(num_robots))
model.addConstrs(gp.quicksum(x[j, 0, k] for j in range(1, num_cities)) == 1 for k in range(num_robots))

# Flow conservation
model.addConstrs(gp.quicksum(x[i, j, k] for j in range(num_cities) if j != i) == gp.quicksum(x[j, i, k] for j in range(num_cities) if j != i) for i in range(1, num_cities) for k in range(num_robots))

# Eliminate subtours
model.addConstrs(u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1 for i in range(1, num_cities) for j in range(1, num_cities) if i != j for k in range(num_robots))

# Solve the model
model.optimize()

if model.status == GRB.OPTIMAL:
    print(f"Optimal solution found with objective value {model.ObjVal:.2f}")
    for k in range(num_robots):
        tour = [0]
        next_city = 0
        while True:
            next_city = [j for j in range(num_cities) if x[tour[-1], j, k].x > 0.5][0]
            tour.append(next_city)
            if next_city == 0:
                break
        print(f"Robot {k} Tour: {tour}")
        tour_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
        print(f"Robot {k} Total Travel Cost: {tour_distance:.2f}")
else:
    print("No optimal solution found.")