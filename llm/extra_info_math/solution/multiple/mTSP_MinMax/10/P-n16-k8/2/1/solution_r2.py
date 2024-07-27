from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, LpContinuous, PULP_CBC_CMD
import math

# Define the coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Function to calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Number of nodes and robots
n = len(coordinates)
m = 8  # Number of robots
robot_ids = range(m)

# Create a matrix for the costs between each pair of nodes
costs = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = LpProblem("Minimal_Max_Distance_Multiple_Robots_TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in robot_ids if i != j), cat=LpBinary)
u = LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat=LpContinuous)
max_distance = LpVariable("max_distance", lowBound=0)

# Objective: minimize the maximum distance travelled by any robot
problem += max_distance

# Subject to
# Each non-depot city must be visited exactly once
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) if i != j for k in robot_ids) == 1

# Each robot must leave the depot exactly once and return exactly once
for k in robot_ids:
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Flow conservation for each robot at each city
for k in robot_ids:
    for j in range(1, n):
        problem += lpSum(x[i, j, k] for i in range(n) if i != j) - lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n) * lpSum(x[i, j, k] for k in robot_ids) <= n - 1

# Maximum distance constraint
for k in robot_ids:
    problem += lpSum(costs[i][j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem using CBC solver
problem.solve(PULP_CBC_CMD(msg=1))

if problem.status == 1:
    print("Optimal solution found!")

    # Extract tour information
    for k in robot_ids:
        print(f"Tour for Robot {k}:")
        tour = []
        next_city = 0
        while True:
            next_cities = [j for j in range(n) if value(x[next_city, j, k]) == 1]
            if not next_cities:
                break
            next_city = next_cities[0]
            tour.append(next_city)
            if next_city == 0:
                break
        print(" -> ".join(map(str, tour)))

    print(f"Maximum distance traveled: {value(max_distance)}")
else:
    print("Solution not found, or infeasible.")