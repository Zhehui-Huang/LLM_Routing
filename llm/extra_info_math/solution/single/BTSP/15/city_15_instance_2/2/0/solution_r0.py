import pulp
import math

# City coordinates
coordinates = [
    (54, 87),  # Depot City 0
    (21, 84),  # City 1
    (69, 84),  # City 2
    (53, 40),  # City 3
    (54, 42),  # City 4
    (36, 30),  # City 5
    (52, 82),  # City 6
    (93, 44),  # City 7
    (21, 78),  # City 8
    (68, 14),  # City 9
    (51, 28),  # City 10
    (44, 79),  # City 11
    (56, 58),  # City 12
    (72, 43),  # City 13
    (6, 99)    # City 14
]

n = len(coordinates)

# Calculating distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
                     (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d = pulp.LpVariable("max_distance", cat='Continuous')

# Objective
problem += d

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += d >= distance(i, j) * x[i, j]

# Subtour elimination (using MTZ constraints)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
problem.solve()

# Extract the tour
tour = []
visited = [0]
current = 0
while True:
    next_city = [j for j in range(n) if pulp.value(x[current, j]) == 1]
    if not next +=city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    visited.append(next_city)
    current = next_city
    if current == 0:
        break

max_distance = pulp.value(d)
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

output = {
    "Tour": [0] + tour + [0],
    "Total travel cost": total_distance,
    "Maximum distance between consecutive cities": max_distance
}

output