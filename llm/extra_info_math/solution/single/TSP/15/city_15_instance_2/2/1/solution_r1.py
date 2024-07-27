import pulp
import math
import itertools

# Coordinates of each city, including depot (city 0)
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Number of cities (including the depot)
n = len(coordinates)

# Calculate the Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cost matrix
c = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for j in range(n)] for i in range(n)]

# Objective function
problem += pulp.lpSum(c[i][j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1  # Each city is left exactly once
    problem += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1  # Each city is entered exactly once

# Subtour elimination constraints
for s in range(2, n):
    subsets = itertools.combinations(range(1, n), s)
    for subset in subsets:
        problem += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve()

# Extract the tour from the solution
tour = []
next_city = 0
while True:
    tour.append(next_city)
    next_cities = [j for j in range(n) if pulp.value(x[next_city][j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city == 0:
        break

# Adding the depot city to complete the tour
tour.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")