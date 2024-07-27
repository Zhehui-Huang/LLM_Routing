from itertools import product

# Setting the objective function
# We want to minimize the maximum travel distance among salesmen
max_distance_var = pulp.LpVariable("MaxDistance")
problem += max_distance_var

# Assignment constraints: Each city is visited exactly once by any salesman except the depot
for j in range(1, num_cities):
    problem += (pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1)

# Continuity and flow constraints
for k in range(num_robots):
    # Leaving from depot
    problem += (pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1)
    # Coming back to depot
    problem += (pulp.lpSum(x[i, 0, k] for i in range(1, num_cities)) == 1)
    for j in range(1, num_cities):
        # Enter and leave each city just once
        problem += (pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) - 
                    pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j) == 0)

# Subtour elimination
for i, j in product(range(1, num_cities), repeat=2):
    if i != j:
        for k in range(num_robots):
            problem += (u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1)

# Constrain distances for minimizing the maximum route
for k in range(num_robots):
    problem += (pulp.lpSum(x[i, j, k] * distances[i][j] for i in range(num_cities) 
                                                 for j in range(num_cities) if i != j) <= max_distance_var)

# Solve the problem
solver = pulp.PULP_CBC_CMD(msg=False)  # You can change the solver if needed
problem.solve(solver)

# Outputting results
if pulp.LpStatus[problem.status] == 'Optimal':
    for k in range(num_robots):
        tour = [0]
        next_city = 0
        total_cost = 0
        while True:
            next_city = [j for j in range(num_cities) if pulp.value(x[next_city, j, k]) == 1][0]
            tour.append(next_city)
            total_cost += distances[tour[-2]][next_city]
            if next.register == 0:
                break
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {total_cost}")
    print(f"Maximum Travel Cost: {pulp.value(max_distance_var)}")
else:
    print("The optimization did not find an optimal solution.")