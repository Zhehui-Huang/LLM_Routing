import pulp
import itertools
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
dist_matrix = [[euclidean(inner, outer) for outer in coords] for inner in coords]

# Create problem
prob = pulp.LpProblem("Minimized_Maximum_Distance_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), lowBound=0, upBound=1, cat='Binary')

# Additional variables for MTZ constraints
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective
prob += pulp.lpSum(x[i, j] * dist_matrix[i][j] for i in range(n) for j in range(n) if i != j), "Total travel cost"

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"sum_to_{i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"sum_from_{i}"

# Subtour elimination constraints (MTZ)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
prob.solve()

# Retrieve the solution
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Order the tour starting from depot
ordered_tour = [0]
for _ in range(len(tour)):
    last = ordered_tour[-1]
    next_city = next(item[1] for item in tour if item[0] == last)
    ordered_tour.append(next_city)

# Close tour to return to depot
ordered_tour.append(0)

# Calculating total cost and max leg length
total_distance = sum(dist_matrix[ordered_tour[i]][ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))
max_leg = max(dist_matrix[ordered_tour[i]][ordered_tour[i + 1]] for i in range(len(ordered_tour) - 1))

# Outputs
print("Tour:", ordered_tour)
print("Total travel cost:", round(total_distance, 2))
print("Maximum distance between consecutive cities:", round(max_leg, 2))