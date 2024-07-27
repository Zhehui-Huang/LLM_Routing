import pulp
import math

# City coordinates (index 0 is the depot)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Euclidean distance calculation function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initialize the optimization model
model = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Decision variables: x_ij = 1 if the connection from i to j is used, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(20) for j in range(20) if i != j), cat='Binary')

# Distance matrix
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(20) for j in range(20) if i != j}

# Objective function: minimize the total distance
model += pulp.lpSum([x[i, j] * distances[i, j] for i in range(20) for j in range(20) if i != j]), "Minimize_total_distance"

# Constraint to ensure each group has exactly one node visited
flatten_groups = [node for group in groups for node in group]
for g in groups:
    model += pulp.lpSum([x[(i, j)] for i in g for j in range(20) if j not in g]) == 1
    model += pulp.lpSum([x[(j, i)] for i in g for j in range(20) if j not in g]) == 1

# Subtour elimination
u = pulp.LpVariable.dicts("u", [i for i in range(1, 20)], lowBound=0, cat='Continuous')
for i in range(1, 20):
    for j in range(1, 20):
        if i != j and (i not in flatten_groups or j not in flatten_groups or groups.index([g for g in groups if i in g][0]) != groups.index([g for g in groups if j in g][0])):
            model += u[i] - u[j] + (len(coordinates) - 1)*x[(i, j)] <= len(coordinates) - 2

# Solve the model
model.solve()

# Extract the tour
tour = [0]
current = 0
for _ in range(sum(len(g) for g in groups) + 1):
    next_cities = [j for j in range(20) if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_cities:
        break
    current = next_cities[0]
    if current == 0:
        break
    tour.append(current)
tour.append(0)  # Return to the depot

# Calculate the total distance of the tour
total_travel_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_travel_cost, 2))