import pulp
import math

# Define coordinates of cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

num_cities = len(coordinates)
robots = 4

# Calculate Euclidean distance between each pair of points
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Create the problem instance
problem = pulp.LpProblem("Multi_Robot_TSP", pulp.LpMinimize)

# Define problem variables
x = pulp.LpVariable.dicts("x",
                          ((i, j, k) for k in range(robots) for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat='Binary')

u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Define the objective function: Minimize the maximum travel distance by any robot
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Add constraints
# Constraint (1): Each city is visited exactly once by one salesman
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for k in range(robots) for i in range(num_cities) if i != j) == 1

# Constraint (2) and (3): Each robot starts and ends at the depot
for k in range(robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Constraint (4): Subtour elimination
for k in range(robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Constraint (5): Travel distance must not exceed the maximum
for k in range(robots):
    problem += pulp.lpSum(x[i, j, k] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j) <= max_distance

# Solve the problem
problem.solve()

# Output the results
if pulp.LpStatus[problem.status] == 'Optimal':
    print(f"Optimal solution found with the maximum path length: {max_distance.varValue}")
    for k in range(robots):
        route = [0]
        while True:
            next_city = next(j for j in range(num_cities) if pulp.value(x[route[-1], j, k]) == 1)
            if next_city == 0:
                break
            route.append(next_city)
        route.append(0)
        tour_cost = sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route) - 1))
        print(f"Robot {k} Tour: {route}")
        print(f"Robot {k} Tour Cost: {tour_cost}")
else:
    print("Solution not found.")