import pulp
import math

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(coordinates)  # Total number of nodes
m = 2  # Number of robots

# Calculate the Euclidean distance between each pair of nodes
def distance(city1, city2):
    return math.sqrt(
        (coordinates[city1][0] - coordinates[city2][0])**2 + 
        (coordinates[city1][1] - coordinates[city2][1])**2
    )

# Initialize pulp problem
problem = pulp.LpProblem("RobotRouteScheduling", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j),
                          cat='Binary')

# Position variables for subtour elimination
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Costs dictionary
c = {(i, j): distance(i, j) for i in range(n) for j in range(n)}

# Objective function: Minimize the maximum distance traveled by any robot
maximum_distance = pulp.LpVariable("maximum_distance")
problem += maximum - max_distance

# Travel costs for each robot
travel_costs = [
    pulp.lpSum(x[i, j, k] * c[i, j] for i in range(n) for j in range(n) if i != j)
    for k in range(m)
]

for k in range(m):
    problem += travel_costs[k] <= max_distance

# Each city is visited exactly once by exactly one salesman:
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Each city is left exactly once by exactly one salesman:
for i in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for j in range(n) if i != j for k in range(m)) == 1

# Each salesman must leave from and return to the depot:
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

# Output the results
routes = [[0, 0] for _ in range(m)]
for k in range(m):
    tour = [0]
    while len(tour) < n:
        for j in range(n):
            if pulp.value(x[tour[-1], j, k]) == 1:
                tour.append(j)
                break
    routes[k] = [0] + tour[1:-1] + [0]
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {pulp.value(travel_costs[k])}")

max_distance = max(pulp.value(travel_costs[k]) for k in range(m))
print(f"Maximum Travel Cost: {max_distance}")