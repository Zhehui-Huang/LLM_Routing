import pulp
import math

# City coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Number of cities (including depot)
n = len(coordinates)

# Helper function to calculate Euclidean distance
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create the distance matrix
cost = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
problem += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n)), "Total Travel Cost"

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"LeaveCity_{i}"
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"EnterCity_{i}"

# Subtour elimination constraints
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] + x[j, i] <= 1

# Solve the problem using the default solver
problem.solve()

# Output the results
tour = []
current_city = 0
visited = [False] * n

while True:
    next_city = None
    for j in range(n):
        if pulp.value(x[current_city, j]) == 1:
            next_city = j
            break
    visited[next_city] = True
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculate the total cost of the tour
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output format
print(f"Tour: {[0] + tour}")
print(f"Total travel cost: {total_cost}")