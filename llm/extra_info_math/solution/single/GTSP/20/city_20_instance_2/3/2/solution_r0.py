import pulp
import math

# City coordinates, including the depot
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# City groups
groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Total number of cities including depot
num_cities = len(coordinates)

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distance matrix
distances = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("TSP_Group", pulp.LpMinimize)

# Create decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Objective Function: Minimize the sum of the distances for the selected paths
problem += pulp.lpSum([distances[i, j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j]), "Total Travel Cost"

# Constraints
for group in groups:
    problem += pulp.lpSum([x[i, j] for i in group for j in range(num_cities) if j not in group and (i, j) in x]) == 1, f"One exit from group {group}"
    problem += pulp.lpSum([x[j, i] for i in group for j in range(num_cities) if j not in group and (j, i) in x]) == 1, f"One entry into group {group}"

# Ensure exactly one connection out of and into each city (excluding group constraints)
for i in range(num_cities):
    problem += pulp.lpSum([x[i, j] for j in range(num_cities) if (i, j) in x]) == 1
    problem += pulp.lpSum([x[j, i] for j in range(num_cities) if (j, i) in x]) == 1

# Solve the problem
problem.solve()

# Check the solution status
print("Status:", pulp.LpStatus[problem.status])

# Output the tour and the cost
tour = []
start = 0
next_city = start

while True:
    next_step = [j for j in range(num_cities) if (next_city, j) in x and pulp.value(x[next_city, j]) == 1]
    if next_step:
        next_city = next_step[0]
        tour.append(next_city)
        if next_city == start:
            break

print("Tour: ", tour)
print("Total travel cost: ", pulp.value(problem.objective))