import pulp
import math

# Coordinates of cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

n = len(coordinates)  # Number of nodes (cities + depot)
m = 4  # Number of robots

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
cost = [[euclidean_index_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the LP problem
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat="Binary")
u = pulp.LpVariable.dicts("u", (i for i in range(n)), cat="Continuous")

# Objective
problem += pulp.lpSum(cost[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[(i, 0, k)] for i in range(1, n)) == 1

for k in range(m):
    for p in range(1, n):
        problem += pulp.lpSum(x[(i, p, k)] for i in range(n) if i != p) - pulp.lpSum(x[(p, j, k)] for j in range(n) if j != p) == 0

for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - 1) * x[(i, j, k)] <= n - 2

# Solve the problem
problem.solve()

# Output results
overall_cost = 0
for k in range(m):
    tour = [0]  # Start at depot
    current_city = 0
    tour_cost = 0
    while True:
        next_city = None
        for j in range(n):
            if j != current_city and pulp.value(x[(current_city, j, k)]) == 1:
                next_city = j
                break
        if next_city is None or next_city == 0:
            tour.append(0)
            tour_cost += cost[current_city][0]
            break
        tour.append(next_city)
        tour_cost += cost[current_city][next_city]
        current_city = next_city

    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")