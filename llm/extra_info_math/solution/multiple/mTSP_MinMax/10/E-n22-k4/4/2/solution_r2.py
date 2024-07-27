import pulp
import math

# Define coordinates of each city including the depot
coordinates = [
    (145, 215), # Depot
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217),
    (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), (164, 193),
    (129, 189), (155, 185), (139, 182)
]

# Calculate Euclidean distances between cities
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Variables
n = len(coordinates)
m = 4  # Number of robots

# Create the problem
model = pulp.LpProblem("MVRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n), range(m)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(n), 1, n-1, cat='Continuous')

# Objective: Minimize the maximum distance traveled by any robot
z = pulp.LpVariable("z", lowBound=0)
model += z, "MaximizeTravelCost"

# Constraints
# Each city is visited exactly once by a robot
for j in range(1, n):
    model += sum(x[i][j][k] for i in range(n) if i != j for k in range(m)) == 1

# Robots start and end at the depot (city 0)
for k in range(m):
    model += pulp.lpSum(x[0][j][k] for j in range(1, n)) == 1
    model += pulp.lpSum(x[j][0][k] for j in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for v in range(1, n):
        model += (pulp.lpSum(x[i][v][k] for i in range(n) if i != v) - 
                  pulp.lpSum(x[v][j][k] for j in range(n) if j != v)) == 0

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + (n) * x[i][j][k] <= n - 1

# Z should be greater than the distance travelled by each robot
for k in range(m):
    model += pulp.lpSum(x[i][j][k] * distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j) <= z

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Output results
if status == pulp.LpStatusOptimal:
    for k in range(m):
        tour = []
        current_location = 0
        tour_cost = 0
        while True:
            next_location = None
            for j in range(n):
                if pulp.value(x[current_location][j][k]) == 1:
                    next_location = j
                    break
            if next_location is None or next_location == 0:
                break
            tour.append(next_location)
            current_location = next_location
        tour = [0] + tour + [0]
        cost = sum(distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {cost}")
    max_cost = pulp.value(z)
    print(f"Maximum Travel Cost: {max_cost}")
else:
    print("An optimal solution was not found.")