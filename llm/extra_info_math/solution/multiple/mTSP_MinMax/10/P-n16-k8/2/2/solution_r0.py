import pulp
import math

# City positions
positions = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distances
def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

# Constants
n = len(positions)     # Number of nodes (including the depot)
m = 8                  # Number of robots

# Create the Euclidean distance matrix
cost = {(i, j): distance(positions[i], positions[j]) for i in range(n) for j in range(n) if i != j}

# Setting up the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("route", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("position", range(1, n), lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum([cost[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j])

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum([x[i, j, k] for i in range(n) for k in range(m) if i != j]) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        problem += (pulp.lpSum([x[i, p, k] for i in range(n) if i != p]) ==
                    pulp.lpSum([x[p, j, k] for j in range(n) if j != p]))

# Each salesman leaves the depot
for k in range(m):
    problem += pulp.lpSum([x[0, j, k] for j in range(1, n)]) == 1
    problem += pulp.lpSum([x[j, 0, k] for j in range(1, n)]) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
status = problem.solve()
print(f"Status: {pulp.LpStatus[status]}")

# Extract results
tours = {k: [] for k in range(m)}
for k in range(m):
    from_city = 0
    while True:
        to_city = [j for j in range(n) if pulp.value(x[from_city, j, k]) == 1]
        if not to_city:
            break
        to_city = to_city[0]
        tours[k].append(to_city)
        from_city = to_city
        if to_city == 0:
            break

for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")