import pulp
import math

# Coordinates of cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Grouping of cities
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Number of vehicles/clusters
k = len(groups)

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

# Creating the cost matrix
n = len(coordinates)
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Optimization problem
prob = pulp.LpProblem("VRP_Single_Visit", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(cost_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints for ensuring one node per group is connected outside the group
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(n) if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(n) if j not in group) == 1

# Flow conservation
for i in range(n):
    prob += pulp.lpSum(x[j, i] for j in range(n) if j != i) == pulp.lpSum(x[i, j] for j in range(n) if j != i)

# Solve the problem
prob.solve()

# Extract the solution
tour = []
current = 0
visited = set()
while True:
    next_city = next(j for j in range(n) if j != current and pulp.value(x[current, j]) == 1)
    tour.append(next_city)
    current = next_city
    if current == 0:
        break

# Compute the total travel cost
total_travel_cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", [0] + tour)
print("Total travel cost:", total_travel_cost)