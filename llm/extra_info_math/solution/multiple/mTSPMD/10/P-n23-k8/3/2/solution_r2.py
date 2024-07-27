import math
from ortools.linear_solver import pywraplp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Helper function to calculate Euclidean distances
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create the distance matrix
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Solver initialization
solver = pywraplp.Solver.CreateSolver('SCIP')

# Number of robots and their respective starting depots (0-indexed)
num_robots = 8
depots = list(range(num_robots))

# Variables:
# x[k][i][j]: whether robot k travels from city i to j
x = {}
for k in range(num_robots):
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j:
                x[k, i, j] = solver.BoolVar(f'x[{k},{i},{j}]')

# u[i] is a position of the city in the tour to eliminate subtours
u = {}
for i in range(len(coordinates)):
    u[i] = solver.IntVar(1, len(coordinates), f'u[{i}]')

# Constraints
# Only one trip out from each city, and one trip into each city
for j in range(len(coordinates)):
    if j not in depots:  # cities that are not depots
        solver.Add(sum(x[k, i, j] for k in range(num_robots) for i in range(len(coordinates)) if i != j) == 1)
        solver.Add(sum(x[k, j, i] for k in range(num_robots) for i in range(len(coordinates)) if i != j) == 1)

# Each robot must start and end at its depot
for k in range(num_robots):
    solver.Add(sum(x[k, depots[k], j] for j in range(len(coordinates)) if j != depots[k]) == 1)
    solver.Add(sum(x[k, j, depots[k]] for j in range(len(coordinates)) if j != depots[k]) == 1)

# Subtour elimination
for i in range(1, len(coordinates)):
    for j in range(1, len(coordinates)):
        if i != j:
            for k in range(num_robots):
                solver.Add(u[i] - u[j] + len(coordinates) * x[k, i, j] <= len(coordinates) - 1)

# Objective: Minimize total distance traveled by all robots
objective = solver.Sum(x[k, i, j] * dist_matrix[i][j] for k in range(num_robots) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)
solver.Minimize(objective)

# Solve
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Total cost of all tours:', solver.Objective().Value())
    for k in range(num_robots):
        tour = []
        current_location = depots[k]
        while True:
            for j in range(len(coordinates)):
                if j != current_location and x[k, current_location, j].solution_value() > 0:
                    tour.append(current_location)
                    current_location = j
                    break
            if current_location == depots[k]:
                tour.append(current_location)  # complete the tour
                break
        tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        print(f'Robot {k} Tour: {tour}')
        print(f'Robot {k} Total Travel Cost: {tour}}')
else:
    print('The problem does not have an optimal solution.')