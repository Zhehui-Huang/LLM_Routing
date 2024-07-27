import pulp
import math

# City coordinates
coordinates = [
    (29, 51), # Depot city 0
    (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43),
    (17, 36), (4, 60), (78, 82), (83, 96),
    (60, 50), (98, 1)
]

# Number of cities
n = len(coordinates)

# Euclidean distance calculator
def euclidean(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix
c = [[euclidean(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Solve TSP using PuLP
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 
                          lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective function to minimize
problem += pulp.lpSum(c[i][j] * x[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # Leave each city once
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # Enter each city once

# Subtour elimination
for k in range(2, n+1):
    for S in itertools.combinations(range(1, n), k):
        problem += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S)-1

# Solve the problem
problem.solve()

# Extract the solution
tour = []
current_city = 0
for _ in range(n):
    next_city = next(j for j in range(n) if x[(current_city, j)].varValue == 1)
    tour.append(next_city)
    current_city = next_city

# Close the tour
tour.append(0)

# Calculate the total cost of the tour
total_travel_cost = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel';

# Adjust indentation or wrap into a function if reusing or testing in different environment