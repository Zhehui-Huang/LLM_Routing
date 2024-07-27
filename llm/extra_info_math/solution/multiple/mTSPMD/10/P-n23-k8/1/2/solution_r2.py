import math
import pulp

# Input Data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
depots = list(range(8))
num_robots = len(depots)

# Distance matrix calculation
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

num_cities = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Optimization model
model = LpProblem("MDVRP", LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), depots), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat='Continuous')

# Objective function
model += pulp.lpSum(distance_matrix[i][j] * x[i][j][k] for i, j, k in product(range(num_cities), repeat=2, depots))

# Constraints
for k in depots:
    model += pulp.lpSum(x[k][j][k] for j in range(num_cities) if j != k) == 1  # One departure from each depot

for k in depots:
    model += pulp.lpSum(x[j][k][k] for j in range(num_cities) if j != k) == 1  # One arrival to each depot

for j in range(num_cities):
    if j not in depots:
        model += pulp.lpSum(x[i][j][k] for i in range(num_cities) for k in depots) == 1  # Each city is visited exactly once

for i in range(num_cities):
    for k in depots:
        if i != k:
            model += pulp.lpSum(x[i][j][k] for j in range(num_cities) if j != i) == \
                     pulp.lpSum(x[j][i][k] for j in range(num_cities) if j != i)  # Flow conservation

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in depots:
                model += u[i] - u[j] + (num_cities - 1) * x[i][j][k] <= num_cities - 2

# Solve the problem
model.solve()

# Extract the tours and travel costs
tours = [[] for k in depots]
costs = [0 for k in depots]

for k in depots:
    next_city = k
    initial = k
    while True:
        for j in range(num_cities):
            if pulp.value(x[next_city][j][k]) == 1:
                next_city = j
                costs[k] += distance_matrix[next_city][j]
                tours[k].append(next_city)
                break
        if next_city == initial:
            break

# Output the results
for k in depots:
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")

print("Overall Total Travel Cost:", sum(costs))