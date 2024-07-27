import math
import pulp as lp

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of cities and salesmen (robots)
n, m = len(coordinates), 4

# Euclidean distance calculator
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
distance_matrix = [[calc_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem setup
problem = lp.LpProblem("VRP", lp.LpMinimize)

# Variables
x = lp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), 0, 1, lp.LpBinary)
u = lp.LpVariable.dicts("u", (i for i in range(1, n)), 0, n-1)

# Objective
problem += lp.lpSum(distance_matrix[i][j] * x[(i, j, k)] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints
# Every city must be visited exactly once by exactly one salesman
for j in range(1, n):
    problem += lp.lpSum(x[(i, j, k)] for i in range(n) if i != j for k in range(m)) == 1

# Flow conservation constraints
for k in range(m):
    for j in range(n):
        problem += lp.lpSum(x[(i, j, k)] for i in range(n) if i != j) - lp.lpSum(x[(j, i, k)] for i in range(n) if i != j) == 0

# Salesman leaves and returns to the depot
for k in range(m):
    problem += lp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    problem += lp.lpSum(x[(j, 0, k)] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] <= (n-1) * (1 - x[(i, j, k)]) - 1

# Solve the problem
problem.solve()

# Output the results
overall_cost = 0
for k in range(m):
    tour = [0]
    current_location = 0
    while True:
        found_next = False
        for j in range(n):
            if j != current_location and lp.value(x[(current_location, j, k)]) == 1:
                tour.append(j)
                overall_cost += distance_matrix[current_location][j]
                current_location = j
                found_next = True
                break
        if not found_next:
            break
    tour.append(0)  # Return to depot
    tour_cost = sum(distance_entry[(j, k)] for j, k in zip(tour[:-1], tour[1:]) if k != 0)
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")