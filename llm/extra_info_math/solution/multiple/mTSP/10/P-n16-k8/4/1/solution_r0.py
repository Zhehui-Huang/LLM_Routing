import pulp
import math

# Define the coordinates of the cities (including the depot)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distance between cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

n = len(coordinates)  # Number of nodes including depot
m = 8  # Number of salesmen

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], cat='Binary')
u = pulp.LpVariable.dicts("u", [i for i in range(n)], lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) for i != j), "Total Travel Cost"

# Constraints
# Every city is visited exactly once by one salesman
for j in range(1, n):
    problem += sum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        problem += sum(x[i][p][k] for i in range(n) if i != p) == sum(x[p][j][k] for j in range(n) if j != p)

# Salesmen leave the depot
for k in range(m):
    problem += sum(x[0][j][k] for j in range(1, n)) == 1

# Salesmen return to the depot
for k in range(m):
    problem += sum(x[i][0][k] for i in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(2, n):
        if i != j:
            problem += u[i] - u[j] + n * sum(x[i][j][k] for k in range(m)) <= n - 1

# Solve the problem
problem.solve()

# Output the results
overall_cost = 0
for k in range(m):
    print(f"Robot {k} Tour:", end=" ")
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                print(f"{i} -> {j}", end=" ")
    print()
    tour_cost = sum(distance(i, j) * pulp.value(x[i][j][k]) for i in range(n) for j in range(n) if i != j)
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")