import pulp as pl
import math

# City coordinates (including the depot)
coordinates = [
    (84, 67),
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Number of cities (including depot)
n = len(coordinates)

# Create a problem instance
problem = pl.LpProblem("TSP", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Auxiliary variable for maximum distance in the objective
max_distance = pl.LpVariable("max_distance", lowBound=0)

# Objective: minimize the maximum distance
problem += max_distance, "Minimize the maximum distance between consecutive cities"

# Constraints: each city must be entered and exited exactly once
for i in range(n):
    problem += pl.lpSum([x[i, j] for j in range(n) if i != j]) == 1, f"Leave_{i}"
    problem += pl.lpSum([x[j, i] for j in range(n) if i != j]) == 1, f"Enter_{i}"

# Prevent subtours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += x[i, j] * euclidean_distance(coordinates[i], coordinates[j]) <= max_distance

# Solve the problem
status = problem.solve()

if status == pl.LpStatusOptimal:
    # Extract the tour
    tour = [0]
    while len(tour) < n:
        for j in range(n):
            if j != tour[-1] and pl.value(x[tour[-1], j]) == 1:
                tour.append(j)
                break
    tour.append(0)  # returning to the depot

    # Calculate distances
    total_distance = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))
    max_dist_between_cities = max(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

    # Output the results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_dist_between_cities}")
else:
    print("The problem did not solve optimally - status:", pl.LpStatus[status])