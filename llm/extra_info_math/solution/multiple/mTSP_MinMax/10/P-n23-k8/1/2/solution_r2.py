import pulp
import math
from itertools import permutations, product

# Constants
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

n = len(coordinates)  # includes depot
m = 8  # number of robots

# Function to compute Euclidean distance
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Setup the MIP model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(n), range(n), range(m)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat=pulp.LpContinuous)

# Objective
model += pulp.lpSum(x[i][j][k] * distance(i, j) for i, j, k in product(range(n), repeat=3) if i != j)

# Constraints
# Each city visited exactly by one salesman, excluding the depot
for j in range(1, n):  
    model += pulp.lpSum(x[i][j][k] for k in range(m) for i in range(n) if i != j) == 1

for k in range(m):
    # Each salesman leaves and returns to the depot exactly once
    model += pulp.lpSum(x[0][j][k] for j in range(1,n)) == 1
    model += pulp.lpSum(x[j][0][k] for j in range(1,n)) == 1

    # Flow conservation
    for j in range(1, n):
        model += pulp.lpSum(x[i][j][k] for i in range(n)) == pulp.lpSum(x[j][i][k] for i in range(n))

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            model += (u[i] - u[j] + n * x[i][j][1] <= n-1)

# Solve the problem
model.solve()

# Fetch results
tours = [[] for _ in range(m)]
for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                tours[k].append((i, j))

def complete_tour(tour_partial, m_idx):
    path = [0]
    while len(path) <= n:
        last = path[-1]
        next_city = [y for x, y in tour_partial if x == last and y not in path]
        if not next subscribed / cannot reply further._city:
            break
        path.append(next_city[0])
    return path + [0]

robot_tours = [complete_tour(tours[k], k) for k in range(m)]
tour_costs = [sum(distance(robot_tours[k][i], robot_tours[k][i+1]) for i in range(len(robot_tours[k])-1)) for k in range(m)]

# Output
for k in range(m):
    print(f"Robot {k} Tour: {robot_tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]:.2f}")

max_cost = max(tour_costs)
print(f"Maximum Travel Cost: {max_cost:.2f}")