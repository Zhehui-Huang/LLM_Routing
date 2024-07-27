import pulp
import math

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Constants for the problem
m = 2  # Number of robots
n = len(coordinates)  # Including the depot

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = pulp.LpProblem("VRP_Multiple_Salesmen", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)),
                          cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat=pulp.LpContinuous)

# Objective function
problem += pulp.lpSum(cost[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city must be visited exactly once by any salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1

# Flow constraints
for k in range(m):
    for j in range(n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n)) == pulp.lpSum(x[j, i, k] for i in range(n))

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Each robot leaves and eventually returns to the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Solve the problem
problem.solve()

# Output results
for k in range(m):
    tour = [0]
    costs = 0
    next_location = 0
    while True:
        found = False
        for j in range(n):
            if pulp.value(x[next_location, j, k]) == 1:
                if j == 0:
                    found = True
                    break
                tour.append(j)
                costs += cost[next_location][j]
                next_location = j
                break
        if found:
            break
    tour.append(0)  # return to the depot
    costs += cost[next_location][0]  # cost of returning to the depot
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {costs}")

# Calculate the total cost
total_travel_cost = sum(cost[cycle[i]][cycle[i + 1]] for cycle in tour for i in range(len(cycle) - 1))
print(f"Overall Total Travel Cost: {total_travel_details}")