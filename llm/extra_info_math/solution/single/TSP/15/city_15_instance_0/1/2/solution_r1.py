import pulp
import math
import itertools

# Define the cities' coordinates
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Number of cities including the depot
num_cities = len(coordinates)

# Calculate Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Cost matrix
cost_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Setting up the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat='Binary')

# Objective function
problem += pulp.lpSum(cost_matrix[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints: Ensure each city is arrived at and left exactly once
for i in range(num_cities):
    problem += pulp.lpSum(x[i, j] for j in range(num_cities) if i != j) == 1, f"Leave_city_{i}"
    problem += pulp.lpSum(x[j, i] for j in range(num_cities) if i != j) == 1, f"Enter_city_{i}"

# Subtour elimination constraints
for n in range(2, num_cities):
    for S in itertools.combinations(range(1, num_cities), n):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve()

# Result extraction
tour = [0]  # start from depot city (index 0)
for _ in range(num_cities - 1):
    current = tour[-1]
    next_city = [j for j in range(num_cities) if j != current and pulp.value(x[current, j]) == 1][0]
    tour.append(next_city)

# Close the tour by returning to the depot
tour.append(0)

# Calculate total travel cost
total_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)