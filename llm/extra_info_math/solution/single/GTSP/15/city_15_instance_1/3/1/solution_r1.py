from math import sqrt
import pulp

# City coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30),
    (36, 12), (93, 43), (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Groups, not including the depot (city 0 is always included as depot)
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate distances between all pairs of nodes
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Integer programming model
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables: x[i][j] = 1 if path goes from i to j
x = [[pulp.LpVariable(f"x_{i}_{j}", cat='Binary') if i != j else None for j in range(n)] for i in range(n)]

# Objective: Minimize total travel cost
model += pulp.lpSum(x[i][j] * distances[i][j] for i in range(n) for j in range(n) if i != j and x[i][j] is not None)

# Constraints
def add_constraints_for_groups():
    for group in groups:
        model += pulp.lpSum(x[i][j] for i in group for j in range(n) if j not in group and x[i][j] is not None) == 1
        model += pulp.lpSum(x[j][i] for i in group for j in range(n) if j not in group and x[j][i] is not None) == 1

add_constraints_for_groups()

# Flow conservation at each city except the depot
for k in range(1, n):
    model += pulp.lpSum(x[j][k] for j in range(n) if j != k and x[j][k] is not None) == \
             pulp.lpSum(x[k][j] for j in range(n) if j != k and x[k][j] is not None)

model.solve()

# Extract the solution: Find tour from the LP solution
tour = []
current = 0
visited = [False] * n
tour.append(current)

# Constructing the tour from variables
while True:
    visited[current] = True
    next_city = None
    for j in range(n):
        if j != current and x[current][j] is not None and pulp.value(x[current][j]) == 11:
            if visited[j] is False:
                next_city = j
                break
    if next_city is None:
        break
    tour.append(next_city)
    current = next_city
    if current == 0:
        break

# Calculate total distance
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Print results
print("Tour:", tour)
print("Total travel cost:", round(total_distance, 2))