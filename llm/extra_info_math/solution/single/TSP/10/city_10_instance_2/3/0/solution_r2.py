from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Coordinates of each city
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance between two cities
def euclidean_dist(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Number of cities including the depot
n = len(coordinates)

# Cost matrix c_ij
cost = {(i, j): euclidean_dist(i, j) for i in range(n) for j in range(n) if i != j}

# Create the problem
model = LpProblem(name="tsp", sense=LpMinimize)

# Decision variables
x = {(i, j): LpVariable(name=f"x_{i}_{j}", cat=LpBinary) for i in range(n) for j in range(n) if i != j}

# Objective function: Minimize the cost of the tour
model += lpSum(cost[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints: Visit every city exactly once and leave every city exactly once
for k in range(n):
    model += lpSum(x[i, k] for i in range(n) if i != k) == 1, f"enter_city_{k}"
    model += lpSum(x[k, j] for j in range(n) if k != j) == 1, f"leave_city_{k}"

# Subtour elimination
for S in range(3, n+1):
    for subset in itertools.combinations(range(1, n), S-1):
        subset = list(subset)
        subset.append(0)  # Including the depot city
        model += lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve()

# Output the result
tour = [0]
current = 0
for _ in range(n - 1):
    for j in range(n):
        if j != current and x[current, j].varValue == 1:
            tour.append(j)
            current = j
            break

tour.append(0)  # Return to the depot city
total_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
print("Tour:", tour)
print("Total travel cost:", total_cost)