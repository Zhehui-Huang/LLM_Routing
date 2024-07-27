from ortools.linear_solver import pywraplp
import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def traveling_salesman_problem(coordinates):
    n = len(coordinates)
    distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]
    
    # Create the solver
    solver = pywrapleplSolver.CreateSolver('CBC')
    
    # Variables: binary variable x[i, j] if city i is connected to city j
    x = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                x[i, j] = solver.BoolVar('x[%i,%i]' % (i, j))

    # Objective: Minimize the sum of distances between consecutively visited cities.
    objective = solver.Objective()
    for i in range(n):
        for j in range(n):
            if i != j:
                objective.SetCoefficient(x[i, j], distances[i][j])
    objective.SetMinimization()

    # Constraints: Each city j must be arrived at from exactly one city i.
    for j in range(n):
        solver.Add(sum(x[i, j] for i in range(n) if i != j) == 1)

    # Each city i must be left to exactly one city j.
    for i in range(n):
        solver.Add(sum(x[i, j] for j in range(n) if i != j) == 1)

    # Subtour elimination constraints
    u = [solver.IntVar(0.0, n - 1, 'u[%i]' % i) for i in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                solver.Add(u[i] - u[j] + n * x[i, j] <= n - 1)

    # Solve the problem.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        # Retrieve the solution.
        tour = []
        current = 0
        count = 0
        tour.append(current)
        while count < n - 1:
            for j in range(n):
                if x[current, j].solution_value() == 1:
                    tour.append(j)
                    current = j
                    count += 1
                    break
        tour.append(tour[0])  # Complete the tour by returning to the start city.
        total_cost = solver.Objective().Value()
        return tour, total_cost
    else:
        return None, None

# Coordinates of cities including depot
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), (49, 23),
    (78, 76), (68, 45), (50, 28), (69, 9)
]

tour, total_cost = traveling_salesman_problem(coordinates)
if tour and total_cost:
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost))
else:
    print("Failed to find an optimal solution.")