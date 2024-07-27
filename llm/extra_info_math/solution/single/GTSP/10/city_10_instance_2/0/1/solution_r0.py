!pip install pulp

import pulp
import math

# Define city coordinates
cities = {
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

# Define the city groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialize the problem
prob = pulp.LpProblem("Minimize_Tour", pulp.LpMinimize)

# Variables: x_ij = 1 if travel from i to j, 0 otherwise
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary) for i in cities for j in cities if i != j}

# u variables for subtour elimination constraints
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in cities if i != 0}

# Objective: Minimize total travel cost
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j), "Total travel cost"

# Constraints
# Each group must have exactly one outgoing and incoming connection
for group in groups.values():
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1, f"Outgoing_from_group_{group}"
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1, f"Incoming_to_group_{group}"

# Flow conservation constraint
for i in cities:
    prob += (pulp.lpSum(x[j, i] for j in cities if j != i) == pulp.lpSum(x[i, j] for j in cities if j != i)), f"Flow_conservation_{i}"

# Subtour elimination constraints
for g in groups.values():
    for i in g:
        for j in g:
            if i != j:
                prob += u[i] - u[j] + len(g) * x[i, j] + (len(g) - 2) * x[j, i] <= len(g) - 1, f"Subtour_elimination_{i}_{j}"

# Solve the problem
status = prob.solve()
print("Status:", pulp.LpStatus[status])

# Output result
tour = []
current_city = 0
visited = set([0])
total_cost = 0

while len(tour) < len(groups) + 1:
    for i in cities:
        if i not in visited and pulp.value(x[current_city, i]) == 1:
            tour.append(i)
            total_cost += distance(current_city, i)
            visited.add(i)
            current_city = i
            break

# Make sure to return to the depot
tour.append(0)
total_cost += distance(current_city, 0)

print("Tour:", tour)
print("Total travel cost:", total_cost)