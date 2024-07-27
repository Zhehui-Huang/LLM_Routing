import pulp as pl
import math

# Define the cities and their coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Function to calculate Euclidean distance
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Compute the distance matrix
dist_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            dist_matrix[(i, j)] = distance(cities[i], cities[j])

# Create the problem
problem = pl.LpProblem("RobotTour", pl.LpMinimize)

# Variables: x_ij is 1 if the robot travels from city i to city j, 0 otherwise
x = pl.LpVariable.dicts(
    "x",
    ((i, j) for i in cities for j in cities if i != j),
    cat=pl.LpBinary
)

# Objective function: Minimize total distance
problem += pl.lpSum(x[(i, j)] * dist_density[(i, j)] for i in cities for j in cities if i != j)

# Constrains for the groups
for g, nodes in enumerate(groups.values()):
    problem += pl.lpSum(x[(i, j)] for i in nodes for j in cities if j not in nodes) == 1
    problem += pl.lpSum(x[(j, i)] for i in nodes for j in cities if j not in nodes) == 1

# Conservation of flow for non-depot cities
for c in cities:
    if c != 0:
        problem += pl.lpSum(x[(c, j)] for j in cities if j != c) == pl.lpSum(x[(j, c)] for j in cities if j != c)
        problem += pl.lpSum(x[(j, c)] for j in cities if j != c) == pl.lpSum(x[(c, j)] for j in cities if j != c)

# Solve the problem
status = problem.solve()

# Extract and print results if solved
if pl.LpStatus[status] == "Optimal":
    tour, total_cost = [0], 0
    next_city = 0
    while True:
        for i in cities:
            if i != next_city and x[(next_city, i)].varValue > 0.99:  # To handle float precision
                tour.append(i)
                total_cost += dist_matrix[(next_city, i)]
                next_city = i
                break
        if next_city == 0:
            break
    # Output solution
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")