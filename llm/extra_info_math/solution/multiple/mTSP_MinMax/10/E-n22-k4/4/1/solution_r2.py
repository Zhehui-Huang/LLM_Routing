from gurobipy import Model, GRB, quicksum
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
    21: (139, 182),
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
u = model.addVars(n, vtype=GRB.CONTINUOUS, lowBound=0, name="u")  # Subtour avoidance

# Objective
max_distance = model.addVar(vtype=GRB.CONTINUOUS, name="maxDistance")
model.setObjective(max_distance, GRB.MINIMIZE)

# Constraints
# 1. Assignment constraint: Each city (excluding depot 0) must be visited exactly once by exactly one robot
for j in range(1, n):  # start from 1 to exclude depot
    model.addConstr(quicksum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1)

# 2. Flow conservation at each city for each robot
for k in range(m):
    for j in range(1, n):  # again, exclude depot
        model.addConstr(quicksum(x[i, j, k] for i in range(n) if i != j) == quicksum(x[j, i, k] for i in range(n) if i != j))

# 3. Depot constraints
for k in range(m):
    model.addConstr(quicksum(x[0, j, k] for j in range(1, n)) == 1)
    model.addConstr(quicksum(x[j, 0, k] for j in range(1, n)) == 1)

# 4. Subtour elimination: Miller-Tucker-Zemlin (MTZ) constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model.addConstr(u[i] - u[j] + n * quicksum(x[i, j, k] for k in range(m)) <= n - 1)

# 5. Connect max travel distance to the traveled distances
for k in range(m):
    model.addConstr(quicksum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n)) <= max_distance)

# Optimize the model
model.Params.TimeLimit = 60  # Limit execution time (optional)
model.optimize()

# Print the result
if model.status == GRB.OPTIMAL:
    print("Optimal solution found. Maximum Travel Cost:", max_distance.X)
    distances = []
    for k in range(m):
        tour = []
        current_city = 0
        while True:
            next_city = None
            for j in range(n):
                if x[current_city, j, k].X > 0.5:
                    tour.append(j)
                    next_city = j
                    break
            if next_city == 0:
                break
            current_city = next_city
        cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        distances.append(cost)
        print(f"Robot {k} Tour: {tour} with Cost: {cost}")
    print("Maximum of individual travel costs:", max(distances))
else:
    print("No optimal solution was found.")