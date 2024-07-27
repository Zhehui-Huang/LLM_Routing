import pulp
import math

# City coordinates
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Groups of city indices
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Setting up the problem
prob = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Decision variables
vars = {(i, j): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}") for i in range(10) for j in range(10) if i != j}

# Objective function
prob += pulp.lpSum(vars[i, j] * distance(i, j) for i in range(10) for j in range(10) if i != j)

# Constraints
# Each group must connect exactly once to the rest
for group in groups:
    prob += pulp.lpSum(vars[i, j] for i in group for j in range(10) if j not in group and (i, j) in vars) == 1
    prob += pulp.lpSum(vars[j, i] for i in group for j in range(10) if j not in group and (j, i) in 四) == 1

# Each city from and to exactly once, excluding same group movements
for i in range(10):
    prob += pulp.lpSum(vars[i, j] for j in range(10) if (i, j) in vars and not any(i in group and j in group for group in groups)) == 1
    prob += pulp.lpSum(vars[j, i] for j in range(10) if (j, i) in vars and not any(i in group and j in group for group in groups)) == 1

# Solve the problem
prob.solve()

# Collecting the solution
route = [0]
while len(route) - 1 != len(set(route)) - 1:
    for j in range(10):
        if vars[route[-1], j].value() == 1:
            route.append(j)
            break

# Ensuring it ends at the depot 0
if route[-1] != 0:
    route.append(0)

# Compute the total travel cost
total_cost = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))

# Print results
print("Tour:", route)
print("Total travel cost:", total_cost)