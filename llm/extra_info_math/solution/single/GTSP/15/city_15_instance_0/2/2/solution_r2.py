from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD
import math

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Initialize problem
model = LpProblem(name="robot-routing-problem", sense=LpMinimize)

# Variables
x = {(i, j): LpVariable(name=f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}
u = {i: LpVariable(name=f"u_{i}", lowBound=0, cat='Continuous') for i in cities}

# Objective Function
model += lpSum(euclidean_distance(cities[i], cities[j]) * x[i, j]
               for i in cities for j in cities if i != j)

# Constraints
# Ensure connection for each subgroup
for group in groups.values():
    model += lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Flow conservation
for k in cities:
    model += lpSum(x[i, k] for i in cities if i != k) == lpSum(x[k, j] for j in cities if j != k)

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j:
            model += u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1

# Solve the model
model.solve(PULP_CBC_CMD(msg=0))

# Tour extraction from the solution
tour = []
current = 0
visited = {current}
for _ in range(len(cities)):
    for j in cities:
        if x[current, j].value() == 1:
            tour.append(current)
            current = j
            visited.add(current)
            break
    if current == 0:
        break
tour.append(0)  # to complete tour back to the depot

# Calculate travel cost
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")