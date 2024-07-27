import pulp
import math

# Coordinates of cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

n = len(coordinates)
m = 8  # Number of robots

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the problem
prob = pulp.LpProblem("VRP_Multi_Depot_Robots", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for k in range(m) for i in range(n) for j in range(n)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
prob += pulp.lpSum(c[i][j] * x[i, j, k] for k in range(m) for i in range(n) for j in range(n))

# Each non-depot city is visited exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

# Depot constraints for each robot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Continuity constraints to eliminate subtours
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += u[i] - u[j] + (n * x[i, j, k]) <= n - 1

# Solve the problem
prob.solve()

# Printing the results
tours = {k: [] for k in range(m)}
costs = {k: 0 for k in range(m)}

for k in range(m):
    sequence = [0]
    next_city = 0
    while True:
        next_cities = [j for j in range(n) if pulp.value(x[next_city, j, k]) == 1 and j not in sequence]
        if not next_cities:
            break
        next_city = next_cities[0]
        sequence.append(next_city)
    tours[k] = sequence + [0]
    costs[k] = sum(c[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1))

# Output tours and costs
total_cost = sum(costs.values())
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Cost: {total"],