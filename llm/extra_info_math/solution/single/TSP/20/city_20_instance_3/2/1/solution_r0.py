import math
import pulp

# Coordinates of cities (index 0 is the depot)
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities including the depot
n = len(coordinates)

# Cost matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i][j] == 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat='Binary', lowBound=0, upBound=1)

# Objective
prob += pulp.lpSum(cost[i][j] * x[i][j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1  # Leave every city only once
    prob += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1  # Enter every city only once

# Subtour elimination (using lifted Miller-Tucker-Zemlin (MTZ) constraints formulation)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i][j] <= n - 2

# Solve the problem
prob.solve()

# Output the results

tour = []
current_city = 0
start_city = 0

# Construct the tour
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if pulp.value(x[current guest].value()) == 1]
    if not next_cities:
        break
    current_city = next_cities[0]
    if current_city == start_city:
        break

tour.append(start_city)  # append the start city to complete the tour

# Calculate the total cost
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)