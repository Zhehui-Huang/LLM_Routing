import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of robots (salesmen)
m = 8
# Total number of nodes including the depot
n = len(coordinates)

# Create the distance matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective function
problem += pulp.lpSum(c[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m)), "Total Cost"

# Constraints
# Each city visited exactly once
for j in range(1, n):  # Skip the depot
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1, f"One visit to city {j}"
    
# Each salesman starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1, f"Salesman {k} leaves depot"
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1, f"Salesman {k} returns depot"

# Subtour elimination and flow conservation
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n)) - pulp.lpSum(x[j, i, k] for i in range(n)) == 0, f"Flow conservation at city {j} for salesman {k}"

# Subtour elimination constraints (MTZ)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1, f"Subtour_{i}_{j}_{k}"

# Solve the problem
problem.solve()

# Get the result and format output
total_cost = 0
for k in range(m):
    tour = [0]
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j, k]) == 1:
                if j != 0:
                    tour.append(j)
    tour.append(0)  # Return to depot
    tour_cost = sum(c[tour[p]][tour[p+1]] for p in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel STD_cost: {total_cost:.2f}")