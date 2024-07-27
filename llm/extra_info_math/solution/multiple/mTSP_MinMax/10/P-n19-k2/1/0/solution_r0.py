import pulp
import math

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define the problem instance
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

n = len(cities)  # Number of nodes including the depot
m = 2            # Number of salesmen

# Costs matrix
C = {}
for i in range(n):
    for j in range(n):
        if i != j:
            C[(i, j)] = euclidean_distance(cities[i], cities[j])
        else:
            C[(i, j)] = 0

# Create the problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat=pulp.LpContinuous)

# Objective: Minimize the maximum distance traveled by any salesman
maximum_distance = pulp.LpVariable("maximum_distance", lowBound=0, cat=pulp.LpContinuous)
prob += maximum_distance

# Constraints
# 1. Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

# 2. Flow conservation constraints
for k in range(m):
    for j in range(n):
        prob += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# 3. Each salesman leaves depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# 4. Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# 5. Max distance constraint for each salesman
for k in range(m):
    prob += pulp.lpSum(C[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= maximum_distance

# Solve the problem
prob.solve()

# Output results
max_travel_cost = pulp.value(maximum_distance)
print(f"Maximum Travel Cost: {max_travel_cost}")

tours = []
for k in range(m):
    tour = [0]
    next_city = 0
    total_cost = 0
    while True:
        next_city = next(j for j in range(n) if pulp.value(x[next_city, j, k]) == 1)
        total_cost += C[tour[-1], next_city]
        tour.append(next_city)
        if next_city == 0:
            break
    tours.append(tour)
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {total_cost}")