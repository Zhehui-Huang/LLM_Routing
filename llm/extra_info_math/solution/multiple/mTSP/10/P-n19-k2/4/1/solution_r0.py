import pulp
import math

# Coordinates of cities including depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of cities and salesmen
n = len(coordinates)
m = 2

# Calculate Euclidean distance between cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Create the problem
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum(cost[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints

# Each city is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1

# Salesmen constraints
for k in range(m):
    # Leave the depot
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    # Return to the depot
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1
    # Flow conservation
    for j in range(1, n):
        problem += (pulp.lpSum(x[i, j, k] for i in range(n)) - pulp.lpSum(x[j, i, k] for i in range(n))) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Solve the problem
status = problem.solve()
print("Status:", pulp.LpStatus[status])

# Output results
for k in range(m):
    print(f"Robot {k} Tour:", end=" ")
    tour = [0]
    while True:
        j_list = [j for j in range(1, n) if pulp.value(x[tour[-1], j, k]) == 1]
        if len(j_list) == 0:
            break
        tour.append(j_list[0])
    tour.append(0)  # return to depot
    print(tour)
    cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Total Travel Cost: {cost}")

total_cost = sum(cost[tour[i], tour[i+1]] for k in range(m) for i in range(len(tour)-1))
print("Overall Total Travel Cost:", total_cost)