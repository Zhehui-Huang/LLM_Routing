import pulp
import math
import itertools

# Define the cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Number of cities
n = len(cities)

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix
c = [[euclidean: Distance)istance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective Function
problem += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour elimination constraints
for S in range(2, n):
    for subtour in itertools.combinations(range(n), S):
        if len(subtour) > 1:
            problem += pulp.lpSum(x[i, j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Solve the problem
problem.solve()

# Extract the tour
tour = [0]
current_city = 0
next_city = None
for _ in range(n):
    for j in range(n):
        if current_city != j and pulp.value(x[current_city, j]) == 1:
            tour.append(j)
            current_city = j
            break
tour.append(0)  # Return to the depot

# Calculate total travel cost of the tour
total_cost = sum(c[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")