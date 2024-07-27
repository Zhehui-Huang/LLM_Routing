import pulp
import math

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of robots (salesmen)
m = 8

# City coordinates, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of cities (including the depot)
n = len(coordinates)

# Distance matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Set up the optimization problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum(c[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m)) == 1

# Each salesman must leave the depot exactly once
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1

# Each salesman must return to the depot
for k in range(m):
    problem += pulp.lpSum(x[(i, 0, k)] for i in range(1, n)) == 1

# Each city is entered and left exactly once
for p in range(1, n):
    for k in range(m):
        problem += pulp.lpSum(x[(i, p, k)] for i in range(n)) == pulp.lpSum(x[(p, j, k)] for j in range(n))

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[(i, j, k)] <= n - 1

# Solve the problem
problem.solve()

# Output the results
overall_cost = 0
for k in range(m):
    tour = [0]
    current_city = 0
    while True:
        next_city = next(j for j in range(n) if pulp.value(x[(current_city, j, k)]) == 1)
        if next_city == 0:
            tour.append(next_city)
            break
        tour.append(next_city)
        current_city = next_city
    tour_cost = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")