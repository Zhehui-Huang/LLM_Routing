import math
import pulp

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distances between all pairs of cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

num_cities = len(cities)
num_robots = 2

# Creating a problem variable to minimize the maximum cost
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# x[i][j][k] binary variable
x = {}
distances = {}
for k in range(num_robots): 
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x[(i, j, k)] = pulp.LpVariable(f"x_{i}_{j}_{k}", 0, 1, pulp.LpBinary)
                distances[(i, j)] = calc_distance(i, j)

max_distance = pulp.LpVariable("max_distance")

# Objective function
prob += max_distance

# Constraint: Ensure each city is visited exactly once by the robots
for j in range(1, num_cities):  # skip the depot
    prob += pulp.lpSum(x[(i, j, k)] for k in range(num_robots) for i in range(num_cities) if i != j) == 1

# Constraints: Flow conservation for each robot
for k in range(num_robots):
    for j in range(num_cities):
        prob += pulp.lpSum(x[(i, j, k)] for i in range(num_cities) if i != j) == pulp.lpSum(x[(j, i, k)] for i in range(num_cities) if i != j)

# Constraints on entering and leaving the depot
for k in range(num_robots):
    prob += pulp.lpSum(x[(0, j, k)] for j in range(1, num_cities)) == 1
    prob += pulp.lpSum(x[(j, 0, k)] for j in range(1, num_cities)) == 1

# Subtour prevention constraints
for k in range(num_robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                prob += pulp.lpSum(x[(i, j, k)] for k in range(num_robots)) * (num_cities - 1) <= num_cities - 2

# Max distance constraints
for k in range(num_robots):
    prob += pulp.lpSum(distances[(i, j)] * x[(i, j, k)] for i in range(num_cities) for j in range(num_cities) if i != j) <= max_distance

# Solve the problem
prob.solve()

# Output the solution
for k in range(num_robots):
    print(f"Robot {k} route:", end=" ")
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and pulp.value(x[(i, j, k)]) > 0.5:
                print(j, end=" -> ")
    print("0")
    cost = sum(distances[(i, j)] * pulp.value(x[(i, j, k)]) for i in range(num_cities) for j in range(num_cities) if i != j)
    print(f"Cost: {cost}")

print(f"Max Distance (objective value): {pulp.value(max_distance)}")