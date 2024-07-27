import pulp
import math

# Known data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
n = len(coordinates)
m = 4  # Number of robots

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create problem instance
problem = pulp.LpProblem("VRP_Multiple_Salesmen_MinMax", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat='Continuous')

# Cost matrix
cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Minimize the maximum cost among all robots
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Constraints
# Each city exactly once by any salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Salesman starts from the depot and comes back
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Subtour prevention
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n * x[i, j, k] for k in range(m)) <= n - 1

# Cost limitation
for k in range(m):
    problem += pulp.lpSum(cost[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem
problem.solve()

# Retrieving and printing solution
if pulp.LpStatus[problem.status] == 'Optimal':
    print("Optimal solution found.")
    for k in range(m):
        route = [0]
        while True:
            current_city = route[-1]
            next_city = next((j for j in range(n) if x[current_city, j, k].value() == 1), None)
            if next_city is None or next_city == 0:
                break
            route.append(next_city)
        route.append(0)  # Return to depot
        # Calculate tour cost
        tour_cost = sum(cost[route[i], route[i+1]] for i in range(len(route)-1))
        print(f'Robot {k} Tour: {route}')
        print(f'Robot {k} Total Travel Cost: {tour_lek}')
    print(f'Maximum Travel Cost: {max_distance.value()}')
else:
    print("No optimal solution found.")