import pulp
import math

# Define the cities and their coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

n = len(coordinates)
m = 2

problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

max_distance = pulp.LpVariable("max_distance")
problem += max_distance

for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

for k in range(m):
    for p in range(1, n):
        problem += pulp.lpSum(x[p, j, k] for j in range(n) if p != j) == pulp.lpSum(x[i, p, k] for i in range(n) if i != p)

for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

for k in range(m):
    for i in range(n):
        for j in range(n):
            if i != j:
                problem += distance(i, j) * x[i, j, k] <= max_distance

status = problem.solve()

tours = []
costs = []
for k in range(m):
    tour = [0]
    next_city = 0
    cost = 0
    while True:
        next_city = next((j for j in range(n) if pulp.value(x[next_city, j, k]) == 1), None)
        if next_city == 0:
            tour.append(0)
            break
        tour.append(next_city)
        cost += distance(tour[-2], next_city)
    tours.append(tour)
    costs.append(cost)

for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

max_cost = max(costs)
print(f"Maximum Travel Cost: {max_cost}")