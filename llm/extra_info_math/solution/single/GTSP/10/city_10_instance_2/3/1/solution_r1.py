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

# Set up the optimization problem
problem = LpProblem("TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
problem += lpSum(costs[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints for each group
for p in range(len(groups)):
    problem += lpSum(x[i, j] for i in groups[p] for j in range(n) if j not in groups[p]) == 1
    problem += lpSum(x[j, i] for i in groups[p] for j in range(n) if j not in groups[p]) == 1

# Flow conservation constraints
for i in range(n):
    if i == 0:  # Depot constraints
        problem += lpSum(x[i, j] for j in range(n) if i != j) == len(groups)
        problem += lpSum(x[j, i] for j in range(n) if i != j) == len(groups)
    elif not any(i in group for group in groups):
        continue  # Skip cities not in any group
    else:
        problem += lpSum(x[j, i] for j in range(n) if i != j) == lpSum(x[i, j] for j in range(n) if i != j)

# Solve the problem
status = problem.solve(PULP_CBC_CMD(msg=0))

# Check if the solution is optimal
if status == 1:
    tour = [0]
    visited = set(tour)

    # Extract the tour
    while len(visited) < len(groups) + 1:
        for j in range(n):
            if x[tour[-1], j].value() == 1 and j not in visited:
                tour.append(j)
                visited.add(j)
                break

    # Complete the cycle by returning to the depot
    tour.append(0)

    # Calculate total travel cost
    total_cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    # Output
    print('Tour:', tour)
    print('Total travel cost:', total_cost)
else:
    print("No optimal solution found.")