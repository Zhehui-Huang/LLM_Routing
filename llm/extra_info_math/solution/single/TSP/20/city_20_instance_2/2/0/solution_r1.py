import math
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, LpStatus

# Define city coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Number of cities
n = len(coordinates)

# Distance matrix calculation
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create matrix
distance_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setup problem
problem = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=LpBinary)

# Objective
problem += lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += lpSum(x[i, j] for j in range(n) if i != j) == 1  # leaving city i
    problem += lpSum(x[j, i] for j in range(n) if i != j) == 1  # entering city i

# Subtour elimination
for i in range(n):
    for j in range(i + 1, n):
        problem += x[i, j] + x[j, i] <= 1

# Solve the problem
status = problem.solve()

# Check if the problem is solved
if LpStatus[status] == 'Optimal':
    solution = []
    for i in range(n):
        for j in range(n):
            if i != j and x[i, j].varValue == 1:
                solution.append((i, j))

    # Extract the tour from the solution
    tour = []
    current = 0  # start at depot
    while len(tour) < n:
        tour.append(current)
        next_city = next(j for i, j in solution if i == current)
        current = next_city
        solution = [(i, j) for i, j in solution if i != current]

    # Return to the start
    tour.append(0)
    
    # Calculate the total distance
    total_distance = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("No optimal solution found.")