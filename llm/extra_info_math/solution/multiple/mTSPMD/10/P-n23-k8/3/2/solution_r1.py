from math import sqrt
from ortools.linear_solver import pywraplp

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Function to calculate Euclidean distance
def calculate_distance(pt1, pt2):
    return sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Number of robots (each starts at a depot)
num_robots = 8

# Distance matrix
num_cities = len(coordinates)
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create the solver
solver = pywraplp.Solver.CreateSolver('CBC')

# Variables
x = {}
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x[k, i, j] = solver.BoolVar(f'x[{k},{i},{j}]')

u = {i: solver.IntVar(1.0, num_cities - 1, f'u[{i}]') for i in range(num_cities)}

# Constraint: Enter each city once and leave once
for j in range(8, num_cities):
    solver.Add(sum(x[k, i, j] for k in range(num_robots) for i in range(num_cities) if i != j) == 1)
    solver.Add(sum(x[k, j, i] for k in range(num_robots) for i in range(num_cities) if i != j) == 1)

# Constraint: Each robot leaves and enters its depot
for k in range(num_robots):
    solver.Add(sum(x[k, k, j] for j in range(num_cities) if j != k) == 1)
    solver.Add(sum(x[k, j, k] for j in range(num_cities) if j != k) == 1)

# Subtour prevention
for k in range(num_robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                solver.Add(u[i] - u[j] + (num_cities + 1) * x[k, i, j] <= num_cities)

# Objective Function: Minimize the total distance travelled
objective = solver.Sum(distance_matrix[i][j] * x[k, i, j] for k in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j)
solver.Minimize(objective)

# Solving the problem
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    total_distance = solver.Objective().Value()
    print(f'Total cost of all tours: {total_distance}')
    for k in range(num_robots):
        tour = [k]
        next_location = k
        while True:
            for j in range(num_cities):
                if j != next_location and x[k, next_location, j].solution_value() > 0.5:
                    tour.append(j)
                    next_location = j
                    break
            if next_location == k:
                break
        tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        print(f'Robot {k} Tour: {tour}')
        print(f'Robot {k} Total Travel Cost: {tour_cost}')
else:
    print("The problem does not have an optimal solution.")