import pulp
import math
import itertools

# City coordinates indexed from 0 to 19
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distances
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coordinates)
distances = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective Function
model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints - entering and leaving each city
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1  # leave each city once
    model += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1  # enter each city once

# Subtour elimination constraints (SEC)
for i in range(2, n):
    for subset in itertools.combinations(range(1, n), i):
        S = list(subset)
        model += pulp.lpSum(x[S[k], S[j]] for k in range(len(S)) for j in range(len(S)) if k != j) <= len(S) - 1

# Solve Model
model.solve()

# Processing results
tour = []
active_arcs = [(i, j) for i in range(n) for j in range(n) if pulp.value(x[i, j]) == 1]
current_city = 0
while len(active_arcs) > 0:
    for i, j in active_arcs:
        if i == current_city:
            tour.append(current_city)
            current_city = j
            active_arcs.remove((i, j))
            break
tour.append(0)  # Return to the depot city

# Calculate total distance
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Printing solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")