from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary
import math

# Define the points (cities) and their coordinates
points = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define the city groups
city_groups = [
    [7, 9], [1, 3], [4, 6], [8], [5], [2]
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n = len(points)  # Number of all nodes
group_count = len(city_groups)

# List of all nodes and representative nodes to include in the tour from each group
V = list(points.keys())
representatives = [gr[0] for gr in city_groups]  # Pick the first city in each group as representative

# Create a LP problem instance
model = LpProblem(name="minimum-travel-cost-tsp", sense=LpMinimize)

# Variables x_ij where i, j in V
x = LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat=LpBinary)

# Objective Function
model += lpSum(euclidean_distance(points[i], points[j]) * x[i, j] for i in V for j in V if i != j)

# Constraints

# Only leave from each node once and enter each node once
for j in V:
    model += lpSum(x[i, j] for i in V if i != j) == 1
    model += lpSum(x[j, k] for k in V if j != k) == 1

# Subtour Elimination for selected nodes including depot and representatives
n2 = [0] + representatives
for i in range(len(n2)):
    for j in range(len(n2)):
        if i != j:
            model += x[n2[i], n2[j]] + x[n2[j], n2[i]] <= 1

# Solve the model
model.solve()

# Append tour from the depot with selected representatives
tour = [0]
while len(tour) < group_count + 1:
    current = tour[-1]
    next_city = next(j for j in V if x[current, j].value() == 1)
    if next_city != 0 or len(tour) == group_count:
        tour.append(next_city)

# Find and plug in the last connection back to depot if it's not present (because of constraint relaxation above)
if tour[-1] != 0:
    tour.append(0)

# Calculate the total travel cost
total_cost = sum(euclidean_distance(points[tour[i]], points[tour[i + 1]]) for i in range(len(tour) - 1))

# Print result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")