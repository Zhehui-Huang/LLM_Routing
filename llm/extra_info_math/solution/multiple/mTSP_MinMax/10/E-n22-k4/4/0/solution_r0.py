import pulp
import math
from itertools import product

# Coordinates for each city including the depot as city 0
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Number of nodes and salesmen (robots)
n = len(coordinates)
m = 4

# Costs between each pair of cities
cost = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
problem = pulp.LpProblem("VRP_Multiple_Salesmen_MinMax", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i, j, k in product(range(n), range(n), range(m)) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=1, upBound=n-1, cat='Continuous')

# Objective function: minimize the maximum distance traveled
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Constraints
# Each city is visited exactly once excluding the depot
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation: each robot leaves each city he visits and each robot returns to each city from somewhere
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[(i, j, k)] for i in range(n) if i != j) - pulp.lpSum(x[(j, i, k)] for i in range(n) if i != j) == 0

# Each robot leaves the depot once
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1

# Subtour elimination constraints
for i, j, k in product(range(1, n), range(1, n), range(m)):
    if i != j:
        problem += u[i] - u[j] + (n - 1) * x[(i, j, k)] <= n - 2

# Cost constraints to minimize the maximum distance traveled
for k in range(m):
    problem += pulp.lpSum(cost[(i, j)] * x[(i, j, k)] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Retrieve the tours for each robot and calculate the costs
tours = {k: [] for k in range(m)}
for k in range(m):
    tour = [0]
    next_city = None
    while True:
        next_city = next((j for j in range(n) if x[(tour[-1], j, k)].varValue == 1), None)
        if next_city is None or next_city == 0:
            break
        tour.append(next_city)
    tour.append(0)
    tours[k] = tour

# Calculate and print each robot's tour and cost
max_cost = 0
for k in tours:
    tour_cost = sum(cost[(tours[k][i], tours[k][i+1])] for i in range(len(tours[k])-1))
    max_cost = max(tour_cost, max_cost)
    print(f'Robot {k} Tour: {tours[k]}')
    print(f'Robot {k} Total Travel Cost: {tour_cost:.2f}')

print(f'Maximum Travel Cost: {max_cost:.2f}')