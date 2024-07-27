import pulp
import math

# City coordinates
coordinates = [
    (8, 11),   # Depot city 0
    (40, 6),   # 1
    (95, 33),  # 2
    (80, 60),  # 3
    (25, 18),  # 4
    (67, 23),  # 5
    (97, 32),  # 6
    (25, 71),  # 7
    (61, 16),  # 8
    (27, 91),  # 9
    (91, 46),  # 10
    (40, 87),  # 11
    (20, 97),  # 12
    (61, 25),  # 13
    (5, 59),   # 14
    (62, 88),  # 15
    (13, 43),  # 16
    (61, 28),  # 17
    (60, 63),  # 18
    (93, 15)   # 19
]

# City groups
groups = [
    [0, 1, 3, 5, 11, 13, 14, 19],   # Group 0
    [0, 2, 6, 7, 8, 12, 15],        # Group 1
    [0, 4, 9, 10, 16, 17, 18]       # Group 2
]

# Calculate distances
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Helper function to define variable accessing indices
def not_same(i, j):
    return i != j

# Defining the problem
problem = pulp.LpProblem("Minimize_Route", pulp.LpMinimize)

# Defining decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if not_same(i, j)), cat='Binary')

# Objective Function: Minimize the total distance
problem += pulp.lpSum(euclidean_distance(i, j) * x[(i, j)] for i in range(len(coordinates)) for j in range(len(coordinates)) if not_same(i, j))

# Setup Constraints
# Ensure exactly one link out and one link in for each city group and depot
for group in groups:
    # Outgoing connection from depot
    if 0 in group:
        problem += pulp.lpSum(x[(0, j)] for j in group if j != 0) == 1
        problem += pulp.lpSum(x[(j, 0)] for j in group if j != 0) == 1

    # Adding vehicle in and out constraints
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(len(coordinates)) if not_same(i, j) and j not in group) == 1
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(len(coordinates)) if not_same(i, j) and j not in group) == 1

# Solve the problem
problem.solve()

# Fetching and printing results
tour = [0]
current = 0
distance_covered = 0

for _ in range(len(coordinates)):
    for next_city in range(len(coordinates)):
        if next_city != current and pulp.value(x[(current, next_city)]) == 1:
            tour.append(next_city)
            distance_covered += euclidean_distance(current, next_city)
            current = next_city
            break
    
print("Tour:", tour)
print("Total travel cost:", distance_covered)