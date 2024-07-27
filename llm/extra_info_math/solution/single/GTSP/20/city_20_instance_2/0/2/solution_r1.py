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

# All nodes must connect to one other
for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in cities if i != j) == 1

# Constrain each group to have exactly one node participating in the tour
for group in groups.values():
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Solve the model
model.solve()

# Extract the tour
tour = [0]
next_city = tour[0]
for _ in range(len(groups) + 1):
    next_city = next(j for j in cities if j != next_city and pulp.value(x[next_city, j]) == 1)
    tour.append(next_city)
    if next_city == 0:
        break

total_cost = pulp.value(model.objective)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")