import pulp
import math

# Define the cities and their coordinates
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Define the groups
groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to calculate Euclidean distance
def euclidean_dist(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Variables for all pairs of cities
cities = list(range(10))
V = cities + [0]  # Include the depot as starting and ending point

# Create the LP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables x_ij for the route existence between cities i and j
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat='Binary')

# Subtour elimination variables u
u = pulp.LpVariable.dicts("u", (i for i in V if i != 0), lowBound=0, cat='Continuous')

# Objective
objective = pulp.lpSum(euclidean_dist(i, j) * x[(i, j)] for i in V for j in V if i != j)
problem += objective, "Minimizing total travel distance"

# Constraint for exactly one outgoing connection from each group
for grp in groups.values():
    problem += pulp.lpSum(x[(i, j)] for i in grp for j in V if j not in grp) == 1

# Constraint for exactly one incoming connection to each group
for grp in groups.values():
    problem += pulp.lpSum(x[(j, i)] for i in grp for j in V if j not in grp) == 1

# Flow conservation
for i in V:
    problem += (pulp.lpSum(x[(j, i)] for j in V if j != i) - pulp.lpSum(x[(i, j)] for j in V if j != i)) == 0

# Subtour elimination
k = len(groups)
for p in range(1, k):
    for q in range(p+1, k):
        V_p, V_q = groups[p], groups[q]
        problem += (u[p] - u[q] + k * pulp.lpSum(x[(i, j)] for i in V_p for j in V_q) +
                    (k-2) * pulp.lpSum(x[(i, j)] for i in V_q for j in V_p)) <= k-1

# Solve problem
status = problem.solve()
if pulp.LpStatus[status] == 'Optimal':
    print("Tour:", end=" ")
    path = []
    current = 0
    # Deconstruct path from x variables
    while len(path) < len(groups) + 1:
        path.append(current)
        next_moves = [j for j in V if j not in path and pulp.value(x[(current, j)]) == 1]
        if not next_moves:
            break
        current = next_moves[0]
    path.append(0)  # Return to depot

    total_cost = pulp.value(problem.objective)

    print(path)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")