import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Number of robots (salesmen)
m = 8

# Calculate Euclidean distance between each pair of nodes
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
prob = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat=pulp.LpContinuous)

# Objective: Minimize the maximum distance traveled by any robot
max_distance = pulp.LpVariable("max_distance")
prob += max_distance

# Constraints
# Each city is visited exactly once by exactly one robot
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot leaves from and arrives at the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        prob += (pulp.lpSum(x[i, p, k] for i in range(n) if i != p) - pulp.lpSum(x[p, j, k] for j in range(n) if j != p)) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Distance should not exceed max_distance for any robot
for k in range(m):
    prob += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem
prob.solve()

# Extract the solution
routes = [[(i, j) for i in range(n) for j in range(n) if pulp.value(x[i, j, k]) == 1] for k in range(m)]
tour_costs = [sum(distance_matrix[i][j] for i, j in route) for route in routes]

for k in range(m):
    tour = [0] + [j for i, j in routes[k]]
    print(f"Robot {k} Tour: {tour + [0]}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]}")

print(f"Maximum Travel Cost: {puls.value(max_distance)}")