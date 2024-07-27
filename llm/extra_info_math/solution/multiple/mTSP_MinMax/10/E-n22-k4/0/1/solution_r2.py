from pulp import *
import math

# Constants
num_robots = 4
num_cities = 22
depot_city = 0

# Define the coordinates for each city (including the depot at index 0)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Decision variables
model = LpProblem("Robot_Routing_Problem", LpMinimize)
x = LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots)), cat="Binary")
u = LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat='Continuous')

# Objective Function
model += lpMax([lpSum([x[(i, j, k)] * distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j]) for k in range(num_robots)])

# Constraints
for k in range(num_robots):
    model += lpSum([x[(depot_city, j, k)] for j in range(num_cities) if j != depot_city]) == 1  # Departure from depot
    model += lpSum([x[(j, depot_city, k)] for j in range(1, num_cities)]) == 1  # Return to depot

for j in range(1, num_cities):
    model += lpSum([x[(i, j, k)] for i in range(num_cities) if i != j for k in range(num_robots)]) == 1  # Each city visited exactly once

# Flow conservation
for k in range(num_robots):
    for j in range(1, num_cities):
        model += lpSum([x[(i, j, k)] for i in range(num_cities) if i != j]) == \
                 lpSum([x[(j, i, k)] for i in range(num_cities) if i != j])

# Subtour Elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                model += u[i] - u[j] + num_cities * x[(i, j, k)] <= num_cities-1

# Solve the model
status = model.solve(PULP_CBC_CMD(msg=1))

# Output results
if status == LpStatusOptimal:
    max_cost = max([value(lpSum([x[(i, j, k)] * distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j]))
                    for k in range(num_robots)])
    for k in range(num_robots):
        tour = []
        for i in range(num_cities):
            for j in range(num_cities):
                if x[(i, j, k)].varValue > 0.99:
                    tour.append((i, j))
        print(f"Robot {k} Tour: {tour}")

    print("Maximum Travel Cost:", max_cost)
else:
    print("The problem is not optimally solvable.")