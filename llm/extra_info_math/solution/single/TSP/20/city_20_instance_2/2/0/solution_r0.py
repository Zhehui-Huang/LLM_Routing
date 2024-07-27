import pulp
import math

# Define the cities and their coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Calculate the distance matrix
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coordinates)
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 
                          cat='Binary')

# Objective function: minimize the travel cost
prob += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraint: Leave each city only once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Constraint: Enter each city only once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour Elimination constraints
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current = 0
while True:
    tour.append(current)
    next_cities = [j for j in range(n) if pulp.value(x[current, j]) == 1]
    if not next_cities:
        break
    current = next_cities[0]

# Ensure the tour returns to the depot
tour.append(tour[0])

# Print the results
total_distance = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")