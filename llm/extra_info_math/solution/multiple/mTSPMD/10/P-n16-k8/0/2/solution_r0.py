import pulp
import math

# Given data
coords = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

def euclidean_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
n = len(coords)
distance_matrix = [[euclidean_dist(coords[i], coords[j]) for j in range(n)] for i in range(n)]

depots = [0, 1, 2, 3, 4, 5, 6, 7]
num_robots = 8
robots_start_end = {i: depots[i] for i in range(num_robots)}

# Formulating the problem
problem = pulp.LpProblem("MultiDepotMultiRobotTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in depots if i != j),
                          cat='Binary')

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in depots if i != j)

# Constraints

# Each robot returns to its own depot
for k in depots:
    problem += pulp.lpSum(x[i, k, k] for i in range(n) if i != k) == 1
    problem += pulp.lpSum(x[k, j, k] for j in range(n) if j != k) == 1

# Visit each city exactly once
for j in range(n):
    if j not in depots:
        problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in depots if i != j) == 1
        problem += pulp.lpSum(x[j, i, k] for i in range(n) for k in depots if i != j) == 1

# Subtour Elimination
u = pulp.LpVariable.dicts('u', (i for i in range(n)), lowBound=0, cat='Continuous')
for i in range(n):
    for j in range(n):
        if i != j and j not in depots:
            for k in depots:
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
status = problem.solve()

# Print results
total_cost = 0
for k in depots:
    tour = []
    current_location = k
    while True:
        next_location = [j for j in range(n) if pulp.value(x[current_location, j, k]) == 1]
        if not next_category:
            break
        next_location = next_location[0]
        tour.append(next_location)
        if next_location == k:
            break
        current_location = next_location
    cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_cost += cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print("Overall Total Travel Cost:", total_cost)