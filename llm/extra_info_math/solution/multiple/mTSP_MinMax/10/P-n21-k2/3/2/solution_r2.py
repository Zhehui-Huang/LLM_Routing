import pulp
import math

# Define the cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

n = len(coordinates)  # Number of nodes including depot
m = 2  # Number of salesmen

# Initialization of the problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Constraints
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):
    for p in range(1, n):
        problem += pulp.lpSum(x[p, j, k] for j in range(n) if p != j) == pulp.lpSum(x[i, p, k] for i in range(n) if i != p)

for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

for i in range(1, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Add constraint for maximum travel cost
for k in range(m):
    problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem
status = problem.solve()

# Print status
print("Status:", pulp.LpStatus[status])

# Extract the tours
tours = [[] for _ in range(m)]
costs = [0] * m

for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j, k]) == 1:
                tours[k].append((i, j))
                costs[k] += distance(i, j)

# Format the outputs
formatted_tours = [[0] for _ in range(m)]
for k in range(m):
    cur_city = 0
    while True:
        next_cities = [j for j in range(n) if x[cur_city, j, k].varValue == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        formatted_tours[k].append(next_city)
        cur_city = next_city
    formatted_tours[k].append(0)

for i, tour in enumerate(formatted_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

max_cost = max(costs)
print("Maximum Travel Cost:", max_cost)