import pulp
import math

# Coordinates of cities including the depot
coordinates = [
    (16, 90),  # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Create the problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(distance(i, j) * x[i, j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Each group must connect to exactly one other city
for group in city_groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(len(coordinates)) if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Flow conservation at each city excluding the depot
for c in range(1, len(coordinates)):
    prob += pulp.lpSum(x[i, c] for i in range(len(coordinates)) if i != c) == pulp.lpSum(x[c, j] for j in range(len(coordinates)) if j != c)

# Solving the problem
prob.solve()

# Checking the solution status
if pulp.LpStatus[prob.status] == 'Optimal':
    # Extracting the tour
    path = []
    for v in prob.variables():
        if v.varValue > 0 and 'x' in v.name:
            indices = tuple(map(int, v.name.split('_')[1:]))
            path.append(indices)

    # Ordering path by starting from depot
    tour = [0]
    next_city = dict(path)
    while len(tour) < len(path) + 1:
        current = tour[-1]
        tour.append(next_city[current])

    # Compute the total travel cost
    total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("Failed to solve the problem. Status:", pulp.LpStatus[prob.status])