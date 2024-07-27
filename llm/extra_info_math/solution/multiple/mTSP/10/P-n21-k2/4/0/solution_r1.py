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
     for i, j, k in product(range(n), range(n), range(m)) if i != j}
u = {i: pulp.LpVariable(f'u_{i}', lowBound=0) for i in range(1, n)}

# Objective function
cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i, j in product(range(n), repeat=2)}
prob += pulp.lpSum(cost[i, j] * x[i, j, k] for i, j, k in product(range(n), range(n), range(m)) if i != j)

# Constraints
# Each city is visited exactly once by one robot
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        prob += pulp.lpSum(x[i, p, k] for i in range(n) if i != p) == pulp.lpSum(x[p, j, k] for j in range(n) if j != p)

# Each robot leaves and returns to the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination with sequential constraints
for i, j, k in product(range(2, n), repeat=3):
    if i != j:
        prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
prob.solve()

# Extract tours and calculate their costs
tours = {k: [] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if j != i and pulp.value(x[i, j, k]) == 1:
                tours[k].append((i, j))

# Post-process the routes to make them more readable and calculate costs
for k in range(m):
    tour, total_cost = [0], 0
    while len(tour) < n:
        for i, j in tours[k]:
            if i == tour[-1]:
                tour.append(j)
                total_cost += cost[i, j]
                break
    tour.append(0)  # Complete the tour by returning to the depot
    total_cost += cost[tour[-2], 0]  # Add cost of returning to depot
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {total_cost}\n")

# If needed, calculate and print the overall cost
overall_cost = sum(cost[tour[i], tour[i + 1]] for k in tours for i in range(len(tour) - 1))
print(f"Overall Total Travel Cost: {overall_cost}")