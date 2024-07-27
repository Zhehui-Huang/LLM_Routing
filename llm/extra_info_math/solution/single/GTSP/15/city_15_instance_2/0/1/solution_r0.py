import pulp
from math import sqrt

# Define data
depot = (54, 87)
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Calculate distances
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

distances = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Initialize the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function
prob += pulp.lpSum([distances[i, j] * x[i, j] for i in cities for j in cities if i != j])

# Constraints
# Each group except the depot must have exactly one outgoing and one incoming connection
for group in city_groups:
    prob += pulp.lpSum([x[i, j] for i in group for j in cities if j not in group]) == 1
    prob += pulp.lpSum([x[j, i] for i in group for j in cities if j not in group]) == 1

# Flow conservation at nodes
for k in cities:
    prob += pulp.lpSum([x[i, k] for i in cities if i != k]) == pulp.lpSum([x[k, i] for i in cities if i != k])

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", range(1, len(cities)), lowBound=0, cat='Continuous')
for i in range(1, len(cities)):
    for j in range(1, len(cities)):
        if i != j:
            prob += u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1

# Solve the problem
prob.solve()

# Parse the result
tour = [0]
cost = 0
visited = [0]

while len(visited) < len(cities):
    for k in cities:
        if k not in visited and pulp.value(x[tour[-1], k]) == 1:
            tour.append(k)
            visited.append(k)
            cost += distances[tour[-1], k]
            break
tour.append(0)
cost += distances[tour[-2], 0]

# Output
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))