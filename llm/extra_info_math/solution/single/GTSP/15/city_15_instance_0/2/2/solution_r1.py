from pulp import LpMinimize, LpProblem, LpVariable, LpBinary, lpSum
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
# Each cluster must have exactly one outgoing edge to a node outside the cluster
for _, group in groups.items():
    model += lpSum(x[i, j] for i in group for j in cities if j not in group) == 1

# Each cluster must have exactly one incoming edge from a node outside the cluster
for _, group in groups.items():
    model += lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Flow conservation constraint
for k in cities:
    model += lpSum(x[i, k] for i in cities if i != k) == lpSum(x[k, j] for j in cities if j != k)

# Subtour prevention constraints
k = len(groups) + 1  # Including depot
for i in cities:
    for j in cities:
        if i != j:
            model += u[i] - u[j] + k * x[i, j] <= k - 1

# Solve the problem
model.solve()

# Extract the tour
edges = [(i, j) for i in cities for j in cities if i != j and x[i, j].varValue == 1]
current = 0
tour = [0]
while len(edges) > 0:
    for (i, j) in edges:
        if i == current:
            tour.append(j)
            current = j
            edges.remove((i, j))
            break

# Calculate total cost
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")