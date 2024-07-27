from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
from math import sqrt

# Define the city coordinates
coords = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 
    3: (53, 40), 4: (54, 42), 5: (36, 30), 
    6: (52, 82), 7: (93, 44), 8: (21, 78), 
    9: (68, 14), 10: (51, 28), 11: (44, 79), 
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Define the city groups with depot not as part of a cluster
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate distances
def distance(city1, city2):
    x1, y1 = coords[city1]
    x2, y2 = coords[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Define LP problem
problem = LpProblem("RobotTour", LpMinimize)

# Decision Variables
x = {(i, j): LpVariable(f"x_{i}_{j}", cat="Binary") for i in coords for j in coords if i != j}

# Objective function
problem += lpSum(x[i, j] * distance(i, j) for i in coords for j in coords if i != j), "TotalTravelCost"

# Cluster exit and entrance constraints
for group in groups:
    problem += lpSum(x[0, j] for j in group) == 1  # exactly one connection from depot to each group
    problem += lpSum(x[j, 0] for j in group) == 1  # and back

    for city in group:
        problem += lpSum(x[city, j] for j in coords if j != city and j not in group) == 1  # exit each group once
        problem += lpSum(x[j, city] for j in coords if j != city and j not in group) == 1  # enter each group once

# Solve the problem
problem.solve(PULP_CBC_MSG=False)

# Extract the solution
current_city = 0
tour = [current_city]
total_cost = 0

# creating a map for quick lookup
route_map = {(i, j): x[i, j].varValue for (i, j) in x if x[i, j].varValue > 0.999}

while len(tour) < len(groups) + 1:
    for j in coords:
        if j != current_city and (current_city, j) in route_map:
            tour.append(j)
            total_cost += distance(current_city, j)
            current_city = j
            break

# Ending at the depot
tour.append(0)
total cost += distance(current_city, 0)

# Print the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")