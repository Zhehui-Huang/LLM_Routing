import pulp
import math

# Constants and data setup
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

# PuLP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables:
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')  # route decision
u = pulp.LpVariable.dicts("u", (i for i in cities), lowBound=0, cat='Continuous')  # position in tour to prevent subtour

# Objective:
problem += pulp.lpSum([distances[i, j] * x[(i, j)] for i in cities for j in cities if i != j]), "Total Cost"

# Constraints:
# Ensure each city is visited exactly once by any robot
for j in cities:
    problem += sum(x[(i, j)] for i in cities if i != j) == 1, f"Entering_city_{j}"
    problem += sum(x[(j, i)] for i in cities if i != j) == 1, f"Leaving_city_{j}"

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0) and (i, j) in x:
            problem += u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1

# Solve problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))
print("Status:", pulp.LpStatus[status])

# Extract results
tour_edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[i, j]) == 1]

# Organizing the tours - following the edges to create path
def get_tour(start):
    tour, current = [], start
    while True:
        tour.append(current)
        next_steps = [j for (i, j) in tour_edges if i == current]
        if not next_steps:
            break
        current = next_steps[0]
    return tour

robot_tours = [get_tour(depot) for depot in depots]
tour_costs = [
    sum(distances[robot_tours[i][k], robot_tours[i][k + 1]] for k in range(len(robot_tours[i]) - 1))
    for i in range(len(robot_tours))
]
overall_cost = sum(tour_costs)

# Output results
for i in range(len(robot_tours)):
    print(f"Robot {i} Tour: {robot_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")
print(f"Overall Total Travel Cost: {overall_cost}")