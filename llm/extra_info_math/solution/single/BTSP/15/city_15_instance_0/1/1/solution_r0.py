import math
import pulp

# City coordinates
coordinates = [
    (9, 93),  # Depot city
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coordinates)  # Number of cities including depot
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Indexes representing the cities
indexes = list(range(n))

# Create problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if travel from i to j, else 0
x = pulp.LpVariable.dicts("x", (indexes, indexes), cat=pulp.LpBinary)

# Auxiliary variable to minimize
z = pulp.LpVariable("z", lowBound=0)

# Objective function: minimize the maximum distance
prob += z

# Constraints
# Outgoing sum
for i in indexes:
    prob += pulp.lpSum(x[i][j] for j in indexes if i != j) == 1
    
# Incoming sum
for j in indexes:
    prob += pulp.lpSum(x[i][j] for i in indexes if i != j) == 1

# Prevent sub-tour: Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", indexes, lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in indexes:
    for j in indexes:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + n * x[i][j] <= n - 1

# Maximize-Z constraint
for i in indexes:
    for j in indexes:
        if i != j:
            prob += x[i][j] * distances[i][j] <= z

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current_city = 0
tour.append(current_city)
for _ in range(n):
    next_city = None
    for j in indexes:
        if j != current_city and pulp.value(x[current_city][j]) == 1:
            next_city = j
            break
    if next_city is None:
        break
    tour.append(next_city)
    current_city = next_city

# Calculate metrics
total_distance = 0.0
max_distance = 0.0
for i in range(1, len(tour)):
    dist = distances[tour[i - 1]][tour[i]]
    total_distance += dist
    if dist > max_distance:
        max_distance = dist

# Ensure we return to the depot
tour.append(0)
total_distance += distances[tour[-2]][0]

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_eraseion:.2f}")