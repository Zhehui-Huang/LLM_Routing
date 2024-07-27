import pulp
import math

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Number of robots and cities
num_robots = 4
num_cities = len(coordinates)

# Problem instance
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinize)

# Variables
x = {}
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                x[(i, j, k)] = pulp.LpVariable(f"x_{i}_{j}_{k}", 0, 1, pulp.LpBinary)

u = {}
for j in range(1, num_cities):
    u[j] = pulp.LpVariable(f"u_{j}", 0, num_cities - 1, pulp.LpContinuous)

# Objective Function
problem += pulp.lpSum(euclidean_distance(coordinates[i], coordinates[j]) * x[i, j, k] 
                      for k in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each non-depot city visited exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for k in range(num_robots) for i in range(num_cities) if i != j) == 1

# Enter and leave for each robot
for k in range(num_robots):
    for j in range(num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) == \
                   pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j)

# Depot constraints
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Subtour Elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            problem += (u[i] - u[j] + (num_cities - 1) * pulp.lpSum(x[i, j, k] for k in range(num_robots))) <= num_cities - 2

# Solve the problem
problem.solve()

# Output
print("Status:", pulp.LpStatus[problem.status])

overall_cost = 0
for k in range(num_robots):
    tour = [0]
    costs = 0
    current_city = 0
    while True:
        next_city = None
        for j in range(num_cities):
            if x[(current_city, j, k)].varValue == 1:
                next_city = j
                break
        if next_city == 0:
            tour.append(next_city)
            break
        tour.append(next_city)
        current_city = next_city
    for i in range(len(tour) - 1):
        costs += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    print(f'Robot {k} Tour: {tour}')
    print(f'Robot {k} Total Travel Cost: {costs}')
    overall_cost += costs

print(f'Overall Total Travel Cost: {overall_cost}')