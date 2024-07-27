import pulp
import math

# Coordinates for each city
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# City groups
groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

# Calculate Euclidean distance between two cities
def calculate_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the problem
prob = pulp.LpProblem("Minimize_total_travel_cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(x[(i, j)] * calculate_distance(i, j) for i in cities for j in cities if i != j), "Total travel cost"

# Constraints
# Each group must have exactly one outgoing edge to a node outside the group
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1

# Each group must have exactly one incoming edge from a node outside the group
for group in groups:
    prob += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1

# Flow conservation
for i in cities:
    prob += (pulp.lpSum(x[(j, i)] for j in cities if j != i) - pulp.lpSum(x[(i, j)] for j in cities if j != i) == 0)

# Solve the problem
prob.solve()

# Extract the solution
tour = [0]
visited = {0}
current = 0
while True:
    next_step = [j for j in cities if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_step:
        break
    next_city = next_step[0]
    tour.append(next_city)
    visited.add(next_city)
    current = next_city
    if current == 0:
        break

total_cost = pulp.value(prob.objective)

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")