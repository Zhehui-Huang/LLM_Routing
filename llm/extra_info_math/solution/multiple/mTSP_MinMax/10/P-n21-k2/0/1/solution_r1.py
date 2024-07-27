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

# Objective function
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Constraints
# Each city is visited and left exactly once by exactly one salesman:
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1
for i in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for j in range(n) if i != j for k in range(m)) == 1

# Flow conservation
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Travel cost conditions for each robot should not exceed max distance
for k in range(m):
    problem += pulp.lpSum(x[i, j, k] * distance(i, j) for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem
problem.solve()

# Output the results
for k in range(m):
    tour = [0]
    for i in range(n):
        next_city = next(j for j in range(n) if pulp.value(x[tour[-1], j, k]) == 1)
        tour.append(next_city)
        if next_city == 0:
            break
    travel_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {travel_cost:.2f}")

max_distance_value = pulp.value(max_distance)
print(f"Maximum Travel Cost: {max_distance_value:.2f}")