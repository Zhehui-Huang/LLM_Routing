import pulp
import math

# Given data
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

# Number of robots
m = 2

# Euclidean distance calculation
def dist(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Problem instance
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(len(cities)) for j in range(len(cities)) for k in range(m) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", [i for i in range(len(cities))], lowBound=1, upBound=len(cities) - 1, cat=pulp.LpInteger)

# Objective Function
prob += pulp.lpSum(dist(i, j) * x[i, j, k] for k in range(m) for i in range(len(cities)) for j in range(len(cities)) if i != j)

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, len(cities)):
    prob += sum(x[i, j, k] for i in range(len(cities)) for k in range(m) if i != j) == 1

# Flow conservation constraints
for k in range(m):
    for i in range(len(cities)):
        prob += sum(x[i, j, k] for j in range(len(cities)) if i != j) == sum(x[j, i, k] for j in range(len(cities)) if i != j)

# Each robot starts and ends at the depot
for k in range(m):
    prob += sum(x[0, j, k] for j in range(1, len(cities))) == 1
    prob += sum(x[j, 0, k] for j in range(1, len(cities))) == 1

# Subtour elimination
for i in range(1, len(cities)):
    for j in range(1, len(cities)):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (len(cities) - 1) * x[i, j, k] <= len(cities) - 2

# Solve the problem
status = prob.solve()
print("Status:", pulp.LpStatus[status])

# Output Results
for k in range(m):
    tour = [0]
    for i in range(len(cities)):
        j = next(j for j in range(len(cities)) if pulp.value(x[i, j, k]) == 1)
        if j == 0:
            break
        tour.append(j)
    tour.append(0) # Return to depot
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))}")

max_cost = max(sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1)) for tour in tours)
print(f"Maximum Travel Cost: {max_cost}")