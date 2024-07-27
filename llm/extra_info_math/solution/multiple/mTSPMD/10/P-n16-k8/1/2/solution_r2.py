import math
from pulp import *

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robots & their depots
robots = list(range(8))  # IDs: 0 to 7
depots = list(range(8))  # Depots are at cities 0 to 7

# Compute Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Optimization problem
prob = LpProblem("VRP_with_Multiple_Depots_and_Robots", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for k in robots for i in range(n) for j in range(n)], 0, 1, LpBinary)

# Objective function
prob += lpSum(distance_matrix[i][j] * x[i, j, k] for k in robots for i in range(n) for j in range(n))

# Constraints
# Each robot starts and ends at its assigned depot
for k in robots:
    prob += lpSum(x[i, k, k] for i in range(n) if i != k) == 1  # Return to depot
    prob += lpSum(x[k, j, k] for j in range(n) if j != k) == 1  # Leave depot

# Visit each city exactly once
for j in range(n):
    prob += lpSum(x[i, j, k] for k in robots for i in range(n)) == 1  # Visitation by some robot, each city

# Subtour elimination constraints
for k in robots:
    u = LpVariable.dicts(f'u_{k}', range(n), lowBound=0, upBound=n-1, cat=LpInteger)
    for i in range(n):
        for j in range(n):
            if i != j:
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
prob.solve()

# Outputting results
if LpStatus[prob.status] == 'Optimal':
    total_cost = 0
    for k in robots:
        print(f"Robot {k} Tour: ", end="")
        path = []
        for i in depots:
            next_city = i
            while True:
                for j in range(n):
                    if x[next_city, j, k].varValue == 1 and j not in path:
                        path.append(j)
                        next_city = j
                        break
                else:
                    break
            if path[-1] == i:
                break
        path.append(path[0])  # returning to starting depot
        print(path)
        tour_cost = sum(distanceix[iath]")  # ➔ print total cost