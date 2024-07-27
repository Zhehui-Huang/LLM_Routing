from pulp import LpMinimize, LpProblem, lpSum, LpVariable, PULP_CBC_CMD
import math

# Coordinates of cities including depot
coordinates = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Groups of cities excluding the depot
groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]

# Total number of cities
n = len(coordinates)

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate costs
costs = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Set up the problem
problem = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += lpSum(costs[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints for each group
k = len(groups)
for p in range(k):
    problem += lpSum(x[i, j] for i in groups[p] for j in range(n) if j not in groups[p]) == 1
    problem += lpSum(x[j, i] for i in groups[p] for j in range(n) if j not in groups[p]) == 1

# Flow conservation constraints
for i in range(n):
    if i == 0:  # Depot constraints
        problem += lpSum(x[0, j] for j in range(1, n)) == k
        problem += lpSum(x[j, 0] for j in range(1, n)) == k
    elif not any(i in group for group in groups):
        continue
    else:
        problem += (lpSum(x[j, i] for j in range(n)) == lpSum(x[i, j] for j in range(n)))

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=False))

# Extract the tour
tour = [0]
while len(tour) < k + 1:
    for i, j in x:
        if x[i, j].value() == 1 and i == tour[-1]:
            tour.append(j)
            break

# Add the depot to the end of the tour
tour.append(0)

# Calculate total travel cost
total_cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the result
print('Tour:', tour)
print('Total travel cost:', total_cost)