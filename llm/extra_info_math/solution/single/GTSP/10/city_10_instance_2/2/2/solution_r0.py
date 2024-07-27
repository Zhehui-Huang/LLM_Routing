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

# Each group must be connected exactly once to the rest of the graph
for group_id, group_cities in groups.items():
    # One outgoing connection from each group
    problem += pl.lpSum(x[(i, j)] for i in group_cities for j in cities if j not in group_cities) == 1

    # One incoming connection to each group
    problem += pl.lpSum(x[(j, i)] for i in group_cities for j in cities if j not in group_cities) == 1

# Flow conservation at each city (except depot)
for ci in cities:
    if ci != 0:
        problem += pl.lpSum(x[(j, ci)] for j in cities if j != ci) == pl.lpSum(x[(ci, j)] for j in cities if j != ci)

# Solve the problem
status = problem.solve()

# Check if the optimal solution is found
if pl.LpStatus[status] == 'Optimal':
    # Extract the tour
    tour = []
    visited = [0]
    last_visited = 0
    # Find the next city iteratively based on the solution starting from depot
    while len(visited) < len(cities):
        for j in cities:
            if last_visited != j and x[(last_visited, j)].varValue == 1:
                tour.append(j)
                visited.append(j)
                last_visited = j
                break

    # Adding back the depot at end of the tour
    tour = [0] + tour + [0]

    # Calculate total travel cost
    total_cost = sum(dist_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

    # Output the required results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")