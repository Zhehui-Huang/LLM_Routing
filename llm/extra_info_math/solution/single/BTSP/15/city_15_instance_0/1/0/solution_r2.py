import numpy as np
from ortools.linear_solver import pywraplp

# Coordinates of the cities, depot is at index 0
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
    (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

num_cities = len(coordinates)

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Initialize solver
solver = pywraplp.Solver.CreateSolver('SCIP')

# Decision variables
x = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            x[i, j] = solver.BoolVar(f'x[{i},{j}]')

# Objective variable (maximum distance between consecutive cities)
max_distance = solver.NumVar(0, solver.infinity(), 'max_distance')
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            solver.Add(x[i, j] * distances[i, j] <= max_distance)
solver.Minimize(max_distance)

# Each city must begin and end exactly once
for i in range(num_cities):
    solver.Add(sum(x[i, j] for j in range(num_cities) if i != j) == 1)
    solver.Add(sum(x[j, i] for i in range(num_cities) if i != j) == 1)

# Subtour elimination using constraints
u = [solver.NumVar(0, num_cities - 1, f'u[{i}]') for i in range(num_cities)]
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            solver.Add(u[i] - u[j] + num_cities * x[i, j] <= num_cities - 1)

# Solve the model
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    tour = []
    current_city = 0
    next_city = None

    for _ in range(num_cities):
        tour.append(current_city)
        for j in range(num_cities):
            if current_city != j and x[current_city, j].solution_value() > 0.5:
                next_city = j
                break
        current_city = next_city
    
    tour.append(tour[0])  # Close the tour by returning to the depot
    
    # Calculate the total travel cost and maximum distance
    total_distance = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    max_dist_consecutive = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist_consecutive:.2f}")
else:
    print("The problem does not have an optimal solution.")