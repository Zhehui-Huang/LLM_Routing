import gurobipy as gp
from gurobipy import GRB
import math

# Define Euclidean distance function
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

# Distance matrix
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities}

# Initialize model
model = gp.Model()

# Decision variables
x = model.addVars(num_cities, num_cities, num_robots, vtype=GRB.BINARY, name='x')
u = model.addVars(num_cities, vtype=GRB.CONTINUOUS, name='u')

# Objective
model.setObjective(gp.quicksum(distances[i, j] * x[i, j, k] for i in cities for j in cities if i != j for k in range(num_robots)), GRB.MINIMIZE)

# Constraints
model.addConstrs(gp.quicksum(x[i, j, k] for i in cities for k in range(num_robots) if i != j) == 1 for j in range(1, num_cities))
model.addConstrs(gp.quicksum(x[0, j, k] for j in cities if j != 0) == 1 for k in range(num_robots))
model.addConstrs(gp.quicksum(x[i, j, k] for i in cities if i != j) - gp.quicksum(x[j, i, k] for i in cities if i != j) == 0 for j in range(1, num_cities) for k in range(num_robots))
model.addConstrs(u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1 for i in range(1, num_cities) for j in range(1, num_cities) if i != j for k in range(num_robots))

# Solve model
model.optimize()

# Check the solution
if model.status == GRB.OPTIMAL:
    tours = [[0] for _ in range(num_robots)]
    total_cost = 0

    for k in range(num_robots):
        current_city = 0
        while True:
            next_city = [j for j in range(num_cities) if j != current_city and x[current_city, j, k].X > 0.5]
            if not next_city:  # Should not happen as the tour must loop back
                break
            next_city = next_city[0]
            tours[k].append(next_city)
            total_cost += distances[current_city, next_city]
            current_city = next_city
            if current_city == 0:
                break
    
    # Repeating last step to complete the tour and display each robot's tour and cost
    for k in range(num_robots):
        tours[k].append(0)
        cost = sum(distances[tours[k][i], tours[k][i + 1]] for i in range(len(tours[k]) - 1))
        print(f"Robot {k} Tour: {tours[k]}")
        print(f"Robot {k} Total Travel Cost: {cost}")
    
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("Optimal solution was not found.")