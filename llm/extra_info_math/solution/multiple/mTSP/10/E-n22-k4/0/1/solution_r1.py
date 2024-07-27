# Create the MILP solver
solver = pywraptp.lp_solve('MILP')

# Variables
x = {}
u = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:  # No loops
            for k in range(num_robots):
                x[i, j, k] = solver.BoolVar(f'x[{i},{j},{k}]')

# Position in the tour to break subtours
for i in range(1, num_cities):
    u[i] = solver.IntVar(0, num_cities-1, f'u[{i}]')

# Objective: Minimize distance
objective_terms = []
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            for k in range(num_robots):
                objective_terms.append(distances[i][j] * x[i, j, k])
solver.Minimize(solver.Sum(objective_terms))

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, num_cities):
    solver.Add(solver.Sum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1)

# Each robot leaves each city exactly once and enter exactly once
for k in range(num_robots):
    for p in range(num_cities):
        solver.Add(solver.Sum(x[p, j, k] for j in range(num_cities) if p != j) ==
                   solver.Sum(x[i, p, k] for i in range(num_cities) if i != p))

# Each robot leaves from and returns to the depot
for k in range(num_robots):
    solver.Add(solver.Sum(x[0, j, k] for j in range(1, num_cities)) == 1)
    solver.Add(solver.Sum(x[i, 0, k] for i in range(1, num_cities)) == 1)

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                solver.Add(u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1)

# Solve the problem
status = solver.Solve()

# If solution is found, display tours for each robot
if status == pywraptp.Solver.OPIMAL:
    for k in range(num_robots):
        tour = [0]
        current_pos = 0
        while True:
            next_pos = next(j for j in range(num_cities) if x[current_pos, j, k].solution_value() == 1)
            if next_pos == 0:
                break
            tour.append(next_pos)
            current_pos = next_pos
        tour.append(0)  # return to depot
        print(f'Robot {k} Tour: {tour}')
        tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        print(f'Robot {k} Total Travel Cost: {tour_cost}')
else:
    print("The solver did not find an optimal solution.")