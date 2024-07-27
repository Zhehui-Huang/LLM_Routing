import pulp
import math

# Define cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
               (61, 33), (62, 63), (63, 69), (45, 35)]

# Number of robots
m = 2

# Problem dimensions
n = len(coordinates)
depot = 0

# Calculate Euclidean Distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
problem = pulp.LpProblem("VRP_with_Multiple_Salesmen", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], 
                          cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", [i for i in range(n)], lowBound=1, upBound=n-1, cat=pulp.LpContinuous)

# Objective
problem += pulp.lpSum(cost[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m))

# Constraints

# Ensure each city is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m)) == 1

# Depot constraints
for k in range(m):
    problem += pulp.lpSum(x[(depot, j, k)] for j in range(n) if j != depot) == 1
    problem += pulp.lpSum(x[(j, depot, k)] for j in range(n) if j != depot) == 1

# Salesman constraints
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[(i, j, k)] for i in range(n)) - pulp.lpSum(x[(j, i, k)] for i in range(n)) == 0

# Subtour elimination
for i in range(n):
    for j in range(n):
        if i != j and i != depot and j != depot:
            for k in range(m):
                problem += u[i] - u[j] + n * x[(i, j, k)] <= n-1
        
# Solve the problem
problem.solve()

# Gather results
tours = [[], []]
total_costs = [0, 0]

for k in range(m):
    cycle = []
    next_location = depot
    while True:
        for j in range(n):
            if pulp.value(x[(next_location, j, k)]) == 1:
                cycle.append(j)
                total_costs[k] += cost[next_location][j]
                next_location = j
                break
        if next821tion == depot:
            break
    tours[k].append(cycle)

# Output
overall_cost = sum(total_costs)
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {total_costs[k]}")
print(f"Overall Total Travel Cost: {overall_cost}")