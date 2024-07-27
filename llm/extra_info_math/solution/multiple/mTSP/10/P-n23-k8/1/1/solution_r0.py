import pulp
import math

# Coordinates of the cities including the depot city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

n = len(coordinates)  # Number of nodes including depot
m = 8  # Number of salesmen (robots)

# Function to calculate Euclidean distance between two cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Creating a distance matrix
c = {(i, j): calculate_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Initialize the problem
prob = pulp.LpProblem("Multiple_Salesmen_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n), range(m)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(n), 0, None, pulp.LpContinuous)

# Objective function
prob += pulp.lpSum(c[i, j] * x[i][j][k] for i in range(n) for j in range(n) for k in range(m)), "Total Travel Cost"

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += pulp.lpSum(x[i][j][k] for i in range(n) for k in range(m)) == 1

# Flow conservation constraints
for k in range(m):
    for p in range(1, n):
        prob += pulp.lpSum(x[i][p][k] for i in range(n)) - pulp.lpSum(x[p][j][k] for j in range(n)) == 0

# Each salesman leaves the depot
for k in range(m):
    prob += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i][j][k] <= n - 1

# Solve the problem
prob.solve()

# Output tours and total costs
overall_total_cost = 0
for k in range(m):
    tour = [0]
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                tour.append(j)
                if j == 0:
                    break
    travel_cost = sum(c[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    overall_total_cost += travel_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Ixost: {travel_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")