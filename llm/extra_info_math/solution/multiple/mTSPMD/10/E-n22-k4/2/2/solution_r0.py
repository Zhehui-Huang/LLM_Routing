import pulp
import math

# Define the coordinates of cities and depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

n = len(coordinates)
depots = [0, 1, 2, 3]
robots = 4

# Calculate distance matrix
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = [
    [euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)
]

# Formulate the problem
problem = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Variables: x[i][j][k]: Robot k travels from i to j
x = [[[pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')
      for k in range(robots)] for j in range(n)] for i in range(n)]

# Objective Function: Minimize the sum of all distances traveled
problem += pulp.lpSum(distance_matrix[i][j] * x[i][j][k]
                       for k in range(robots) for j in range(n) for i in range(n))

# Constraints
# Each robot starts and ends at its depot
for k in range(robots):
    problem += pulp.lpSum(x[depots[k]][j][k] for j in range(n) if j != depots[k]) == 1
    problem += pulp.lpSum(x[j][depots[k]][k] for j in range(n) if j != depots[k]) == 1

# Each city is visited exactly once
for j in range(4, n):  # Exclude depots
    problem += pulp.lpSum(x[i][j][k] for k in range(robots) for i in range(n)) == 1

# Subtour elimination
for k in range(robots):
    for i in range(n):
        for j in range(n):
            if i != j:
                problem += pulp.lpSum(x[i][j][k] for k in range(robots)) <= 1

# Solve the problem
problem.solve()

# Extract solution
tours = [[] for _ in range(robots)]
for k in range(robots):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i][j][k]) == 1:
                tours[k].append((i, j))

# Calculate and print tours and costs
overall_cost = 0
for k in range(robots):
    print(f"Robot {k} Tour: [", end="")
    current_city = depots[k]
    tour_cost = 0
    first_pass = True
    while True:
        for j in range(n):
            if pulp.value(x[current_city][j][k]) == 1:
                if not first_pass:
                    print(" -> ", end="")
                print(j, end="")
                tour_cost += distance_matrix[current_city][j]
                current_city = j
                break
        if current_city == depots[k]:
            break
        first_pass = False
    print("]")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")