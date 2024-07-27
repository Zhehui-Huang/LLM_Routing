from ortools.linear_solver import pywraplp
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def traveling_salesman_problem(coordinates):
    n = len(coordinates)
    distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]
    
    # Create the solver
    solver = pywraplp.Solver.CreateSolver('CBC')
    
    # Ensure solver is available
    if not solver:
        return None, "Failed to create solver. Make sure the solver backend is available."
    
    # Binary variables
    x = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                x[i, j] = solver.BoolVar(f'x[{i},{j}]')
    
    # Objective Function: Minimize the total distance.
    solver.Minimize(solver.Sum(x[i, j] * distances[i][j] for i in range(n) for j in range(n) if i != j))
    
    # Constraints
    # Each city should be left exactly once
    for i in range(n):
        solver.Add(solver.Sum(x[i, j] for j in range(n) if i != j) == 1)
    
    # Each city should be entered exactly once
    for j in range(n):
        solver.Add(solver.Sum(x[i, j] for i in range(n) if i != j) == 1)
    
    # Subtour elimination constraints
    u = [solver.IntVar(0, n - 1, 'u[%i]' % i) for i in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                solver.Add(u[i] - u[j] + n * x[i, j] <= n - 1)
    
    # Solve the model
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        tour = [0]
        current = 0
        for _ in range(1, n):
            for j in range(n):
                if j != current and x[current, j].solution_value() > 0.5:
                    tour.append(j)
                    current = j
                    break
        tour.append(0)  # return to the starting city
    
        total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        return tour, total_cost
    else:
        return None, "Solver could not find an optimal solution."

# Coordinates of cities including the depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

tour, result = traveling_salesman_problem(coordinates)

if tour:
    print(f"Tour: {tour}")
    print(f"Total travel cost: {round(result)}")
else:
    print(result)