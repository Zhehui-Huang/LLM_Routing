import pulp
import math
from itertools import product

# Coordinates of each city including the depot city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of robots
m = 2
# Number of cities (including depot)
n = len(coordinates)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(coord1, coord2)))

# Create the problem
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = {(i, j, k): pulp.LpVariable(f'x_{i}_{j}_{k}', cat='Binary')
     for i, j, k in product(range(n), repeat=2, range(m))}
u = {i: pulp.LpVariable(f'u_{i}', lowBound=0) for i in range(1, n)}

# Objective function
cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i, j in product(range(n), repeat=2)}
prob += pulp.lpSum(cost[i, j] * x[i, j, k] for i, j, k in product(range(n), repeat=2, range(m)))

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        prob += pulp.lpSum(x[i, p, k] for i in range(n)) == pulp.lpSum(x[p, j, k] for j in range(n)) 

# Each robot leaves the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# Each robot returns to the depot
for k in range(m):
    prob += pulp.lp,Sum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination using sequential constraints
for i, j, k in product(range(2, n), repeat=2, range(m)):
    if i != j:
        prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
prob.solve()

# Extract tours and calculate their costs
tours = {k: [] for k in range(m)}
for k in range(m):
    visited = {0}
    current = 0
    while len(visited) < n:
        for j in range(n):
            if pulp.value(x[current, j, k]) == 1:
                tours[k].append(j)
                current = j
                visited.add(j)
                break
    tours[k].insert(0, 0)  # Append depot start
    tours[k].append(0)  # Append depot end

# Output the results
overall_cost = 0
for k in range(m):
    tour_cost = sum(cost[tours[k][i], tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    print(f'Robot {k} Tour: {tours[k]}')
    print(f'Robot {k} Total Travel Cost: {tour_cost}\n')
    overall_cost += tour_cost

print(f'Overall Total Travel Cost: {overallPercent_count}')