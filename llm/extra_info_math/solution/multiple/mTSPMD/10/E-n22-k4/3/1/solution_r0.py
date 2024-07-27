import pulp
import math

# Coordinates of the cities including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

n = len(coordinates)  # total number of nodes
depots = [0, 1, 2, 3]  # depots are the first four cities
nodes = list(range(n))  # list of all nodes
cities = list(set(nodes) - set(depots))  # non-depot cities

# Euclidean distance function
def euclidean_dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Distance matrix
distances = {(i, j): euclidean_dist(i, j) for i in nodes for j in nodes if i != j}

# Create the problem
problem = pulp.LpProblem("VRPMultipleDepots", pulp.LpMinimize)

# Decision variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for i in nodes for j in nodes for k in depots if i != j}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in nodes}

# Objective function
problem += pulp.lpSum(distances[i, j] * x[i, j, k] for i in nodes for j in nodes for k in depots if i != j)

# Constraints
# Each non-depot city is visited exactly once by exactly one robot
for j in cities:
    problem += pulp.lpSum(x[i, j, k] + x[j, i, k] for i in nodes for k in depots if i != j) == 1

# Flow conservation at each city for each robot
for k in depots:
    problem += pulp.lpSum(x[k, j, k] for j in nodes if j != k) == 1  # leave depot
    problem += pulp.lpSum(x[i, k, k] for i in nodes if i != k) == 1  # return to depot
    for i in nodes:
        problem += (pulp.lpSum(x[i, j, k] for j in nodes if j != i) == pulp.lpSum(x[j, i, k] for j in nodes if j != i))

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j:
            for k in depots:
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

# Output results
total_cost = 0
for k in depots:
    print(f"\nRobot {k} Tour starting at Depot {k}:")
    tour = [k]
    next_location = k
    while True:
        next_location = next(j for j in nodes if pulp.value(x[next_location, j, k]) == 1)
        tour.append(next_location)
        if next_location == k:
            break
    print(tour)
    cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    total_cost += cost
    print(f"Robot {k} Total Travel Cost: {cost}")

print(f"\nOverall Total Travel Cost: {total_cost}")