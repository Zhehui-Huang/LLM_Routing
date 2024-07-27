import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpStatus, value

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(coordinates)  # number of nodes including depot
m = 2  # number of robots

# Calculate distances
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Setting up the problem
problem = LpProblem("Multiple Traveling Salesman Problem", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary')
u = LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Continuous')

# Objective function
problem += lpSum(distances[i][j] * x[i, j, k] for k in range(m) for i in range(n) for j in range(n))

# Constraints
# Each city is visited exactly once by one salesman and return to the depot
for j in range(1, n):
    problem += lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1

for k in range(m):
    problem += lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Conservation of flow
for k in range(m):
    for j in range(1, n):
        problem += lpSum(x[i, j, k] for i in range(n) if i != j) - \
                   lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Subtour prevention (MTZ constraints)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
problem.solve()

if LpStatus[problem.status] == "Optimal":
    # Results by robot
    max_cost = 0
    for k in range(m):
        tour = []
        current_pos = 0
        for _ in range(n):
            next_city = [j for j in range(n) if value(x[current_pos, j, k]) == 1]
            if not next_city:
                break
            next_city = next_city[0]
            tour.append(next_city)
            current_pos = next_city
        if tour:
            tour = [0] + tour + [0]  # start and end at depot
            tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            max_cost = max(max_cost, tour_cost)
            print(f"Robot {k} Tour: {tour}")
            print(f"Robot {k} Total Travel Cost: {tour_cost}")

    # Maximum cost among all tours
    print(f"Maximum Travel Cost: {max_cost}")
else:
    print("No optimal solution found.")