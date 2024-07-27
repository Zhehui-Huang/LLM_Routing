import math
from pulp import *

# City indices and their coordinates
coords = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232),
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Calculate distance between two cities
def distance(c1, c2):
    (x1, y1), (x2, y2) = coords[c1], coords[c2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Total cities including depot
n = len(coords)

# Define the problem
prob = LpProblem("MTSP", LpMinimize)

# Robots
m = 4  # Number of robots

# Decision variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)], cat='Binary')
u = LpVariable.dicts("u", list(range(1, n)), lowBound=0)

# Objective
prob += lpSum(x[i, j, k] * distance(i, j) for i in range(n) for j in range(n) if i != j for k in range(m))

# Constraints

# Each city is visited exactly once by any salesman
for j in range(1, n):
    prob += lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Flow conservation in each node
for k in range(m):
    for j in range(n):
        prob += lpSum(x[i, j, k] for i in range(n) if i != j) == lpSum(x[j, i, k] for i in range(n) if i != j)

# Leaving and entering depot
for k in range(m):
    prob += lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Solve the problem
prob.solve()

# Extract solution
tours = {k: [] for k in range(m)}
for k in range(m):
    tour = [0]
    next_city = None
    while True:
        next_city = [j for j in range(n) if pulp.value(x[tour[-1], j, k]) == 1]
        if not next_city:
            break
        tour.extend(next_city)
        if next_city == [0]:
            break
    tours[k] = tour

# Output the results
for k in tour:
    print(f'Robot {k} Tour: {tours[k]}')
    tour_cost = sum(distance(tours[k][i], tours[k][i+1]) for i in range(len(tours[k])-1))
    print(f'Robot {k} Total Travel Cost: {tour_cost}')

# Calculate the maximum travel cost among all robots
max_cost = max(sum(distance(tours[k][i], tours[k][i+1]) for i in range(len(tours[k])-1)) for k in tours)
print(f'Maximum Travel Cost: {max_cost}')