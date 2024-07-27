import pulp as pl
import math

# Coordinates of cities including the depot
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Grouping of cities excluding the depot
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 
                     + (coordinates[city1][1] - coordinates[city2][1])**2)

# Variable Setup
x = pl.LpVariable.dicts("x", 
                        [(i, j) for i in coordinates for j in coordinates 
                         if i != j and (i in [0] or j in [0] or any(i in g for g in groups) or any(j in g for g in groups))],
                        cat='Binary')

u = pl.LpVariable.dicts("u", list(range(1, 15)), lowBound=1, cat='Continuous')

# Problem setup
problem = pl.LpProblem("Minimize_Tour_Cost", pl.LpMinimize)

# Objective Function: Minimize the total distance
problem += pl.lpSum([distance(i, j) * x[(i, j)] for i, j in x]), "Minimize_total_distance"

# Constraints
# Start and return to the depot
problem += pl.lpSum([x[(0, j)] for j in range(1, 15)]) == 1, "One_departure"
problem += pl.lpSum([x[(j, 0)] for j in range(1, 15)]) == 1, "One_return"

# Connecting selected group cities with constraints
for group in groups:
    problem += pl.lpSum([x[(i, j)] for i in group for j in coordinates if i != j]) == 1, f"Exit_edge_from_group_{group}"
    problem += pl.lpSum([x[(j, i)] for i in group for j in coordinates if i != j]) == 1, f"Entry_edge_to_group_{group}"

# Eliminating sub-tours within the groups
constraints = []
for k in range(2, 15):
    for j in range(2, 15):
        if k != j:
            constraints.append(u[k] - u[j] + (len(coordinates) - 1)*x[(k, j)] <= len(coordinates) - 2)

for constraint in constraints:
    problem += constraint

# Solving the problem
problem.solve()

# Obtaining the tour sequence
tour = [0]
for _ in range(14):  # Maximum of 14 movements excluding the initial position
    next_city = [j for i, j in x if i == tour[-1] and pl.value(x[(i, j)]) == 1]
    if not next_city or next_city[0] == 0:
        break
    tour.append(next_city[0])

tour.append(0)  # Return to depot

# Total travel cost calculation
total_cost = pl.value(problem.objective)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)