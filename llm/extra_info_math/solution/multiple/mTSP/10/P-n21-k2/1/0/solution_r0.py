import pulp
import math

# Inputs
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
    20: (45, 35)
}

n = len(cities)  # Including depot
m = 2  # Number of robots/salesmen

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Compute cost matrix
c = {(i, j): distance(i, j) for i in range(n) for j in range(n)}

# Set up the LP model
model = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for i in range(n) for j in range(n) for k in range(m)}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=2, cat='Continuous') for i in range(2, n)}  # Note: depot does not need a u variable

# Objective function
model += pulp.lpSum(c[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m)), "Total Travel Cost"

# Constraints
# Each non-depot city must be visited exactly once
for j in range(1, n):
    model += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1, f"visit_once_{j}"

# Each salesman leaves depot exactly once and returns once
for k in range(m):
    model += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1, f"leave_depot_{k}"
    model += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1, f"enter_depot_{k}"

# Flow conservation for each salesman at each city
for k in range(m):
    for j in range(1, n):
        model += (pulp.lpSum(x[i, j, k] for i in range(n)) - 
                  pulp.lpSum(x[j, i, k] for i in range(n))) == 0, f"flow_conservation_{j}_{k}"

# Subtour elimination constraints
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            model += u[i] - u[j] + n * pulp.lpSum(x[i, j, k] for k in range(m)) <= n - 1, f"subtour_{i}_{j}"

# Solve the model
model.solve()

# Extract tours and calculate costs
tours = {k: [] for k in range(m)}
for k in range(m):
    cur = 0
    while True:
        # Find next city for each salesman starting from depot
        next_city = [j for j in range(n) if pulp.value(x[cur, j, k]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        tours[k].append(next_city)
        cur = next_city
        if cur == 0:
            break

overall_cost = pulp.value(model.objective)