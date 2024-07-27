import pulp
import math

# Coordinates of the cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Total number of cities including the depot
n = len(coordinates)

# Number of robots (salesmen)
m = 4

# Indices of the cities without the depot
cities = list(range(1, n))

# Calculate the Euclidean distance between two points
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Creating the cost dictionary
costs = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
problem = pulp.LpProblem("VRPTW", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts('u', (i for i in range(1, n)), 0, n-1, pulp.LpContinuous)

# Objective function
objective = pulp.lpSum(costs[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in range(m))
problem += objective

# Constraints
# Each city is visited exactly once by one robot
for j in cities:
    problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Each robot leaves each city at most once
for k in range(m):
    for i in range(n):
        problem += pulp.lpSum(x[i, j, k] for j in range(n) if i != j) == pulp.lpSum(x[j, i, k] for j in range(n) if i != j)

# Each robot leaves the depot exactly once and returns once
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in cities) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in cities) == 1

# Subtour elimination constraints
for i in cities:
    for j in cities:
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
problem.solve()

# Verify if the problem is solved
if pulp.LpStatus[problem.status] == 'Optimal':
    print('Found optimal solution')
else:
    print(f'Solution status: {pulp.LpStatus[problem.status]}')

total_travel_cost = 0  # To track the sum of all costs

for k in range(m):
    tour = [0]
    current_position = 0
    for _ in range(n-1):  # Visiting n-1 cities
        for j in range(n):
            if j != current_position and x[current_position, j, k].varValue == 1:
                tour.append(j)
                total_travel_cost += costs[current_position, j]
                current_position = j
                break
    tour.append(0)  # Return to the depot
    if len(tour) > 2:  # If the robot actually moves
        robot_tour_cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour)-1))
        print(f'Robot {k} Tour: {tour}')
        print(f'Robot {k} Total Travel Cost: {robot_tour_cost}')
        
print(f'Overall Total Travel Cost: {total_travel_cost}')