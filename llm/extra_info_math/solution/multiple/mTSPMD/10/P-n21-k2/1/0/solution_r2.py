from pulp import LpProblem, LpMinimize, lpSum, LpVariable
from math import sqrt

# Define the number of nodes and cities based on the coordinates
number_of_nodes = 21
depots = [0, 1]
robots = [0, 1]

# Define coordinates for the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(number_of_nodes)] for i in range(number_of_nodes)]

# Setting up the problem
problem = LpProblem("Vehicle_Routing_Problem", LpMinimize)

# Decision variables: x[i][j][k] where robot k travels from city i to city j
x = LpVariable.dicts("x", ((i, j, k) for i in range(number_of_nodes) for j in range(number_of_nodes) for k in robots), cat='Binary')

# Objective function: Minimize the total travel distance
problem += lpSum(distance_matrix[i][j] * x[i, j, k] for i in range(number_of_nodes) for j in range(number_of_nodes) for k in robots if i != j)

# Each robot starts and ends at their respective depot
for k in robots:
    problem += lpSum(x[depots[k], j, k] for j in range(number_of_nodes) if j != depots[k]) == 1
    problem += lpSum(x[j, depots[k], k] for j in range(number_of_nodes) if j != depots[k]) == 1

# Each city must be visited exactly once
for j in range(number_of_nodes):
    if j not in depots:
        problem += lpSum(x[i, j, k] for i in range(number_of_nodes) for k in robots if i != j) == 1
        problem += lpSum(x[j, i, k] for i in range(number_of_nodes) for k in robots if i != j) == 1

# Subtour elimination
for k in robots:
    u = LpVariable.dicts("u", (i for i in range(number_of_nodes)), lowBound=0, cat='Continuous')
    for i in range(number_of_nodes):
        for j in range(number_of_nodes):
            if i != j and i != depots[k] and j != depots[k]:
                problem += u[i] - u[j] + (number_of_nodes) * x[i, j, k] <= number_of_nodes - 1

# Solve problem
problem.solve()

# Output the results
routes = {k: [] for k in robots}
for k in robots:
    route = []
    next_city = depots[k]
    while True:
        route.append(next_city)
        next_step = [j for j in range(number_of_nodes) if x[next_city, j, k].varValue > 0.5]
        if not next_step:
            break
        next_city = next_step[0]
        if next_city == depots[k]:
            break
    route.append(depots[k])  # ensure tour returns to depot
    routes[k] = route

# Calculate travel costs
total_costs = {k: sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1)) for k, route in routes.items()}
total_cost = sum(total_costs.values())

# Print Results
for k in routes:
    print(f"Robot {k} Tour: {routes[k]}")
    print(f"Robot {k} Total Travel Cost: {total_costs[k]}")
print(f"Overall Total Travel Cost: {total_cost}")