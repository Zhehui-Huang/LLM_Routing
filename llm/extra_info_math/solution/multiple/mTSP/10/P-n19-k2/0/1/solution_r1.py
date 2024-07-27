import pulp
from math import sqrt

def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Define the problem
problem = pulp.LpProblem("VRP_for_Robots", pulp.LpMinimize)

# Coordinates of cities including the depot
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
               (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]
n = len(coordinates)  # total nodes including depot
m = 2  # number of robots

# Create the decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum(euclidean_distance(coordinates[i], coordinates[j]) * x[(i,j,k)] for k in range(m) for i in range(n) for j in range(n))

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m)) == 1

# Flow conservation, each node except the depot must be entered and left exactly once
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[(i, j, k)] for i in range(n)) - pulp.lpSum(x[(j, i, k)] for i in range(n)) == 0

# Salesman leaves and enters the depot
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[(i, 0, k)] for i in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[(i, j, k)] <= n - 1

# Solve the problem
problem.solve()

# Collect and print the results
for k in range(m):
    tour = [0]
    next_city = 0
    while True:
        next_city = next(j for j in range(1, n) if pulp.value(x[(next_city, j, k)]) == 1)
        if next_city == 0:
            tour.append(next_city)
            break
        else:
            tour.append(next_city)
    cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")

overall_cost = sum(euclidean_distance(coordinates[i], coordinates[j]) * value for k in range(m) for (i, j), value in x.items() if value == 1)
print(f"Overall Total Travel Cost: {overall_cost}")