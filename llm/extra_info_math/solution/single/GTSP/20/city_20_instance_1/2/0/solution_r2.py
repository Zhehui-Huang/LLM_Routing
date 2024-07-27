import pulp
import math

# City coordinates
coordinates = [
    (14, 77),  # City 0 - Depot
    (34, 20),
    (19, 38),
    (14, 91),
    (68, 98),
    (45, 84),
    (4, 56),
    (54, 82),
    (37, 28),
    (27, 45),
    (90, 85),
    (98, 76),
    (6, 19),
    (26, 29),
    (21, 79),
    (49, 23),
    (78, 76),
    (68, 45),
    (50, 28),
    (69, 9)
]

# Grouping of cities in clusters
clusters = [
    [5, 6, 7, 11, 17],   # Group 0
    [1, 4, 8, 13, 16],   # Group 1
    [2, 10, 15, 18, 19], # Group 2
    [3, 9, 12, 14]       # Group 3
]

# Function to compute Euclidean distance between cities
def calc_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Model
model = pulp.LpProblem("Minimum_Dist", pulp.LpMinimize)

# Variables
# x[i][j]: i -> j
x = {}
for i in range(20):
    for j in range(20):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective
model += pulp.lpSum(x[(i, j)] * calc_distance(i, j) for i in range(20) for j in range(20) if i != j)

# Constraints
# Ensure entering and leaving each cluster exactly once
for cluster in clusters:
    model += pulp.lpSum(x[(i, j)] for i in cluster for j in range(20) if j not in cluster) == 1
    model += pulp.lpSum(x[(j, i)] for i in cluster for j in range(20) if j not in cluster) == 1

# Each city is entered and left exactly once
for k in range(20):
    model += pulp.lpSum(x[(i, k)] for i in range(20) if i != k) == pulp.lpSum(x[(k, j)] for j in range(20) if k != j)

# Solve
model.solve()

# Extract tour (starting from city 0 and then find subsequent cities)
tour = [0]
current = 0
while True:
    next_city = [j for j in range(20) if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_explore:
        break
    next_city = next_city[0]
    if next_city == 0:
        break
    tour.append(next_city)
    current = next_city
tour.append(0)

# Calculate cost
cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", cost)