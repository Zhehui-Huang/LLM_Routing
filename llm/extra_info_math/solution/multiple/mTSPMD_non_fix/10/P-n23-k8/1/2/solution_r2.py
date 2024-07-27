from math import sqrt
from mip import Model, xsum, minimize, BINARY

# Define cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

n = len(cities)

# Calculating the Euclidean distance
def euclidean_distance(p1, p2):
    return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

dist = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

m = 8  # number of robots
depot = 0

model = Model()

# Variables
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var(var_type=BINARY) for i in range(n)]  # for subtour elimination

# Objective
model.objective = minimize(xsum(dist[i][j] * x[i][j] for i in range(n) for j in range(n)))

# Constraints
# flow conservation
for j in range(1, n):
    model += xsum(x[i][j] for i in range(n)) == 1
    model += xsum(x[j][i] for i in range(n)) == 1

# exactly m tours starting from depot
model += xsum(x[depot][j] for j in range(n) if j != depot) == m

# eliminate subtours
for j in range(1, n):
    model += u[j] >= 2
    model += u[j] <= n
    for i in range(1, n):
        model += u[i] - u[j] + (n + 1) * x[i][j] <= n

# solve
status = model.optimize(max_seconds=300)

if status == OptimizationStatus.OPTIMAL or status == OptimizationStatus.FEASIBLE:
    print('Solution found.')
    routes = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                routes[i].append(j)

    # Extract tours from solution
    for start in routes:
        if start == depot:
            for end in routes[start]:
                if x[start][end].x >= 0.99:
                    print(f"Robot starting from depot {depot} tours:")
                    current = end
                    tour = [start]
                    total_cost = 0
                    while True:
                        tour.append(current)
                        next_step = next((k for k in routes[current] if x[current][k].x >= 0.99), None)
                        if next_step is None or next_step == start:
                            total_cost += dist[current][start]
                            print(f'Tour: {tour + [start]} with cost {total_cost}')
                            break
                        total_cost += dist[current][next_step]
                        current = next_step

else:
    print("No feasible solution found.")