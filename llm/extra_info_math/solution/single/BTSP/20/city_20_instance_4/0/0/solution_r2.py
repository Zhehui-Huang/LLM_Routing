import math
import pulp
import itertools

# Coordinates of each city including depot (indexed from 0 to 19)
coords = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities, including the depot
n = len(coords)

# Calculate Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0]) ** 2 + (coords[city1][1] - coords[city2][1]) ** 2)

# Problem declaration
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables x_ij where i, j are cities; j != i
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Variable to minimize the maximum distance between consecutive cities
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function
prob += max_distance

# Constraints ensuring each city is entered and left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Constrain max_distance to be at least the distance between each pair of cities in the path
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= max_distance

# Add subtour elimination constraints using the formulation discussed
for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = prob.solve()
if status == pulp.LpStatusOptimal:
    # Retrieve the path
    path = []
    curr = 0  # Start at the depot
    while len(path) < n:
        path.append(curr)
        next_city = [j for j in range(n) if j != curr and pulp.value(x[curr, j]) == 1][0]
        curr = next_city
    path.append(0)  # Return to depot

    # Calculate total travel cost and max distance between consecutive cities
    total_distance = sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1))
    max_leg_distance = max(distance(path[i], path[i + 1]) for i in range(len(path) - 1))

    # Output results
    print("Tour:", path)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_leg_distance)
else:
    print("The problem could not be solved.")