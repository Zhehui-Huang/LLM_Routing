import pulp
import math

# Constants and Data
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
depots = [0, 1]
cities = list(range(len(coordinates)))
robots = 2

# Calculate distances
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
distances = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Optimization problem
problem = pulp.LpProblem("Minimize_Total_Distance", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("route", ((i, j) for i in cities for j in cities if i != j), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("position", (i for i in cities), 0, len(cities))

# Objective function
problem += pulp.lpSum([distances[i, j] * x[i, j] for i in cities for j in cities if i != j]), "Minimize_Total_Travel_Distance"

# Constraints
# Each city must be entered and left only once
for j in cities[2:]:
    problem += pulp.lpSum([x[i, j] for i in cities if (i, j) in x]) == 1, f"Enter_City_{j}"
    problem += pulp.lpSum([x[j, i] for i in cities if (j, i) in x]) == 1, f"Leave_City_{j}"

# Depot start point constraints
problem += pulp.lpSum([x[0, j] for j in cities if j != 0]) == robots, "Start_from_Depot_0"
problem += pulp.lpSum([x[1, j] for j in cities if j != 1]) == robots, "Start_from_Depot_1"

# Subtour elimination constraints
for i in cities[2:]:
    for j in cities[2:]:
        if i != j:
            problem += u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1, f"SubtourConstraint_{i}_{j}"

# Solve the problem
problem.solve()

# Extracting results
routes = [list() for r in range(robots)]
for r in range(robots):
    for i in cities:
        for j in cities:
            if i != j and pulp.value(x[i, j]) == 1:
                if r == 0 and i == 0 or r != 0 and i != 0:
                    routes[r].append(i)

# Output tour and costs
total_costs = 0
for r in range(robots):
    tour = routes[r] + [routes[r][0]]  # Return to initial depo
    tour_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    total_costs += tour_cost
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_costs}")