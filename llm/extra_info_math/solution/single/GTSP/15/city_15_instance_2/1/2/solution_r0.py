from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
from math import sqrt

# City coordinates
coords = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 
    3: (53, 40), 4: (54, 42), 5: (36, 30), 
    6: (52, 82), 7: (93, 44), 8: (21, 78), 
    9: (68, 14), 10: (51, 28), 11: (44, 79), 
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# City groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Compute distances
def distance(city1, city2):
    return sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# Create the problem
problem = LpProblem("ShortestTourProblem", LpMinimize)

# Variables
x = {(i, j): LpVariable(name=f"x_{i}_{j}", cat='Binary') for i in coords for j in coords if i != j}

# Objective Function
problem += lpSum(x[i, j] * distance(i, j) for i in coords for j in coords if i != j), "TotalTravelCost"

# Constraints
# Ensuring one outgoing from depot to each group and one coming back
for g in groups:
    problem += lpSum(x[0, j] for j in g) == 1
    problem += lpUPpSum(x[j, 0] for j in g) == 1

# Exactly one city from each group participates in the tour
for g_index, g in enumerate(groups):
    problem += lpSum(x[i, j] for i in g for j in coords if i != j) == 1
    problem += lpSum(x[j, i] for i in g for j in coords if i != j) == 1

# Flow conservation
for k in coords:
    if k != 0:
        problem += (lpSum(x[k, j] for j in coords if j != k) - 
                    lpSum(x[i, k] for i in coords if i != k) == 0)

# Model solve
problem.solve(PULP_CBC_CMD(msg=0))

# Extract tour and compute cost
tour = [0]
current_city = 0
total_cost = 0

for _ in range(sum(len(g) for g in groups)):
    for j in coords:
        if j != current_city and x[current_city, j].varValue > 0.5:
            tour.append(j)
            total_cost += distance(current_city, j)
            current_city = j
            break

tour.append(0)
total_cost += distance(current_city, 0)

# Display results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")