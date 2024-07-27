import pulp
from math import sqrt

# Node coordinates
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
          (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]

# Parameters
n = len(coords)  # Number of nodes including depot
m = 8  # Number of robots

# Calculate Euclidean distances
def distance(i, j):
    return sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

c = {(i, j): distance(i, j) for i in range(n) for j in range(n) if i != j}

# Initialization problem
prob = pulp.LpProblem("Robotic_Routes", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((k, i, j) for k in range(m) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: Minimize the maximum route cost among all robots
maximum_cost = pulp.LpVariable("maximum_cost")
prob += maximum_cost

# Constraints
# Each city visited exactly once by any salesman except the depot
for j in range(1, n):
    prob += pulp.lpSum(x[(k, i, j)] for k in range(m) for i in range(n) if i != j) == 1
        
# Each robot starts and ends at the depot
for k in range(m):
    prob += pulp.lpSum(x[(k, 0, j)] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[(k, j, 0)] for j in range(1, n)) == 1

# Conservation of flow for robots
for k in range(m):
    for j in range(1, n):
        prob += pulp.lpSum(x[(k, i, j)] for i in range(n) if i != j) == pulp.lpSum(x[(k, j, i)] for i in range(n) if i != j)

# Subtour elimination constraints
for k in range(m):
    u = pulp.LpVariable.dicts(f"u_{k}", range(1, n), lowBound=0, upBound=n, cat='Continuous')
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += u[i] - u[j] + n*x[(k, i, j)] <= n-1

# Route cost constraints
for k in range(m):
    prob += pulp.lpSum(c[i, j] * x[(k, i, j)] for i in range(n) for j in range(n) if i != j) <= maximum_cost

# Solve the problem
prob.solve()

# Collect the result
for k in range(m):
    tour = [0]
    next_city = 0
    while True:
        next_cities = [j for j in range(n) if pulp.value(x[(k, next_city, j)]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        if next_city == 0:
            break

    tour_cost = sum(c[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {pulp.value(maximum_cost)}")