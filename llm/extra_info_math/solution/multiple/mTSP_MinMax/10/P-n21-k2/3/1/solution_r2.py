import pulp
import math

# Coordinates of each city including the depot city 0
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Parameters
n = len(coordinates)  # Number of nodes, including the depot
m = 2  # Number of robots

# Calculate Euclidean distance between all pairs of points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

cost = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
model = pulp.LpProblem("Robot_Tours", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", (range(1, n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective: Minimize the maximum travel cost among all robots
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')
model += max_distance

# Assignment constraints: each city is visited exactly once by one robot
for j in range(1, n):
    model += sum(x[(i, j, k)] for k in range(m) for i in range(n) if i != j) == 1

# Each robot starts and ends at the depot
for k in range(m):
    model += sum(x[(0, j, k)] for j in range(1, n)) == 1
    model += sum(x[(j, 0, k)] for j in range(1, n)) == 1

# Constraints to ensure that each robot leaves every city it enters
for k in range(m):
    for j in range(1, n):
        model += sum(x[(i, j, k)] for i in range(n) if i != j) == sum(x[(j, i, k)] for i in range(n) if i != j)

# Subtour elimination: prevent loops within the solutions
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i] - u[j] + (n-1) * x[(i, j, k)] <= n-2

# To keep under max_distance for any robot
for k in range(m):
    model += sum(cost[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the model
model.solve()

# Check if a valid solution has been found
if model.status == pulp.LpStatusOptimal:
    print("Optimal solution found with total minimal maximum distance:", pulp.value(max_distance))
    for k in range(m):
        print(f"\nRobot {k} Route:")
        route = []
        for i in range(n):
            for j in range(n):
                if i != j and pulp.value(x[(i, j, k)]) == 1:
                    route.append((i, j))
                    print(f"From {i} to {j}")
    travel_costs = {k: sum(cost[i, j] * pulp.value(x[i, j, k]) for i in range(n) for j in range(n) if i != j) for k in range(m)}
    for k in travel_costs:
        print(f"Robot {k} Travel Cost: {travel_costs[k]}")
else:
    print("No optimal solution is available.")