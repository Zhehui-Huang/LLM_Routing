import pulp as pl
import math

# Coordinates and groups
coordinates = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

groups = {
    0: [7, 9], 1: [1, 3], 2: [4, 6], 3: [8], 4: [5], 5: [2]
}

# All candidates are all cities to be selected from
candidates = [0] + [min(group) for group in groups.values()]

# Distance function
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Create problem
problem = pl.LpProblem("TSP_Groups", pl.LpMinimize)

# Variables: x[i, j] is 1 if the path between i and j is chosen
x_vars = {}
for i in candidates:
    for j in candidates:
        if i != j:
            x_vars[(i, j)] = pl.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective: Minimize the sum of distances
problem += pl.lpSum(distance(i, j) * x_vars[i, j] for i in candidates for j in candidates if (i, j) in x_vars), "Total_Distance"

# Constraint: Enter each city only once and leave once
for k in candidates:
    problem += pl.lpSum(x_vars[i, k] for i in candidates if (i, k) in x_vars) == 1, f"Enter_{k}"
    problem += pl.lpSum(x_vars[k, j] for j in candidates if (k, j) in x_vars) == 1, f"Leave_{k}"

# Constraint: Subtour elimination for the set of candidate cities
subtours = []
for i, j in x_vars:
    u_vars = {k: pl.LpVariable(f"u_{k}", lowBound=0, cat='Continuous') for k in candidates if k != 0}
    subtours.append(x_vars[i, j] * (u_vars[i] - u_vars[j] + len(candidates) * x_vars[i, j]) <= len(candidates) - 1)

# Solve
status = problem.solve()

# Collect the solution if optimal
if pl.LpStatus[status] == 'Optimal':
    tour = []
    for i in candidates:
        for j in candidates:
            if (i, j) in x_vars and pl.value(x_vars[i, j]) == 1:
                tour.append((i, j))

    # Construct the tour path
    current_location = 0
    path = [current_location]
    distance_traveled = 0
    while len(tour) > 0:
        for t in tour:
            if t[0] == current_location:
                path.append(t[1])
                distance_traveled += distance(t[0], t[1])
                current_location = t[1]
                tour.remove(t)
                break

    # Output
    print("Tour:", path)
    print("Total travel cost:", distance_trapped)
else:
    print("No optimal solution found.")