import pulp
import math

# City coordinates indexed from 0 to 19
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Calculate Euclidean distances
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
distances = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective Function
model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1  # leave each city once
    model += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1  # enter each city once

# Subtour elimination constraints
for i in range(2, n+1):
    for subset in itertools.combinations(range(1, n), i):
        model += pulp.lpSum(x[k, l] for k in subset for l in subset if k != l) <= len(subset) - 1

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

if status == pulp.LpStatusOptimal:
    print("Found optimal tour.")
    tour = []
    position = 0
    while True:
        tour.append(position)
        for j in range(n):
            if pulp.value(x[position, j]) == 1:
                position = j
                break
        if position == 0:
            break
    tour.append(0)  # returning to the depot
    tour_cost = pulp.value(model.objective)
    print(f"Tour: {tour}")
    print(f"Total travel cost: {tour_cost:.2f}")
else:
    print("Failed to find optimal solution.")