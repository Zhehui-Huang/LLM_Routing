import pulp
from math import sqrt
import itertools

# Coordinates of cities (depot + cities 1 to 9)
coordinates = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Number of cities (including the depot)
n = len(coordinates)

# Euclidean distance
def euclidean_dist(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Create a cost matrix
cost_matrix = [[euclidean_inputs(i, j) for j in range(n)] for i in range(n)]

# Define the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(cost_matrix[i][j] * x[i,j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leaving city i
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # entering city i

# Solve the problem
solver = pulp.getSolver('PULP_CBC_CMD', msg = 1)
model.solve(solver)

# Get the tour
tour = [0]
for i in range(n - 1):
    next_cities = [j for j in range(n) if j != tour[-1] and pulp.value(x[tour[-1], j]) == 1]
    if next_cities:
        tour.append(next_cities[0])

# Ensure to return to the depot
tour.append(0)

# Calculate the cost of the tour
total_travel_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")