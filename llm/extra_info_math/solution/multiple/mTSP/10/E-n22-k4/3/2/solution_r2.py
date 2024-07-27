import pulp
import math

# Coordinates of the cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

n = len(coordinates)  # including depot
cities_idx = range(1, n)
m = 4  # Number of robots

# Euclidean distance calculation
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Create the optimization problem
problem = pulp.LpProblem("VRP_with_Multiple_Robots", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)),
                          cat='Binary')

u = pulp.LpVariable.dicts("u", (i for i in cities_idx), lowBound=0, upBound=n, cat='Continuous')

# Objective
problem += pulp.lpSum(euclidean_distance(i, j) * x[i, j, k] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Each city is visited exactly once by one robot
for j in cities_idx:
    problem += sum(x[i, j, k] for k in range(m) for i in range(n) if i != j) == 1

# Robots leave the depot and return to it once
for k in range(m):
    problem += sum(x[0, j, k] for j in cities_idx) == 1
    problem += sum(x[j, 0, k] for j in cities_idx) == 1

# Ensure flow of robots from one city to next
for k in range(m):
    for j in cities_idx:
        problem += sum(x[i, j, k] for i in range(n) if i != j) == sum(x[j, i, k] for i in range(n) if i != j)

# Sub-tour elimination constraint
for k in range(m):
    for i in cities_idx:
        for j in cities_in
            problem += (u[i] - u[j] + n*x[i, j, k] <= n-1)

# Solve the problem
problem.solve()

# Output solution
total_cost = 0
for k in range(m):
    tour = [0]
    last = 0
    while True:
        next_city = None
        for j in range(n):
            if j != last and pulp.value(x[last, j, k]) == 1:
                next_city = j
                tour.append(next_city)
                total_cost += euclidean_distance(last, next_city)
                last = next_city
                break
        if next_city == 0:
            break
    print(f'Robot {k} Tour: {tour}')
    print(f'Robot {k} Total Travel Cost: {sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))}')

print(f'Overall Total Travel Cost: {total_cost}')