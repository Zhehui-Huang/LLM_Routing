import pulp
from math import sqrt

# Define the problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# City coordinates (city index starting from 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots and cities
m = 2
n = len(coordinates)

# Distances dictionary
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            dist = sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
            distances[(i, j)] = dist

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", list(range(1, n)), lowBound=1, upBound=n-1, cat='Continuous')

# Objective
problem += pulp.lpSum([distances[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j])

# Constraints
# Each city must be visited exactly once by any salesman (except depot)
for j in range(1, n):
    problem += pulp.lpSum([x[i, j, k] for i in range(n) for k in range(m) if i != j]) == 1

# Each salesman leaves and returns to the depot once
for k in range(m):
    problem += pulp.lpSum([x[0, j, k] for j in range(1, n) if j != 0]) == 1
    problem += pulp.lpSum([x[j, 0, k] for j in range(1, n) if j != 0]) == 1

# Each salesman must leave each visited node and enter each visited node exactly once
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum([x[i, j, k] for i in range(n) if i != j]) == pulp.lpSum([x[j, i, k] for i in range(n) if i != j])

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * pulp.lpSum([x[i, j, k] for k in range(m)]) <= n - 2

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=1))

if status == pulp.LpStatusOptimal:
    print("Optimal Solution Found!")
else:
    print("No Optimal Solution available.")

# Extract the results if a solution is found
if pulp.LpStatus[problem.status] == 'Optimal':
    tour_paths = {}
    for k in range(m):
        tour_paths[k] = []
        for i in range(n):
            for j in range(n):
                if pulp.value(x[(i, j, k)]) == 1:
                    tour_paths[k].append((i, j))
    
    # Process to get human-readable tours
    for k in range(m):
        tour = [0]
        while len(tour_paths[k]) > 0:
            last = tour[-1]
            for i, (s, e) in enumerate(tour_paths[k]):
                if s == last:
                    tour.append(e)
                    tour_paths[k].pop(i)
                    break
        tour.append(0)  # Returning to the depot
        tour_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
    
    max_cost = max(sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1)) for tour in tour_paths.values())
    print(f"Maximum Travel Cost: {max_cost}")
else:
    print("Solution is not feasible.")