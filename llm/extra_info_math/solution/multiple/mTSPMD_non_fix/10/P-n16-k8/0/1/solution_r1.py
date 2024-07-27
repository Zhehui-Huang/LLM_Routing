import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpInteger, PULP_CBC_CMD

# Cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]
num_cities = len(coordinates)
depot = 0
num_robots = 8

# Compute Euclidean distances
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Define the problem
model = LpProblem("Minimize_Total_Distance", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities)), cat='Binary')

# Objective function
model += lpSum(distance_matrix[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities))

# Constraints
# Ensure each city is visited exactly once
for j in range(num_cities):
    model += lpSum(x[i, j] for i in range(num_cities) if i != j) == 1

for i in range(num_cities):
    model += lpSum(x[i, j] for j in range(num_cities) if i != j) == 1

# Ensure robots start at the depot
model += lpSum(x[depot, j] for j in range(1, num_cities)) == num_robots

# Subtour elimination
u = LpVariable.dicts("u", range(num_cities), lowBound=0, upBound=num_cities-1, cat=LpInteger)
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            model += u[i] - u[j] + (num_cities) * x[i, j] <= num_cities - 1

# Solve the model
model.solve(PULP_CBC_CMD(msg=0))

# Retrieve results
tours = [[] for _ in range(num_robots)]
current_position = [depot] * num_robots
for _ in range(num_cities - 1):
    for k in range(num_robots):
        next_city = [j for j in range(num_cities) if j != current_position[k] and x[current_position[k], j].value() == 1]
        if next_city:
            next_city = next_city[0]
            tours[k].append(next_city)
            current_position[k] = next_city

# Calculate tour costs and print tours
total_cost = 0
for k in range(num_robots):
    tour_cost = sum(distance_matrix[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: [0, " + ", ".join(map(str, tours[k])) + "]")
    print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel (All Robots): {total_cost:.2f}")