import pulp
import math

# Define the coordinates of the cities (including the depot)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distance between cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

n = len(coordinates)  # Number of nodes including depot
m = 8  # Number of salesmen

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = {}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j:
                x[(i, j, k)] = pulp.LpVariable(f"x_{i}_{j}_{k}", 0, 1, pulp.LpBinary)

u = pulp.LpVariable.dicts("u", [i for i in range(1, n)], lowBound=1, cat='Continuous')

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in range(m)), "Total Travel Cost"

# Constraints
for j in range(1, n):
    problem += sum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Solve the problem
problem.solve()

# Output the results
overall_cost = 0
for k in range(m):
    tour = [0]
    # Find the start of each tour
    for j in range(1, n):
        if pulp.value(x[0][j][k]) == 1:
            tour.append(j)
            break
    # Follow the tour
    while True:
        i = tour[-1]
        next_city = [j for j in range(n) if i != j and pulp.value(x[i][j][k]) == 1]
        if next_city:
            next_city = next_city[0]
            if next_city == 0:
                tour.append(0)
                break
            else:
                tour.append(next_city)
        else:
            break
    print(f"Robot {k} Tour: {tour}")
    tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")