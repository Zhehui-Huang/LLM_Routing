from pulp import LpMinimize, LpProblem, LpVariable, lpSum, PulpSolverError
from math import sqrt

# City coordinates (including the depot city 0)
coordinates = [
    (90, 3),  # Depot
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Define city groups
city_groups = [
    [3, 6],
    [5, 8],
    [4, 9],
    [1, 7],
    [2]
]

def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Precompute the distances
distances = {
    (i, j): euclidean_distance(coordinates[i], coordinates[j])
    for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j
}

# Total number of cities including depot
num_cities = len(coordinates)

# Create the problem
problem = LpProblem("Robot_Min_Tour", LpMinimize)

# Decision variables: x_ij = 1 if the path from city i to city j is taken, otherwise 0
x = LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j], cat='Binary')

# Objective Function
problem += lpSum(distances[(i, j)] * x[(i, j)] for i in range(num_cities) for j in range(num_cities) if i != j)

# Each group exactly connects once with outside nodes
for group in city_groups:
    all_other_cities = [j for j in range(num_cities) if j not in group]
    problem += lpSum(x[(i, j)] for i in group for j in all_other_cities) == 1
    problem += lpSum(x[(j, i)] for i in group for j in all_other_cities) == 1

# Flow conservation constraint for each city
for i in range(num_cities):
    problem += lpSum(x[(j, i)] for j in range(num_cities) if i != j) == lpSum(x[(i, j)] for j in range(num_cities) if i != j)

# Solve the problem
problem.solve()

# Extract the tour from the decision variables
tour = [0]
for _ in range(len(city_groups) + 1):
    current_city = tour[-1]
    next_city = next(j for j in range(num_cities) if i != j and x[(current_city, j)].value() == 1)
    tour.append(next_city)
    if next_city == 0:
        break

# Calculate the total cost of the tour
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")