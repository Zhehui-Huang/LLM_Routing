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
x = pl.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=pl.LpBinary)

# Objective function: Minimize total distance
problem += pl.lpSum(x[(i, j)] * dist_matrix[(i, j)] for i in cities for j in cities if i != j)

# Constraints from the groups
for group_id, group_cities in groups.items():
    problem += pl.lpSum(x[(i, j)] for i in group_cities for j in cities if j not in group_cities) == 1
    problem += pl.lpSum(x[(j, i)] for i in group_cities for j in cities if j not in group_cities) == 1

# Conservation of flow constraints at each city (except depot)
for ci in cities:
    if ci != 0:
        problem += pl.lpSum(x[(j, ci)] for j in cities if j != ci) - pl.lpSum(x[(ci, j)] for j in cities if j != ci) == 0
problem += pl.lpSum(x[(0, j)] for j in cities if j != 0) == 1  # only one outgoing from depot
problem += pl.lpSum(x[(j, 0)] for j in cities if j != 0) == 1  # only one incoming to depot

# Solve the problem
status = problem.solve()

# Check if the optimal solution is found
if pl.LpStatus[status] == 'Optimal':
    path = [0]
    current_city = 0
    while len(path) < 6:  # 5 groups + depot
        for j in cities:
            if j != current_city and pl.value(x[(current_city, j)]) == 1:
                path.append(j)
                current_city = j
                break
    path.append(0)  # return to depot

    # Calculate total travel cost
    total_cost = sum(dist_matrix[(path[i], path[i+1])] for i in range(len(path) - 1))
    
    print("Tour:", path)
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")