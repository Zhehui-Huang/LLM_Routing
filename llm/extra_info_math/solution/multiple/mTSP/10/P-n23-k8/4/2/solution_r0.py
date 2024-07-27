from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Data setup
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
n = len(cities)
m = 8  # number of robots

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
c = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Problem definition
prob = LpProblem("M-TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", (range(n), range(n), range(m)), cat=LpBinary)
u = LpVariable.dicts("u", range(1, n), lowBound=0)

# Objective function
prob += lpSum(c[i, j] * x[i][j][k] for i in range(n) for j in range(n) if i != j for k in range(m))

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += lpSum(x[i][j][k] for i in range(n) if i != j for k in range(m)) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        prob += lpSum(x[p][j][k] for j in range(n) if j != p) - lpSum(x[i][p][k] for i in range(n) if i != p) == 0

# Each salesman leaves the depot
for k in range(m):
    prob += lpSum(x[0][j][k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * lpSum(x[i][j][k] for k in range(m)) <= n - 2

# Solve problem
prob.solve()

# Output solution
total_cost = 0
for k in range(m):
    print(f"Robot {k} Tour:", end=" ")
    tour = []
    for i in range(n):
        for j in range(n):
            if x[i][j][k].value() == 1:
                tour.append(i)
    tour.append(tour[0])
    print(tour)
    tour_cost = sum(c[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")