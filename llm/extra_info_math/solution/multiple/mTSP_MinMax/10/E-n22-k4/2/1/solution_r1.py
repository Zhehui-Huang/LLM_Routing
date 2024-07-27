import pulp
import math

def calculate_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Define coordinates of each city including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

num_cities = len(coordinates)
num_robots = 4

# Distance matrix
distance = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Creating the model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Objective function
model += pulp.lpSum(distance[i][j] * x[i, j, k] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots) if i != j)

# Constraints

# Each city is visited exactly once by exactly one robot
for j in range(1, num_cities):
    model += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# Robots leave each city only once
for k in range(num_robots):
    for i in range(num_cities):
        model += pulp.lpSum(x[i, j, k] for j in range(num_cities) if i != j) == pulp.lpSum(x[j, i, k] for j in range(num_cities) if i != j)

# Robots must start and finish at the depot
for k in range(num_robots):
    model += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    model += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Subtour elimination constraint
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                model += u[i] - u[j] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# Solve the problem
model.solve()

# Collect the results
tours = {k: [] for k in range(num_robots)}
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i, j, k]) == 1:
                tours[k].append((i, j))

# Output the tours in each robot
max_travel_cost = 0
for k in tours:
    route = [0]
    current_city = 0
    while True:
        for (i, j) in tours[k]:
            if i == current_city:
                route.append(j)
                current_city = j
                break
        if current_city == 0:
            break
    travel_cost = sum(distance[route[i]][route[i + 1]] for i in range(len(route) - 1))
    print(f"Robot {k} Tour: {route}")
    print(f"Robot {k} Total Travel Cost: {travel_cost}")
    if travel_cost > max_travel_cost:
        max_travel_cost = travel_cost

print(f"Maximum Travel Cost: {max_travel_cost}")