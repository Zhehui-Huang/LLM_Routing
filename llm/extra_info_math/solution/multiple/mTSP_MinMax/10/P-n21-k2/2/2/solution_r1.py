import numpy as np
import pulp

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Number of cities and number of robots
n = len(coordinates)
m = 2  # number of robots
depot = 0

# Distance matrix calculation
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distance = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Create the problem
problem = pulp.LpProblem("Multi-Depot_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary', lowBound=0, upBound=1)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective: Minimize the maximum distance traveled by any robot
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

for k in range(m):
    problem += pulp.lpSum(distance[i, j] * x[i, j, k] for i in range(n) for j in range(n)) <= max_distance

# Constraints

# Each city is visited exactly once by one of the robots
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot leaves and enters the depot
for k in range(m):
    problem += pulp.lpSum(x[depot, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, depot, k] for j in range(1, n)) == 1

# Subtour elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

# Output results
for k in range(m):
    tour = []
    cost = 0
    for i in range(n):
        for j in range(n):
            if x[i, j, k].varValue == 1:
                if len(tour) == 0 or tour[-1] != i:
                    tour.append(i)
                tour.append(j)
                cost += distance[i, j]
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_distance.varValue}")