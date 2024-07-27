import pulp as pl
import math

# Define the coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Euclidean distance function
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Problem data
num_cities = len(coordinates)
num_robots = 8
depot = 0

# Create the problem variable to contain the problem data
problem = pl.LpProblem("Robot_Routing", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)],
                        cat='Binary', lowBound=0, upBound=1)
u = pl.LpVariable.dicts("u", [i for i in range(1, num_cities)], lowBound=0, cat='Continuous')

# Objective Function: Minimize the total travel cost
problem += pl.lpSum(distance(i, j) * x[i, j, k] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots))

# Constraints
# Visit each city exactly once
for j in range(1, num_cities):
    problem += pl.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Flow conservation
for k in range(num_robots):
    for p in range(num_cities):
        problem += pl.lpSum(x[p, j, k] for j in range(num_cities)) == pl.lpSum(x[j, p, k] for j in range(num_cities))

# Each robot must leave the depot
for k in range(num_robots):
    problem += pl.lpSum(x[depot, j, k] for j in range(1, num_cities)) == 1

# Each robot must return to the depot
for k in range(num_robots):
    problem += pl.lpSum(x[i, depot, k] for i in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Solve the problem
problem.solve()

# Extract solution
tours = [[] for _ in range(num_robots)]
costs = [0 for _ in range(num_robots)]

for k in range(num_robots):
    tour = [depota]
    while True:
        found_next = False
        for j in range(num_cities):
            if pl.value(x[tour[-1], j, k]) == 1:
                tour.append(j)
                costs[k] += distance(tour[-2], j)
                found_next = True
                break
        if not found_next or tour[-1] == depot:
            break
    tours[k] = tour

# Output results
overall_cost = sum(costs)
for k in range(num_robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Overall Total Travel Cost: {overall_cost}")