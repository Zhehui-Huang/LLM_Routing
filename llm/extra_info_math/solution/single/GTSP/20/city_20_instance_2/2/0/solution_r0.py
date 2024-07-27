import numpy as np
import pulp

# Define the city coordinates and groups
city_coordinates = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
                    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
                    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
                    (51, 58), (30, 48)]
groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]

# Calculate Euclidean distances
def euclidean_distance(i, j):
    xi, yi = city_coordinates[i]
    xj, yj = city_coordinates[j]
    return np.sqrt((xi - xj)**2 + (yi - yj)**2)

# Number of the groups
k = len(groups)
V = [0] + [city for group in groups for city in group]  # Expanded list of cities including depot
n = len(V)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables: x_ij = 1 if travel from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat='Binary')

# Objective Function
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in V for j in V if i != j), "TotalTravelCost"

# Constraints for exactly one edge entering and leaving each city set
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in V if i != j) == 1  # exactly one outgoing from group
    problem += pulp.lpSum(x[(i, j)] for j in group for i in V if i != j) == 1  # exactly one incoming to group

# Constraints to ensure path continuity (flow conservation)
for i in V:
    problem += pulp.lpSum(x[(j, i)] for j in V if i != j) - pulp.lpSum(x[(i, j)] for j in V if i != j) == 0

# Subtour elimination using additional variables (MTZ constraints)
u = pulp.LpVariable.dicts("u", (i for i in V if i != 0), lowBound=0, cat=pulp.LpContinuous)
M = k + 1
for i in V:
    if i != 0:
        for j in V:
            if j != 0 and i != j:
                problem += u[i] - u[j] + M * x[(i, j)] <= M - 1

# Solve the problem using a solver
solver = pulp.getSolver('PULP_CBC_CMD', msg=True)
problem.solve(solver)

# Extract the tour order and total cost
tour = [0]
for _ in range(k):
    current = tour[-1]
    next_city = [j for j in V if pulp.value(x[(current, j)]) == 1][0]
    tour.append(next_city)

tour.append(0)  # return to depot
total_cost = pulp.value(problem.objective)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")