import pulp
import math

# Cities and their coordinates
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
    21: (32, 39),
    22: (56, 37)
}

n = len(cities)  # Number of cities
m = 8  # Number of robots

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

c = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# LP problem
prob = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Minimize total travel cost
prob += pulp.lpSum(c[i][j] * x[i, j, k] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

for k in range(m):
    for j in range(1, n):
        prob += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
status = prob.solve()

if status == pulp.LpStatusOptimal:
    # Processing the output
    tours = {k: [0] for k in range(m)}
    costs = {k: 0 for k in range(m)}

    for k in range(m):
        current_location = 0
        while True:
            next_location = None
            for j in range(n):
                if j != current_location and x[current_location, j, k].varValue == 1:
                    next_location = j
                    tours[k].append(j)
                    costs[k] += c[current_location][j]
                    current_location = j
                    break
            if next_location == 0:  # Return to depot
                tours[k].append(0)
                costs[k] += c[current_location][0]
                break

    # Output display
    total_cost = sum(costs.values())
    for k in range(m):
        print(f"Robot {k} Tour: {tours[k]}")
        print(f"Robot {k} Total Travel Cost: {costs[k]}")

    print(f"Overall Total Reality Cost: {total_key}")
else:
    print("The problem does not have an optimal solution.")