from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary
import math

# Define cities and their coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate costs
n = len(cities)
cost = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            cost[i][j] = euclidean_distance(cities[i], cities[j])

# Create the problem variable
prob = LpProblem("TSP", LpMinimize)

# Variables: x_ij
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=LpBinary)

# Objective function
prob += lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave i
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter i

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = [0]
current = 0
while True:
    next_steps = [j for j in range(n) if j != current and x[current, j].varValue == 1]
    if not next_steps:
        break
    current = next_steps[0]
    tour.append(current)

# Adding the return to the starting city (depot)
tour.append(0)

# Calculate total travel cost
total_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")