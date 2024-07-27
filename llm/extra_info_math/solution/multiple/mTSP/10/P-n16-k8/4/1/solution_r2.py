import pulp
import math

# Define the coordinates of the cities (including the depot)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

n = len(coordinates)  # Number of nodes including depot
m = 8  # Number of salesmen (robots)

# Distance function
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Problem setup
problem = pulp.LpProblem("VRP_multivehicle", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat=pulp.LpContinuous)

# Objective
problem += pulp.lpSum(distance(i, j) * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Visit each city exactly once by any salesman except the depot
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

# Each vehicle should leave the depot
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1

# Each vehicle should return to the depot
for k in range(m):
    problem += pulp.lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

# Connectivity from every city
for j in range(1, n):
    for k in range(m):
        problem += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) == pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j)

# Subtour prevention constraints (MTZ)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[(i, j, k)] <= n - 2

# Solve the problem
problem.solve()

# Print the solution
overall_cost = 0
for k in range(m):
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[(i, j, k)]) == 1:
                tour.append((i, j))
    actual_tour = [0]  # Start from depot
    while tour:
        next_city = [t[1] for t in tour if t[0] == actual_tour[-1]]
        if not next_city:
            break
        next_city = next_city[0]
        actual_tour.append(next_city)
        tour = [t for t in tour if t[0] != actual_tour[-2]]
    actual_tour.append(0)  # Return to depot
    tour_cost = sum(distance(actual_tour[i], actual_tour[i + 1]) for i in range(len(actual_tour) - 1))
    print(f"Robot {k} Tour:", actual_tour)
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print("Overall Total Travel Cost:", overall_rosst)