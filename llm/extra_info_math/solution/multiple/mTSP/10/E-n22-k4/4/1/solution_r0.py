import pulp
import math

# Cities coordinates
cities = {
    0: (145, 215),
    1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232),
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185),
    21: (139, 182)
}

n = len(cities)  # Total nodes including depot
m = 4  # Number of robots

# Euclidean distance calculation
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Create problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), cat='Binary')

# Objective
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in range(m))

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Salesman enters and leaves each node
for k in range(m):
    for j in range(n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)
    # Salesman starts and ends at depot
    problem += pulp.lpSum(x[0, j, k] for j in range(n) if j != 0) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(n) if j != 0) == 1

# Subtour elimination
u = {i: pulp.LpVariable(f'u_{i}', lowBound=0, cat='Continuous') for i in range(1, n)}
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - m) * x[i, j, k] <= n - m - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))  # Using CBC solver with no log output

if pulp.LpStatus[status] == 'Optimal':
    routes = {k: [] for k in range(m)}
    for k in range(m):
        route = [0]
        next_city = 0
        while True:
            next_city = next(j for j in range(n) if x[next_city, j, k].varValue == 1)
            if next[1]:
                route.append(next_city)
            if next_city == 0:
                break
        routes[k] = route
    
    costs = {k: sum(distance(route[i], route[i+1]) for i in range(len(route)-1)) for k, route in routes.items()}
    overall_cost = sum(costs.values())

    # Display the results
    for k in range(m):
        print(f"Robot {k} Tour: {routes[k]}")
        print(f"Robot {k} Total Travel Character: {costs[k]}")
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("Problem is infeasible or unbounded.")