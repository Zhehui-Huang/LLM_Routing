import pulp
from math import sqrt

# City coordinates
coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities
n = len(coords)

# Distance matrix
dist_matrix = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Create problem
prob = pulp.LpProblem("Minimize_Maximum_Edge_Length_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0)

# Objective
prob += z, "Max_edge_length"

# Constraint to minimize the max edge used in the tour
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * dist_matrix[i][j] <= z

# Each city must be entered and left once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"exit_from_{i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"enter_to_{i}"

# Subtour elimination
for s in range(3, n+1):
    for subset in itertools.combinations(range(1, n), s-1):
        subset = (0,) + subset  # Ensure the depot is in the subset
        prob += sum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = [0]
while len(tour) < n:
    for j in range(n):
        if pulp.value(x[tour[-1], j]) == 1:
            tour.append(j)
            break

# Close the tour
tour.append(0)

# Calculate total travel cost and maximum distance
total_cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(n))
max_distance = max(dist_matrix[tour[i]][tour[i + 1]] for i in range(n))

# Results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)