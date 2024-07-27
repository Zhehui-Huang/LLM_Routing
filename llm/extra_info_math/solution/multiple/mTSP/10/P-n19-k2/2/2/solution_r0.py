import pulp
import math

# Define the coordinates of the cities including the depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of salesmen (robots)
num_salesmen = 2
n = len(cities)  # number of nodes including the depot

# Calculate Euclidean distance between each pair of nodes
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the problem variable to minimize total distance
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables: x[i][j][k] = 1 if salesman k travels from i to j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(num_salesmen) if i != j),
                          cat=pulp.LpBinary)

# Continuous variable for subtour elimination
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat=pulp.LpContinuous)

# Objective function: Minimize the total distance traveled
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) for k in range(num_salesmen) if i != j)

# Constraints

# Each non-depot city is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(num_salesmen) if i != j) == 1

# Each salesman leaves the depot and returns to the depot
for k in range(num_salesmen):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation: enter and leave each city exactly once for each robot
for k in range(num_salesmen):
    for city in range(1, n):
        problem += pulp.lpSum(x[i, city, k] for i in range(n) if i != city) - pulp.lpSum(x[city, j, k] for j in range(n) if j != city) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(num_salesmen):
                problem += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Solve the problem
status = problem.solve()
if status == pulp.LpStatusOptimal:
    print("Solution found.")
else:
    print("No optimal solution found.")

# Collect the results
tours = [[0] for _ in range(num_salesmen)]
costs = [0 for _ in range(num_salesmen)]
for k in range(num_salesmen):
    cur_city = 0
    while True:
        next_city = next(j for j in range(n) if j != cur_city and pulp.value(x[cur_city, j, k]) == 1)
        tours[k].append(next_city)
        costs[k] += distance(cur_city, next_city)
        cur_city = next_city
        if cur_city == 0:
            break
    tours[k].append(0)
    costs[k] += distance(tours[k][-2], 0)

# Display the results
overall_cost = sum(costs)
for k in range(num_salesmen):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Cost: {overall_cost}")