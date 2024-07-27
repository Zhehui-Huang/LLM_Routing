import pulp
from math import sqrt

# Coordinates of all cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance
def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the distance matrix
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Problem parameters
num_cities = len(coordinates)
num_robots = 2

# Define the problem
problem = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Objective
problem += pulp.lpSum(x[i, j, k] * dist_matrix[i][j] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots))

# Constraints
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

for k in range(num_robots):
    for i in range(num_cities):
        problem += pulp.lpSum(x[i, j, k] for j in range(num_cities)) == pulp.lpSum(x[j, i, k] for j in range(num_cities))
    
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Solve the problem
status = problem.solve()
if status == pulp.LpStatusOptimal:
    print("Solution is optimal")
elif status == pulp.LpStatusInfeasible:
    print("Solution is infeasible")

# Output the routes and costs
total_cost = 0
for k in range(num_robots):
    tour = [0]
    next_city = 0
    cost = 0
    while True:
        next_step = [(i, j) for i, j in enumerate(x.keys()) if j[0] == next_city and j[2] == k and pulp.value(x[j]) == 1]
        if not next_step:
            break
        _, (i, j, _) = next_step[0]
        tour.append(j)
        cost += dist_matrix[i][j]
        if j == 0:
            break
        next_city = j
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {round(cost, 2)}")
    total_cost += cost

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")