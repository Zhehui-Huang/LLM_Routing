import math
import pulp

# Given city coordinates
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Total number of cities
n = len(coordinates)

# Calculate Euclidean distance between every pair of cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create a problem variable
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(dist_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Solve the problem
prob.solve()

# Extract tour
tour = [0]
current_city = 0
while True:
    for j in range(n):
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            tour.append(j)
            current_city = j
            break
    if current_city == 0:
        break

# Calculate total cost
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")