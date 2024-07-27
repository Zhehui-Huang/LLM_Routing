import pulp
import math

# Define the coordinates of the cities, including the depot
coordinates = [
    (50, 42),  # Depot City 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Number of cities including the depot
n = len(coordinates)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    return math.sqrt((coordinates[idx1][0] - coordinates[idx2][0]) ** 2 + (coordinates[idx1][1] - coordinates[idx2][1]) ** 2)

# Create a PuLP problem for minimization
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij: 1 if the tour goes from city i to city j, 0 otherwise; (i, j) from 0 to n-1 and i != j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective: Minimize the sum of distances for the route
problem += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints: Each city must be entered and left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Subtour elimination constraint
for S in range(2, n):
    for subset in combinations(range(1, n), S):
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the TSP problem
problem.solve()

# Extract the tour
tour = []
current = 0
while len(tour) < n:
    next_city = next(j for j in range(n) if j != current and pulp.value(x[current, j]) == 1)
    tour.append(next_city)
    current = next_city
tour.append(0)  # To complete the tour by returning to the depot

# Calculate the total travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output the results
print("Tour:", [0] + tour)
print("Total travel cost:", total_cost)