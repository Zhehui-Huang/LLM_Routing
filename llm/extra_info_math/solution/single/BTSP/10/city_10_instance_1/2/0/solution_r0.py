import pulp
import math

# Coordinate data for each city including the depot city 0
coordinates = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

def euclidean_distance(coord1, coord2):
    # Calculates Euclidean distance between two coordinates
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Number of cities including the depot
n = len(coordinates)

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = pulp.LpProblem("Minimax_Traveling_Salesman", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", [i for i in range(n)], lowBound=0, upBound=n, cat='Continuous')

# The big M for sub-tour elimination constraints
M = 1000

# Objective: minimize the maximum distance between consecutive cities
z = pulp.LpVariable("z", lowBound=0)
problem += z

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave each city only once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter each city only once
    
# Sub-tour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n*x[i, j] <= n-1

# Bounding z by the distances
for i in range(n):
    for j in range(n):
        if i != j:
            problem += z >= distance_matrix[i][j] * x[i, j]

# Solve the problem
status = problem.solve()
print("Status:", pulp.LpStatus[status])

# Parse the result
tour = [0]
for _ in range(1, n):
    for j in range(n):
        if j != tour[-1] and pulp.value(x[tour[-1], j]) == 1:
            tour.append(j)
            break

# Ensuring to return back to the start
tour.append(0)

# Calculating total cost and maximum distance
total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)