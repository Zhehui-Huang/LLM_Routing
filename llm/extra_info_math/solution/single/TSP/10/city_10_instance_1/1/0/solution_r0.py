import pulp
import math

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
c = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

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
for S in range(3, n):
    for subtour in itertools.combinations(range(1, n), S):
        problem += pulp.lpSum(x[i, j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Solve the problem
problem.solve()

# Create the tour based on the variables that are set to 1
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Sort the tour to start and end at depot city 0
sorted_tour = []
current_city = 0
while len(sorted_tour) < n:
    for i, j in tour:
        if i == current_city:
            sorted_tour.append(i)
            current_city = j
            break
sorted_tour.append(0)  # Append the return to the depot

# Calculate the total cost
total_cost = sum(c[sorted_tour[i]][sorted_tour[i + 1]] for i in range(len(sorted_tour) - 1))

print(f"Tour: {sorted_tour}")
print(f"Total travel cost: {total_cost:.2f}")