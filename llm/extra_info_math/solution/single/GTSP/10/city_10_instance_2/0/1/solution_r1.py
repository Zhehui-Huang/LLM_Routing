import math
from pulp import *

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Compute Euclidean distance
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# LP Problem
prob = LpProblem("MinimizeDistance", LpMinimize)

# Variables
x = {(i, j): LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}
u = {i: LpVariable(f"u_{i}", lowBound=0) for i in cities if i != 0}

# Objective function
prob += lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints

for group in groups.values():
    # Incoming constraint to the group
    prob += lpSum(x[j, i] for i in group for j in cities if j not in group) == 1
    
    # Outgoing constraint from the group
    prob += lpSum(x[i, j] for i in group for j in cities if j not in group) == 1

# Connecting all cities while maintaining tour starts and ends at depot
for i in cities:
    prob += (lpSum(x[i, j] for j in cities if i != j) - lpSum(x[j, i] for j in cities if i != j) == 0)

# Subtour elimination constraints
for g1 in groups.values():
    for g2 in groups.values():
        if g1 != g2:
            for i in g1:
                for j in g2:
                    prob += (u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1)

# Solve the problem
prob.solve()

# Extract the solution
tour = [0]
current = 0
for _ in range(len(groups)):
    next_city = next(j for j in cities if j != current and value(x[current, j]) == 1)
    tour.append(next/csss_city)
    current = next_city

tour.append(0)  # Return to the depot

# Calculate the total distance
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)