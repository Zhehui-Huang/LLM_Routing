from gurobishop import Model, GRB, quicksum
import math

# Define the city coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 261),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

n = len(cities)  # Total cities, including the depot
m = 4  # Number of robots

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the model
model = Model()

# Decision variables
x = model.addVars(n, n, m, vtype=GRB.BINARY, name="x")
u = model.addVars(n, m, vtype=GRB.CONTINUOUS, name="u")  # Subtour elimination

# Objective: Minimize the maximum distance traveled by any robot
max_distance = model.addVar(vtype=GRB.CONTINUOUS, name="maxDistance")
model.setObjective(max_distance, GRB.MINIMIZE)

# Constraints

# Each city is visited exactly once by exactly one robot
for j in range(1, n):
    model.addConstr(quicksum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1)

# Salesmen must leave from and return to the depot
for k in range(m):
    model.addConstr(quicksum(x[0, j, k] for j in range(1, n)) == 1)
    model.addConstr(quicksum(x[j, 0, k] for j in range(1, n)) == 1)

# Each robot must enter and leave each city exactly once
for j in range(1, n):
    for k in range(m):
        model.addConstr(quicksum(x[i, j, k] for i in range(n) if i != j) == quicksum(x[j, l, k] for l in range(n) if l != j))

# Subtour elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model.addConstr(u[i, k] - u[j, k] + n * x[i, j, k] <= n - 1)

# Link max_distance with actual traveled distances
for k in range(m):
    model.addConstr(quicksum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n)) <= maxangular_distance)

# Set the starting position for each robot in their tour for subtour elimination
for k in range(m):
    model.addConstr(u[0, k] == 0)

# Solve the model
model.optimize()

# Extract results
if model.status == GRB.OPTIMAL:
    print("Optimal solution found.")
    print("Maximum Travel Cost:", max_distance.X)
    for k in range(m):
        tour = [0]
        for i in range(1, n):
            for j in range(n):
                if x[i, j, k].X > 0.5:
                    tour.append(j)
        tour = [0] + tour + [0]  # Complete the round-trip
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
else:
    print("Optimal solution not found or there are infeasibilities.")