import math
import pulp

# Coordinates of the cities indexed by city number
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# City groups
city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Prepare the problem to minimize
problem = pulp.LpProblem('MinimizeTravelCost', pulp.LpMinimize)

# Variables: x[(i, j)] = 1 if route i to j is chosen
x = {}
n = len(coordinates)
for i in range(n):
    for j in range(n):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)

# Objective: Minimize the total distance traveled
objective = pulp.lpSum(distance(coordinates[i], coordinates[j]) * x[(i, j)]
                       for i in range(n) for j in range(n) if i != j)
problem += objective

# Constraint: Enter each city group exactly once
for group in city_groups:
    problem += sum(x[(i, j)] for i in group for j in range(n) if i != j) == 1

# Constraint: Leave each city group exactly once
for group in city_groups:
    problem += sum(x[(j, i)] for i in group for j in range(n) if i != j) == 1

# Constraint: From each non-depot city exactly one departure
for i in range(1, n):
    problem += sum(x[(i, j)] for j in range(n) if i != j) == 1

# Constraint: To each non-depot city exactly one arrival
for j in range(1, n):
    problem += sum(x[(i, j)] for i in range(n) if i != j) == 1

# Solve the model
problem.solve()

# Calculate the result path and total cost
path = [0]
current_city = 0
total_cost = 0
for _ in range(len(coordinates)-1):
    for next_city in range(n):
        if current_city != next_city and pulp.value(x[(current_city, next_city)]) == 1:
            path.append(next_city)
            total_cost += distance(coordinates[current_city], coordinates[next_city])
            current_city = next_city
            break

# Returning to the depot
if current_city != 0:
    path.append(0)
    total_cost += distance(coordinates[current_city], coordinates[0])

# Output the results
print("Tour:", path)
print("Total travel cost:", total_delta cost)