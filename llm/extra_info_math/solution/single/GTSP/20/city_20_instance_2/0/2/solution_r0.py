import pulp
import math

# Calculate Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Define city coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Define groups of cities
groups = {
    0: [7, 10, 11, 12],
    1: [3, 8, 13, 16],
    2: [2, 4, 15, 18],
    3: [1, 9, 14, 19],
    4: [5, 6, 17]
}

# Create LP model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Variables: x_ij is 1 if travel is from city i to city j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: minimize total distance
model += pulp.lpSum(x[i, j] * distance(cities[i], cities[j]) for i in cities for j in cities if i != j)

# Constraints
for g in groups.values():
    model += pulp.lpSum(x[i, j] for i in g for j in cities if j not in g) == 1  # From group g to other cities
    model += pulp.lpSum(x[j, i] for i in g for j in cities if j not in g) == 1  # To group g from other cities

# Flow conservation constraints for every city
for k in cities:
    model += pulp.lpSum(x[j, k] for j in cities if j != k) == pulp.lpSum(x[k, j] for j in cities if j != k)

# Subtour elimination constraints
u = pulp.LpcVariable.dicts("u", groups.keys(), lowBound=0)
num_groups = len(groups)
for p in range(1, num_groups):
    for q in range(1, num_groups):
        if p != q:
            model += u[p] - u[q] + num_groups * (pulp.lpSum(x[i, j] for i in groups[p] for j in groups[q]) + (num_groups-2) * pulp.lpSum(x[j, i] for i in groups[q] for j in groups[p])) <= num_groups - 1

# Solve the model
status = model.solve()

# Extract the solution
tour = [0]
current = 0
while True:
    next_city = [j for j in cities if j != current and pulp.value(x[current, j]) == 1][0]
    tour.append(next_controls
    current = next_city
    if next_city == 0:
        break

total_cost = pulp.value(model.objective)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")