import pulp
import math
from itertools import chain, combinations

# Data
coords = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
          (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
          (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
          (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
          (155, 185), (139, 182)]
demand = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 
          1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
capacity = 6000

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create Cost Matrix
n = len(coords)
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[(i, j)] = euclidean_distance(coords[i], coords[j])
        else:
            cost_matrix[(i, j)] = 0

# Problem
prob = pulp.LpProblem("CVRP", pulp.LpMinimize)

# x_{rij}
x = pulp.LpVariable.dicts("x", [(r, i, j) for r in range(num_robots) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Objective: minimize travel costs
prob += pulp.lpSum(cost_matrix[i, j] * x[r, i, j] for r in range(num_robots) for i in range(n) for j in range(n) if i != j)

# Subject to:

# Each city visited exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[r, i, j] for r in range(num_robots) for i in range(n) if i != j) == 1

# Each robot leaves the depot
for r in range(num_robots):
    prob += pulp.lpSum(x[r, 0, j] for j in range(1, n)) == 1

# Flow preservation
for r in range(num_robots):
    for j in range(1, n):
        prob += (pulp.lpSum(x[r, i, j] for i in range(n) if i != j) - pulp.lpSum(x[r, j, k] for k in range(n) if j != k)) == 0

# Capacity constraints
for r in range(num_robots):
    prob += pulp.lpSum(demand[j] * x[r, i, j] for i in range(n) for j in range(1, n) if i != j) <= capacity

# Solve
prob.solve()

# Output results
overall_total_cost = 0
for r in range(num_robots):
    print(f"Robot {r} Tour:", end=' ')
    tour = [0]
    while True:
        i = tour[-1]
        next_city = next(j for j in range(n) if j != i and pulp.value(x[r, i, j]) == 1)
        if next_city == 0:
            tour.append(next_city)
            break
        else:
            tour.append(next_city)
    print(tour)

    tour_cost = sum(cost_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {r} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")