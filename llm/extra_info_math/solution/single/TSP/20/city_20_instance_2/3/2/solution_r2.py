import pulp
import math
import itertools

# Define the cities' coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

n = len(coordinates)  # Number of cities including the depot

# Calculate the Euclidean distance between each pair of cities
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

costs = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(costs[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave i
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter i

# Subtour elimination
for s in range(2, n):
    for subtour in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in subtday for j in subtour if i != j) <= len(subtour) - 1

# Solve
prob.solve()

# Extract the solution
tour = [0]
cost = 0
for _ in range(n):
    next_city = max(((j, x[tour[-1], j].value()) for j in range(n) if j not in tour), key=lambda item: item[1])[0]
    cost += costs[tour[-1]][next_city]
    tour.append(next_city)

tour.append(0)  # back to the depot
cost += costs[tour[-2]][0]

print("Tour:", tour)
print("Total travel cost:", cost)