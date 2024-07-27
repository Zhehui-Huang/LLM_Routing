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
        if i != j:
            distances[i, j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distances[i, j] = float('inf')  # Infinite cost to travel from the city to itself

# Initialize solver
solver = pywraplp.Solver.CreateSolver('SCIP')

# Create variables x[i, j] for i != j
x = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            x[i, j] = solver.BoolVar(f'x[{i},{j}]')

# Objective: Minimize the maximum distance in the tour
solver.Minimize(solver.Max([x[i, j] * distances[i, j] for i in range(num_cities) for j in range(num_cities) if i != j]))

# Each city must be left once and visited once
for i in range(num_cities):
    solver.Add(sum(x[i, j] for j in range(num_cities) if i != j) == 1)
    solver.Add(sum(x[j, i] for j in range(num_cities) if i != j) == 1)

# Subtour elimination
# Use a common trick for subtour elimination by adding additional constraints
for i in range(num_cities):
    for j in range(1, num_cities):
        if i != j:
            sub_tour = [k for k in range(num_cities) if k != i and k != j]
            num_sub = len(sub_tour)
            if num_sub > 1:
                solver.Add(
                    solver.Sum(x[k, l] for k in sub_tour for l in sub_tour if k != l) <= num_sub - 1
                )

# Solve the problem
status = solver.Solve()

# Fetch the results
tour = []
if status == pywraplp.Solver.OPTIMAL:
    # Create tour list starting from the depot
    current_city = 0
    tour.append(current_city)
    while len(tour) < num_cities:
        for j in range(num_cities):
            if current_city != j and x[current_city, j].solution_value() == 1:
                tour.append(j)
                current_city = j
                break
    tour.append(0)  # coming back to depot

    # Calculate the total and maximum distances
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distances[tour[i], tour[i + 1]]
        total_distance += dist
        if dist > max_distance:
            max_distance = dist

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("The problem does not have an optimal solution.")