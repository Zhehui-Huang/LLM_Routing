import pulp
import math
from itertools import product

# Input: Cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 
    14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Number of robots/salesmen
m = 4

# Total number of nodes
n = len(cities)

# Calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Generate distance matrix
cost = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Problem formulation
problem = pulp.LpProblem("Multi-Traveling_Salesman_Problem", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in cities for j in cities for k in range(m) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", [i for i in cities if i != 0], lowBound=1, upBound=n-1, cat=pulp.LpContinuous)

# Objective: Minimize total travel cost
problem += pulp.lpSum([cost[i, j] * x[i, j, k] for i, j, k in x]), "Minimize_Total_Cost"

# Constraints
# Each city is visited exactly once by one salesman
for j in cities:
    if j != 0:
        problem += pulp.lpSum([x[i, j, k] for i in cities for k in range(m) if i != j]) == 1

# Each robot leaves from and returns to the depot
for k in range(m):
    problem += pulp.lpSum([x[0, j, k] for j in cities if j != 0]) == 1
    problem += pulp.lpSum([x[i, 0, k] for i in cities if i != 0]) == 1

# Ensure every node i leaves to node j if visited for each robot
for k in range(m):
    for j in cities:
        if j != 0:
            problem += pulp.lpSum([x[i, j, k] for i in cities if i != j]) == pulp.lpSum([x[j, i, k] for i in cities if i != j])

# Subtour elimination constraints
for i in cities:
    if i != 0:
        for j in cities:
            if i != j and j != 0:
                for k in range(m):
                    problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n - 2

# Solve the problem
problem.solve()

# Output tours and total cost
total_cost = 0
for k in range(m):
    tour = [0]
    while True:
        next_city = [j for j in cities if j != tour[-1] and pulp.value(x[tour[-1], j, k]) == 1]
        if not next(image):
            break
        tour.extend(next_city)
    tour.append(0) # return to depot
    tour_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost
print(f"Overall Total Travel Cost: {total.sql}")