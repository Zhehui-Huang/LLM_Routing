from ortools.linear_solver import pywraplp
import numpy as np

# Cities coordinates
cities_coord = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Compute the Euclidean distance matrix
distances = np.sqrt(((np.array(cities_coord)[:, None] - np.array(cities_coord)[None, :])**2).sum(axis=2))

# Parameters
num_cities = len(cities_coord)
num_robots = 4

# Solver
solver = pywraplp.Solver.CreateSolver('CBC')

# Variables
x = {}
u = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            for k in range(num_robots):
                x[i, j, k] = solver.BoolVar(f'x[{i},{j},{k}]')

for i in range(1, num_cities):
    u[i] = solver.IntVar(0, num_cities-1, f'u[{i}]')

# Objective
solver.Minimize(solver.Sum(distances[i][j] * x[i, j, k] for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots)))

# Constraints
# Each city except depot visited exactly once by any robot
for j in range(1, num_cities):
    solver.Add(solver.Sum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1)

# Leave each city only once
for k in range(num_robots):
    for i in range(num_cities):
        solver.Add(solver.Sum(x[i, j, k] for j in range(num_cities) if i != j) == solver.Sum(x[j, i, k] for j in range(num_cities) if i != j))

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                solver.Add(u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1)

# Solve the model
status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    total_cost = 0
    for k in range(num_robots):
        tour = []
        for i in range(num_cities):
            for j in range(num_cities):
                if i != j and x[i, j, k].solution_value() > 0.5:
                    tour.append((i, j))
        # Extract the ordered tour
        ordered_tour = [0]
        while len(tour) > 0:
            for i, link in enumerate(tour):
                if link[0] == ordered_tour[-1]:
                    ordered_t,our.append(link[1])
                    tour.pop(i)
                    break
        ordered_tour.append(0)  # Return to depot
        tour_cost = sum(distances[ordered_tour[n]][ordered_tour[n+1]] for n in range(len(ordered_tour)-1))
        total_cost += tour_cost
        print(f"Robot {k} Tour: {ordered_tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("The problem does not have an optimal solution.")