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

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Total number of cities including the depot
n = len(coordinates)

# Creating the cost matrix
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')

# Objective Function: Minimize the travel cost
prob += pulp.lpSum(cost_matrix[i][j] * x[(i, j)] for i in range(n) for j in range(n) if i != j)

# Adding the constraints
# Each group must be visited exactly once
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[(j, i)] for i in group for j in range(n) if i != j) == 1

# Flow conservation constraint for each city
for i in range(1, n):
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == pulp.lpSum(x[(i, k)] for k in range(n) if i != k)

# Return to depot
prob += pulp.lpSum(x[(i, 0)] for i in range(1, n)) == 1
prob += pulp.lpSum(x[(0, i)] for i in range(1, n)) == 1

# Solve the problem
prob.solve()

# Check if a solution exists
if pulp.LpStatus[prob.status] == 'Optimal':
    # Extract the tour starting from depot which is 0
    path = []
    next_city = 0
    while True:
        for i in range(n):
            if i != next_city and x[(next_city, i)].value() == 1:
                path.append(next_city)
                next_city = i
                break
        if next_city == 0:
            path.append(0)
            break

    # Calculate the cost of the path
    total_cost = sum(cost_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))

    print("Tour:", path)
    print("Total travel cost:", total_cost)
else:
    print("No feasible solution found.")