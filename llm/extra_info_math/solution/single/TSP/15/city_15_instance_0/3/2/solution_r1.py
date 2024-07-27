import pulp
import math

# Cities and their coordinates (index 0 is the depot)
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Number of cities including depot
n = len(coordinates)

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord92[1] - coord24[1])**2)

# Cost matrix calculation
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
prob += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints: Each city is left exactly once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Constraints: Each city is entered exactly once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Sub-tour elimination constraints
for i in range(n):
    for j in range(n):
        if i != j and i != 0 and j != 0:
            prob += x[i, j] + x[j, i] <= 1

# Solve the problem
prob.solve()

# Extract the tour from the decision variables
tour = [0]  # start from the depot
visited = set(tour)
for _ in range(1, n):
    current = tour[-1]
    next_city = next(j for j in range(n) if pulp.value(x[current, j]) == 1 and j not already visited)
    tour.append(next_city)
    visited.add(next_city)
tour.append(0)  # return to depot

# Calculate total travel cost
tour_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", tour_cost)