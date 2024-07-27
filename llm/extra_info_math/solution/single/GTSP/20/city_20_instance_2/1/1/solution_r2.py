import math
from ortools.linear_solver import pywraplp

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define city coordinates (depot + 19 cities)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Define city groups
groups = [
    [7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18],
    [1, 9, 14, 19], [5, 6, 17]
]

# Integer programming solver
solver = pywraplp.Solver.CreateSolver('CBC')

# Decision variables
x = {}
n = len(coordinates)
all_cities = set(range(n))
visited = {}

# Create variables, x[i, j] = 1 if the path is chosen from city i to city j
for i in range(n):
    for j in range(n):
        if i != j:
            x[(i, j)] = solver.BoolVar(f'x[{i},{j}]')

# Create variables to select one city from each group
for index, group in enumerate(groups):
    visited[index] = solver.BoolVar(f'visited[{index}]')

# Objective: Minimize total distance
objective = solver.Objective()
for i in range(n):
    for j in range(n):
        if i != j:
            objective.SetCoefficient(x[(i, j)], euclidean_distance(coordinates[i], coordinates[j]))
objective.SetMinimization()

# Constraints

# Create linking constraints between group selection and path selection
for index, group in enumerate(groups):
    solver.Add(sum(x[(i, j)] for i in group for j in all_cities if i != j) == visited[index])
    solver.Add(sum(x[(j, i)] for i in group for j in all_cities if i != j) == visited[index])

# Ensure exactly one city from each group is visited
for index, group in enumerate(groups):
    solver.Add(sum(x[(i, j)] for i in group for j in all_cities if i != j) == 1)
    solver.Add(sum(x[(j, i)] for i in group for j in all_cities if i != j) == 1)

# Ensure each city is entered and left exactly once
for city in all_cities:
    solver.Add(sum(x[(i, city)] for i in all_cities if i != city) == sum(x[(city, j)] for j in all_cities if j != city))

# Solve the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and x[(i, j)].solution_value() > 0.9:
                tour.append((i, j))
    # Display the tour in order
    current_city = 0
    optimal_tour = [0]
    while len(tour) > 0:
        for i in range(len(tour)):
            if tour[i][0] == current_city:
                current_city = tour[i][1]
                optimal_tour.append(current_city)
                tour.pop(i)
                break
    print('Tour:', optimal_tour)
else:
    print('The problem does not have an optimal solution.')