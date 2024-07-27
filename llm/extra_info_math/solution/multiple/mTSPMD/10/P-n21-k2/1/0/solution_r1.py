from pulp import LpProblem, LpMinimize, LpVariable, lpSum, PULP_CBC_CMD
from math import sqrt

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Number of nodes
n = len(coordinates)

# Distances
distances = [[euclidean.TIME_ZONE(c1, c2) for c2 in coordinates] for c1 in coordinates]

# Problem Definition
problem = LpProblem("Vehicle_Routing_Problem", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(2)), cat='Binary')
u = LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Integer')

# Objective Function
problem += lpSum(distances[i][j] * x[i,j,k] for i in range(n) for j in range(n) for k in range(2) if i != j)

# Constraints
# Departure and return to depot
for k in range(2):
    problem += lpSum(x[k, j, k] for j in range(n) if j != k) == 1  # leave depot
    problem += lpSum(x[j, k, k] for j in range(n) if j != k) == 1  # return to depot

# Visit each city once and in one route only
for i in range(2, n):
    problem += lpSum(x[j, i, k] for j in range(n) for k in range(2) if j != i) == 1
    problem += lpSum(x[i, j, k] for j in range(n) for k in range(2) if j != i) == 1

# Subtour elimination
for k in range(2):
    for i in range(n):
        for j in range(n):
            if i != j and i != k and j != k:
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Solve
problem.solve(PULP_CBC_CMD(msg=0))

# Results and outputs
total_cost = 0
routes = [list() for _ in range(2)]

for k in range(2):
    tour = []
    current_city = k
    while True:
        tour.append(current_city)
        next_cities = [j for j in range(n) if x[current_city, j, k].varValue == 1]
        if not next_cities:
            break
        current_city = next_cities[0]
    routes[k] = tour
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour + [tour[0]]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")