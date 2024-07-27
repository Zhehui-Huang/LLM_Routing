import pulp
import math

# Define the coordinates of the cities
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Define the Euclidean distance function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create the distance matrix
n = len(cities)
dist_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            dist_matrix[i, j] = euclidean_connection(cities[i], cities[j])

# Setting up the PuLP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path leads directly from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum(dist_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city must be left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Each city must be entered exactly once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1
    
# Subtour prevention (Miller-Tucker-Zemlin formulation could be included for large problems)

# Solve the problem
problem.solve()

# Retrieve results
tour = [-1] * n
total_cost = 0
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour[i] = j
            total_cost += dist_matrix[i, j]

# Convert tour to human-readable form starting from depot city "0"
tour_readable = [0]
while len(tour_readable) < n:
    next_city = tour[tour_readable[-1]]
    if next_city != 0:
        tour_readable.append(next_city)
    else:
        break
tour_readable.append(0)  # Return to depot

print(f"Tour: {tour_readable}")
print(f"Total travel cost: {total_cost:.2f}")