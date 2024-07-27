import pulp
import math

# City coordinates (including depot as city 0)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(coordinates)  # number of nodes including the depot
m = 2  # number of robots

# Calculate distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

cost = [[distance(i, j) for j in range(n)] for i in range(n)]

# Initialize the model
model = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat=pulp.LpContinuous)

# Objective function
model += pulp.lpSum(cost[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m))

# Constraints
for i in range(1, n):
    model += sum(x[i, j, k] for k in range(m) for j in range(n) if i != j) == 1

for k in range(m):
    model += sum(x[0, j, k] for j in range(1, n)) == 1
    model += sum(x[j, 0, k] for j in range(1, n)) == 1
    for i in range(1, n):
        model += sum(x[i, j, k] for j in range(n) if i != j) - sum(x[j, i, k] for j in range(n) if i != j) == 0

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + (n * x[i, j, k] <= n - 1)

# Solve the model
model.solve()

# Retrieve results
overall_cost = 0
for k in range(m):
    current_location = 0
    tour = [current_location]
    tour_cost = 0
    while True:
        choices = [j for j in range(n) if x[(current_location, j, k)].varValue == 1]
        if not choices:
            break
        next_location = choices[0]
        tour.append(next_location)
        tour_cost += cost[current_location][next_location]
        current_location = next_location
    tour.append(0)  # return to depot
    tour_cost += cost[current_location][0]
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tourfrac.], rotatelock.arrayosta}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")