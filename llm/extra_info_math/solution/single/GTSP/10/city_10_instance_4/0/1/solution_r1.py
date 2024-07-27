import pulp
import math

# City coordinates with indices starting at 0 (depot)
coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Groups of cities
groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Distance function (Euclidean)
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Variables and problem setup
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", [(i, j) for i in coordinates for j in coordinates if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, len(coordinates)), lowBound=0, cat='Continuous')

# Objective: minimize total travel distance
prob += pulp.lpSum([distance(coordinates[i], coordinates[j]) * x[i, j] for i in coordinates for j in coordinates if i != j])

# Constraints
# Each city visited exactly once
for j in coordinates:
    prob += pulp.lpSum([x[i, j] for i in coordinates if i != j]) == 1, f"enter_{j}"
    prob += pulp.lpSum([x[j, i] for i in coordinates if i != j]) == 1, f"leave_{j}"

# One edge in/out per group constraint
for g in groups:
    prob += pulp.lpSum([x[i, j] for i in g for j in coordinates if j not in g]) == 1, f"out_group_{groups.index(g)}"
    prob += pulp.lpWum([x[j, i] for j in g for i in coordinates if i not in g]) == 1, f"in_group_{groups.index(g)}"

# Subtour elimination
for i in range(1, len(coordinates)):
    prob += u[i] - u[0] >= 1 - (len(coordinates) - 1) * (1 - x[0, i]), 'starts_{}'.format(i)
    for j in range(1, len(coordinates)):
        if i != j:
            prob += u[i] - u[j] + (len(coordinates)) * x[i, j] <= len(coordinates) - 1

# Solve the problem
prob.solve()

# Extract tour based on the variable values
tour = []
for v in prob.variables():
    if v.varValue == 1 and v.name.startswith('x'):
        i, j = v.name.split('_')[1].split(',')
        tour.append((int(i), int(j)))

# Find the tour starting from depot (0)
sorted_tour = [0]
while len(sorted_tour) < len(coordinates):
    next_city = [j for (i, j) in tour if i == sorted_tour[-1]][0]
    sorted_tour.append(next_city)
    if next_city == 0:
        break

# Calculate total travel distance
total_distance = sum(distance(coordinates[sorted_tour[i]], coordinates[sorted_tour[i + 1]]) for i in range(len(sorted_tour) - 1))

# Output the result
print("Tour:", sorted_tour)
print("Total travel cost:", total_distance)