import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, value

# Coordinates including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), 
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), 
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), 
    (139, 182)
]

n = len(coordinates)  # Total number of nodes including the depot
m = 4                # Number of salesmen

# Distance matrix
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the LP model
problem = LpProblem("VRP_with_Multiple_Robots", LpMinimize)

# Variables
x = [[[LpVariable(f"x_{k}_{i}_{j}", cat=LpBinary) for j in range(n)] for i in range(n)] for k in range(m)]
u = [LpVariable(f"u_{i}", lowBound=1, upBound=n-1, cat='Continuous') for i in range(1, n)]

# Objective function
problem += lpSum(c[i][j] * x[k][i][j] for k in range(m) for i in range(n) for j in range(n))

# Constraints
# Each city must be visited exactly once by exactly one salesman
for j in range(1, n):
    problem += lpSum(x[k][i][j] for k in range(m) for i in range(n) if i != j) == 1

# Each salesman starts and ends at the depot
for k in range(m):
    problem += lpSum(x[k][0][j] for j in range(1, n)) == 1
    problem += lpSum(x[k][j][0] for j in range(1, n)) == 1

# Each city must have one arrival and one departure
for k in range(m):
    for j in range(1, n):
        problem += lpSum(x[k][i][j] for i in range(n) if i != j) == lpSum(x[k][j][i] for i in range(n) if i != j)

# Subtour elimination constraints
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                problem += u[i-1] - u[j-1] + (n-1) * x[k][i][j] <= n - 2

# Solve the problem
problem.solve()

# Extract tours and calculate their costs
tours = {k: [] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if x[k][i][j].varValue == 1:
                tours[k].append((i, j))

# Reformat tours into readable form and calculate costs
def get_next_city(current, tour):
    return [x for x, y in tour if x == current][0]

final_tours = {k: [] for k in range(m)}
total_costs = {k: 0 for k in range(m)}
overall_cost = 0

for k in range(m):
    city = 0  # start at the depot
    while True:
        next_cities = [y for x, y in tours[k] if x == city]
        if not next_cities:
            break
        next_city = next_cities[0]
        final_tours[k].append((city, next_city))
        total_costs[k] += c[city][next_city]
        city = next_city
        if city == 0:
            break

# Output information
for k in range(m):
    tour_list = [i for i, j in final_tours[k]] + [0]
    print(f"Robot {k} Tour: {tour_list}")
    print(f"Robot {k} Total Travel Cost: {total_costs[k]}")
    overall_cost += total_costs[k]

print(f"Overall Total Travel Cost: {overall_cost}")