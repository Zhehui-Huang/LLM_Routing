import pulp
import math

# Locations of all the cities including the depot
locations = [
    (8, 11),  # Depot city 0
    (40, 6),  # City 1
    (95, 33),  # City 2
    (80, 60),  # City 3
    (25, 18),  # City 4
    (67, 23),  # City 5
    (97, 32),  # City 6
    (25, 71),  # City 7
    (61, 16),  # City 8
    (27, 91),  # City 9
    (91, 46),  # City 10
    (40, 87),  # City 11
    (20, 97),  # City 12
    (61, 25),  # City 13
    (5, 59),  # City 14
    (62, 88),  # City 15
    (13, 43),  # City 16
    (61, 28),  # City 17
    (60, 63),  # City 18
    (93, 15)  # City 19
]

# Grouping cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Calculating distance using Euclidean formula
def distance(city1, city2):
    return math.sqrt((locations[city1][0] - locations[city2][0]) ** 2 + (locations[city1][1] - locations[city2][1]) ** 2)

# Constructing the problem
prob = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(20) for j in range(20) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, 20), 0, 20, pulp.LpContinuous)

# Objective
prob += pulp.lpSum([distance(i, j) * x[i, j] for i in range(20) for j in range(20) if i != j]), "Total travel cost"

# Constraints
for g in groups:
    prob += pulp.lpSum([x[i, j] for i in g for j in range(20) if i != j]) == 1, f"Outgoing_from_group_{groups.index(g)}"
    prob += pulp.lpSum([x[j, i] for i in g for j in range(20) if i != j]) == 1, f"Incoming_to_group_{groups.index(g)}"

# Flow conservation
for i in range(20):
    prob += (pulp.lpSum([x[i, j] for j in range(20) if i != j]) - pulp.lpSum([x[j, i] for j in range(20) if i != j])) == 0, f"Flow_conservation_{i}"

# Subtour elimination
for i in range(1, 20):
    for j in range(1, 20):
        if i != j:
            prob += u[i] - u[j] + 19 * x[i, j] <= 18, f"Subtour_constraint_{i}_{j}"

# Solve the problem
prob.solve()

# Extract the solution
tour = []
visited = [0]
while len(visited) < len(groups) + 1:
    current = visited[-1]
    next_city = [j for j in range(20) if pulp.value(x[current, j]) == 1 and j not in visited]
    if next_city:
        visited.append(next_city[0])
visited.append(0)  # Return to depot

total_cost = pulp.value(prob.objective)

print(f"Tour: {visited}")
print(f"Total travel cost: {total_cost:.2f}")