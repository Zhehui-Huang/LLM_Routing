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

# Creating the distance matrix
distance_matrix = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variable: x[i, j, k] == 1 if and only if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j),
                          cat='Binary', lowBound=0, upBound=1)

# Continuous variable u for subtour elimination
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=(n - 1))

# The objective function is to minimize the maximum travel cost among all robots
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Constraints
# Each city is visited exactly once by one of the robots
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

# Each robot starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Travel from one city must lead to another city by the same robot
for k in range(m):
    for j in range(1, n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Adding objective-related constraints
for k in range(m):
    problem += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem using a suitable solver
solver = pulp.PULP_CBC_CMD(msg=False)
problem.solve(solver)

# Gather results and calculate costs
tour_results = []
max_tour_cost = 0
for k in range(m):
    path = []
    total_cost = 0
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j, k]) == 1:
                if i == 0 and not path:
                    path.append(i)  # Starting city
                path.append(j)
                total_cost += distance_matrix[i][j]
                if j == 0:
                    break
    if path and path[-1] != 0:  # Ensure return to depot
        path.append(0)
        total_cost += distance_matrix[path[-1]][0]
    if path:
        tour_results.append((path, total_cost))
        max_tour_cost = max(max_tour_cost, total_cost)

# Output the results
for idx, (tour, cost) in enumerate(tour_results):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Maximum Travel Cost: {max_tour_cost:.2f}")