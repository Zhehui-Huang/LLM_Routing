import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Number of robots (salesman)
m = 8

# Calculate Euclidean distance between pairs of nodes
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem setup
prob = pulp.LpProblem("MVRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(1, n) if i != j for k in range(m)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat=pulp.LpContinuous)

# Objective: Minimize the maximum distance traveled by any robot
max_distance = pulp.LpVariable("max_distance")
prob += max_distance

# Constraints

# Each city except depot is visited exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow constraints
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1
    for j in range(1, n):
        prob += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += (u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2) for k in range(m)

# Limit distance to maximum distance variable
for k in range(m):
    prob += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(1, n) if i != j) <= max_distance

# Solve the problem
prob.solve()

# Output the tours and costs
for k in range(m):
    tour = [0]
    next_city = 0
    while True:
        next_city = sum(x[next_city, j, k].value() * j for j in range(n) if j != next_city)
        if next_city == 0:
            break
        tour.append(next_city)
    tour.append(0)
    tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {pulp.value(max_distance)}")