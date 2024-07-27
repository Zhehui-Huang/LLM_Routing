import pulp
import math
import itertools

# Coordinates of each city including the depot city
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), 
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Number of cities including the depot
n = len(coordinates)

# Calculate Euclidean distance between two cities
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
dist_matrix = [[calc_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat="Binary")

# Variable for the maximum distance in the tour
d_max = pulp.LpVariable("d_max", lowBound=0, cat="Continuous")

# Objective Function
problem += d_max

# Constraints
# Each city must be left and visited exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination using constraints
for S in range(2, n):  # From 2 to n-1, all subsets of the set of nodes except the depot
    for subset in itertools.combinations(range(1, n), S):
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * dist_matrix[i][j] <= d_max

# Solve the problem using the default solver
status = problem.solve()

# Output results
tour = [0]
for _ in range(n-1):
    for j in range(n):
        if j != tour[-1] and pulp.value(x[tour[-1], j]) == 1:
            tour.append(j)
            break
tour.append(0)  # Return to the depot

# Calculate total travel cost and maximum distance
total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_dist = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")