import pulp
import math

# City coordinates
cities = {
    0: (35, 40),  # Depot
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Groups of cities, adding depot to the possibilities (modeling choice)
groups = {
    0: [0, 3, 8],
    1: [0, 4, 13],
    2: [0, 1, 2],
    3: [0, 6, 14],
    4: [0, 5, 9],
    5: [0, 7, 12],
    6: [0, 10, 11]
}

# Compute Euclidean distances
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Creating the linear programming problem
problem = pulp.LpProblem("Minimize Distance", pulp.LpMinimize)

# Variables: x_ij = 1 if travel from i to j, otherwise 0
variables = {}
for k in groups:
    for i in groups[k]:
        for j in groups[k]:
            if i != j:
                variables[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

# Objective: Minimize total distance
problem += pulp.lpSum(variables[(i, j)] * distance(cities[i], cities[j]) for (i, j) in variables), "Total Cost"

# Constraints
# Each group must connect to exactly one other node outside of its own group
for k in groups:
    problem += pulp.lpSum(variables[i, j] for i in groups[k] for j in groups[k] if (i, j) in variables) == 2, f"Connectivity_{k}"

# Subtour elimination, ensure entering and leaving each city once
for ci in cities:
    problem += pulp.lpSum(variables[(i, ci)] for i in cities if i != ci and (i, ci) in variables) == \
               pulp.lpSum(variables[(ci, j)] for j in cities if j != ci and (ci, j) in variables), f"Flow_{ci}"

# Solve the problem
status = problem.solve()

# Output results
if pulp.LpStatus[status] == 'Optimal':
    print("Found optimal solution.")
    tour = []
    visited = set()
    current = 0  # starting at the depot
    while True:
        tour.append(current)
        visited.add(current)
        next_city = None
        for j in cities:
            if j != current and (current, j) in variables and pulp.value(variables[(current, j)]) == 1:
                next_city = j
                break
        if next_city == 0 or next_city is None:
            break
        current = next_city
    tour.append(0)  # returning to the depot
    total_cost = pulp.value(problem.objective)
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")