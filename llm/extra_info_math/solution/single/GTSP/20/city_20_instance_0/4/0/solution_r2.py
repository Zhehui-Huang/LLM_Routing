import pulp
from math import sqrt

# Define the cities and their coordinates
coordinates = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Define city groups
groups = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# Initialize Problem
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in coordinates for j in coordinates if i != j], 
                          cat=pulp.LpBinary)

u = pulp.LpVariable.dicts("u", list(coordinates.keys()), lowBound=0,
                          cat=pulp.LpContinuous)

# Objective Function
model += pulp.lpSum(sqrt((coordinates[i][0] - coordinates[j][0])**2 + 
                          (coordinates[i][1] - coordinates[j][1])**2) * x[i, j]
                    for i in coordinates for j in coordinates if i != j), "Total Distance"

# Constraints
# Visit each group exactly once
for group in groups:
    model += pulp.lpSum(x[i, j] for i in groups[group] for j in coordinates if j not in groups[group]) == 1
    model += pulp.lpSum(x[j, i] for i in groups[group] for j in coordinates if j not in groups[group]) == 1

# Flow conservation at each city
for k in coordinates:
    model += pulp.lpSum(x[i, k] for i in coordinates if i != k) == \
             pulp.lpSum(x[k, j] for j in coordinates if k != j)

# Subtour Prevention
N = len(coordinates)
for i in coordinates:
    for j in coordinates:
        if i != j and (i != 0 and j != 0):
            model += u[i] - u[j] + N * x[i, j] <= N - 1

# Solve Model
model.solve()

# Display the results
tour = []
total_distance = 0
for v in model.variables():
    if v.varValue > 0 and v.name.startswith('x'):
        edge = eval(v.name[2:])
        tour.append(edge)
        total_distance += sqrt((coordinates[edge[0]][0] - coordinates[edge[1]][0])**2 + 
                               (coordinates[edge[0]][1] - coordinates[edge[1]][1])**2)

# Tour Construction
final_tour = [0]
while len(final_tour) < len(coordinates):
    for i in tour:
        if i[0] == final_tour[-1]:
            final_tour.append(i[1])
            break
final_tour.append(0)  # End at the depot

print(f"Tour: {final_tour}")
print(f"Total travel cost: {total_distance}")