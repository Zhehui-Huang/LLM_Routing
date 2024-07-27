import pulp
import math

# City Locations
locations = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

# Number of nodes and robots
n = len(locations)
m = 8

# Calculate cost matrix
c = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Create problem
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j),
                          cat='Binary', lowBound=0, upBound=1)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=(n - 1))

# Objective function
problem += pulp.lpSum(c[i][j] * x[i, j, k] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraint - Each city is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i][j][k] for k in range(m) for i in range(n) if i != j) == 1

# Constraint - Each salesman departs and arrives at the depot exactly once
for k in range(m):
    problem += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[i][0][k] for i in range(1, n)) == 1

# Constraint - Salesman must leave and enter each city exactly once
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i][j][k] for i in range(n) if i != j) == pulp.lpSum(x[j][i][k] for i in range(n) if i != j)

# Subtour Elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - 1) * x[i][j][k] <= n - 2

# Solve the problem
problem.solve()

# Collect results
output = []
max_cost = 0
for k in range(m):
    tour = [0]
    current_city = 0
    tour_cost = 0
    while True:
        next_city = [j for j in range(n) if pulp.value(x[current_city][j][k]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        tour_cost += c[current_city][next_city]
        current_city = next_city
        tour.append(current_city)
        if current_city == 0:
            break
    output.append((tour, tour_cost))
    max_cost = max(max_cost, tour_cost)

# Display output
for idx, (tour, cost) in enumerate(output):
    if len(tour) > 1:  # Only display tours that visit at least one city
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")