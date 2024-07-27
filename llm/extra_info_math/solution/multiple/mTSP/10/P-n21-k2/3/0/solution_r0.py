import pulp as pl
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

n = len(coordinates)  # Total number of cities including the depot
m = 2  # Number of robots

# Function to calculate Euclidean distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate cost matrix
c = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Problem definition
problem = pl.LpProblem("VRP_with_Multiple_TSPs", pl.LpMinimize)

# Decision variables: x[i, j, k] is 1 if robot k travels from city i to city j
x = {(i, j, k): pl.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')
     for i in range(n) for j in range(n) if i != j for k in range(m)}

# Positional variables to eliminate subtours
u = {i: pl.LpVariable(f"u_{i}", lowBound=0) for i in range(1, n)}

# Objective
problem += pl.lpSum(c[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in range(m))

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, n):  # exclude the depot for these constraints
    problem += pl.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Flow conservation for each robot and each city
for k in range(m):
    for j in range(1, n):
        problem += pl.lpSum(x[i, j, k] for i in range(n) if i != j) == pl.lpSum(x[j, i, k] for i in range(n) if i != j)
    
# Each robot starts and ends at the depot
for k in range(m):
    problem += pl.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pl.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Solve Problem
problem.solve()

# Checking if problem has an optimal solution
if pl.LpStatus[problem.status] == 'Optimal':
    tours = [[0] for _ in range(m)]
    costs = [0 for _ in range(m)]
    
    for k in range(m):
        current_city = 0
        while True:
            next_city = next(j for j in range(n) if j != current_city and pl.value(x[current_city, j, k]) == 1)
            tours[k].append(next_city)
            costs[k] += c[current_city, next_city]
            current_city = next_city
            if current_city == 0:
                break
    
    for k, tour in enumerate(tours):
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {costs[k]}")
    
    print(f"Overall Total Travel Cost: {sum(costs)}")
else:
    print("No optimal solution found.")