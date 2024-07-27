import pulp
import math

# Coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate Euclidean distance between any two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

n = len(cities)
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), 1, n-1, cat='Integer')  # Node indices start from 1

# Objective function - minimize the maximum distance
max_edge = pulp.LpVariable("max_edge", lowBound=0)
prob += max_edge

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Subtour prevention + max edge restriction
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= max_edge

# Solve the problem
status = prob.solve()

# Extract tour
path = []
for v in prob.variables():
    if v.varValue == 1 and v.name.startswith('x'):
        i, j = map(int, v.name[2:-1].split(',_'))
        path.append((i, j))

# Create ordered tour
tour = [0]
while len(tour) < n:
    last = tour[-1]
    for (i, j) in path:
        if i == last:
            tour.append(j)
            break

max_distance = 0
total_travel_cost = 0

for k in range(1, len(tour)):
    d = distance(tour[k-1], tour[k])
    total_travel_cost += d
    if d > max_distance:
        max_distance = d

# Create complete cycle back to the start
tour.append(0)
total_travel_cost += distance(tour[-2], tour[0])

# Display results
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_travel_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")