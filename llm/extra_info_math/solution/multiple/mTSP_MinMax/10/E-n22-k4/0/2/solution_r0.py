import pulp
import math

# Coordinates of the depot and cities (index corresponds to city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of cities (including depot)
n = len(coordinates)
# Number of robots
m = 4
# All nodes including depot
all_nodes = list(range(n))
# Nodes without the depot
cities = list(range(1, n))

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
cost = {(i, j): distance(coordinates[i], coordinates[j]) for i in all_nodes for j in all_nodes if i != j}

# Setup the problem
prob = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (all_nodes, all_nodes, range(m)), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (all_nodes), lowBound=0, cat=pulp.LpContinuous)

# Objective
max_distance = pulp.LpVariable("max_distance")
prob += max_distance

# Constraints
# Each city is visited exactly once by one robot
for j in cities:
    prob += pulp.lpSum(x[i][j][k] for i in all_insnodes for k in range(m) if i != j) == 1

# Flow conservation constraints
for k in range(m):
    for j in all_nodes:
        prob += pulp.lpSum(x[i][j][k] for i in all_nodes if i != j) - pulp.lpSum(x[j][i][k] for i in all_nodes if i != j) == 0

# Each robot must leave the depot exactly once and return
for k in range(m):
    prob += pulp.lpSum(x[0][j][k] for j in cities) == 1
    prob += pulp.lpSum(x[j][0][k] for j in cities) == 1

# Subtour elimination constraints
for i in cities:
    for j in cities:
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i][j][k] <= n - 1

# Max distance constraint
for k in range(m):
    prob += pulp.lpSum(x[i][j][k] * cost[i, j] for i in all_nodes for j in all_nodes if i != j) <= max_distance

# Solve the problem
prob.solve()

# Output results
for k in range(m):
    tour = [0]
    next_city = 0
    while True:
        next_city = next(j for j in all_nodes if pulp.value(x[next_city][j][k]) == 1)
        if next_city == 0:
            break
        tour.append(next_city)
    tour.append(0)
    tour_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {pulp.value(max_distance)}")