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

# Create problem instance
problem = pl.LpProblem("MinimizeTourCost", pl.LpMinimize)

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 
                     + (coordinates[city1][1] - coordinates[city2][1])**2)

# Variables
x = pl.LpVariable.dicts("x",
                        [(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j],
                        cat='Binary')

# Objective: Minimize the total travel cost
problem += pl.lpSum([distance(i, j) * x[i, j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j]), "TotalTravelCost"

# Constraints for ensuring exact one entry and exit in each cluster
for group in groups:
    problem += pl.lpSum([x[i][j] for i in group for j in range(len(coordinates)) if i != j]) == 1, f"One_outgoing_from_group_{group}"
    problem += pl.lpSum([x[j][i] for i in group for j in range(len(coordinates)) if i != j]) == 1, f"One_incoming_to_group_{group}"

# Constraint for depot
problem += pl.lpSum([x[0][j] for j in range(1, len(coordinates))]) == len(groups), "Outflow_from_depot"
problem += pl.lpSum([x[j][0] for j in range(1, len(coordinates))]) == len(groups), "Inflow_to_depot"

# Flow conservation for all nodes except depot
for i in range(1, len(coordinates)):
    problem += (pl.lpSum(x[j][i] for j in range(len(coordinates)) if i != j) -
                pl.lpSum(x[i][j] for j in range(len(coordinates)) if i != j)) == 0, f"Flow_conservation_at_node_{i}"

# Avoid subtour - Miller-Tucker-Zemlin (MTZ) constraints
u = pl.LpVariable.dicts("u", range(1, len(coordinates)), lowBound=0, cat='Continuous')
for i in range(1, len(coordinates)):
    for j in range(1, len(coordinates)):
        if i != j:
            problem += u[i] - u[j] + len(coordinates) * x[i, j] <= len(coordinates) - 1

# Solve problem
status = problem.solve()

# Extract tour from variables
tour = []
visited = [0]
current = 0

while True:
    next_city = [j for j in range(len(coordinates)) if j != current and x[current, j].varValue == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city
    if current == 0:
        break

# Compute total distance
total_cost = pl.value(problem.objective)

# Results
tour.insert(0, 0)  # Starting from depot
print("Tour:", tour)
print("Total travel cost:", total_cost)