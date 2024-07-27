import pulp
import math

# City coordinates
coords = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

# Calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Number of cities
n = len(coords)

# Distance matrix
cost = [[distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Define problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
problem += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave city i once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter city i once

# Subtour elimination using additional constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Validate solution and extract results
if status == pulp.LpStatusOptimal:
    # Extract tour
    tour = []
    next_city = 0
    for _ in range(n):
        tour.append(next_city)
        next_city = next(j for j in range(n) if pulp.value(x[next_city, j]) == 1)
    tour.append(0)  # Return to depot
    
    # Calculate total travel cost
    total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    # Output result
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("An optimal solution could not be found.")