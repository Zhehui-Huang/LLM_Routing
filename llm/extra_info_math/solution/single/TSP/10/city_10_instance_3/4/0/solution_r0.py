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
problem += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave city i once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter city i once

# Subtour elimination
for m in range(2, n):
    for S in itertools.combinations(range(1, n), m):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = problem.solve()

# Check if a valid solution has been found
if status == pulp.LpStatusOptimal:
    # Extract tour
    tour = []
    active = 0
    while len(tour) < n:
        for j in range(n):
            if pulp.value(x[active, j]) == 1:
                tour.append(active)
                active = j
                break
    tour.append(0)  # Return to depot
    
    # Calculate total travel cost
    total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    # Output result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("An optimal solution could not be found.")