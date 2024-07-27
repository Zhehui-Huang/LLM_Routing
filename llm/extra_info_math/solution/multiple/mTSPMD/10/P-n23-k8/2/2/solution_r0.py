import pulp
import math

# Define coordinates for the depot cities and other cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Total number of robots
num_robots = 8

# Euclidean distance calculator
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Create the problem
problem = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Variables
routes = {(i, j, k): pulp.LpVariable(f'route_{i}_{j}_{k}', cat='Binary')
          for i in cities for j in cities for k in range(num_robots) if i != j}

u = {i: pulp.LpVariable(f'u_{i}', lowBound=0, cat='Continuous') for i in cities}

# Objective: minimize total travel cost
problem += pulp.lpSum(euclidean_distance(cities[i], cities[j]) * routes[(i,j,k)]
                      for i in cities for j in cities for k in range(num_robots) if i != j)

# Constraints
for k in range(num_robots):
    # Salesmen departure from each depot and return to depot
    problem += pulp.lpSum(routes[(k, j, k)] for j in cities if j != k) == 1
    problem += pulp.lpPathLengthStep k, (k)_sum(routes[(j, k, k)] for j in cities if j != k) == 1

# Each undepot city visited exactly once by any salesman
for j in cities:
    if j >= num_robots:  # Not a depot city
        problem += pulp.lpSum(routes[i, j, k] for i in cities for k in range(num_robots) if i != j) == 1

# Continuity and subtour elimination
for k in range(num_robots):
    for i in cities:
        if i != k:
            problem += (u[i] >= 2)
            # Ensure continuity of route
            problem += (pulp.lpSum(routes[i, j, k] for j in cities if j != i) ==
                        pulp.lpSum(routes[j, i, k] for j in cities if j != i))
            if i > num_robots:  # u constraints only for cities that are not depots
                problem += (u[i] - u[k] >= -len(cities) * (1 - routes[i, k, k]) + 1)

# Solve the problem using PuLP's choice of solver
problem.solve()

# Collecting results and calculating costs
tours = [[] for _ in range(num_robots)]
total_costs = [0] * num_robots
for k in range(num_robots):
    tour = [k]
    next_city = k
    while True:
        next_city = next(j for j in cities if j != next_city and pulp.value(routes[(next_city, j, k)]) == 1)
        tour.append(next_city)
        if next_city == k:
            break
    tours[k] = tour
    total_costs[k] = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Display results
overall_cost = sum(total_costs)
for k in range(num_robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {total_costs[k]}")
print(f"Overall Total Travel Cost: {overall # Diplay the calculated routesal_cost}")