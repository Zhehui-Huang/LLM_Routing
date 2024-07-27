import pulp
import math

# Define the coordinates of the cities including the depot city
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Problem size
n = len(coordinates)

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat=pulp.LpInteger)

# Objective
problem += pulp.lpSum(x[i, j] * euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # each city must be left exactly once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # each city must be entered exactly once

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
problem.solve()

# Retrieve solution
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Simplify tour into readable format
sorted_tour = [0]
for _, next_city in sorted(tour, key=lambda x: x[0]):
    sorted_tour.append(next_city)

# Ensure tour ends at the depot
sorted_tour.append(0)

# Calculate the total travel cost
total_distance = sum(euclidean_distance(coordinates[sorted_tour[i]], coordinates[sorted_tour[i+1]]) for i in range(len(sorted_tour)-1))

# Output results
print("Tour:", sorted_tour)
print("Total travel cost:", total_distance)