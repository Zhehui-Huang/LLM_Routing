import pulp
import math
from itertools import combinations

# Define the cities and their coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Number of cities
num_cities = len(coordinates)

# Calculate the Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create the cost matrix
cost_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities)), cat='Binary')

# Objective Function
prob += pulp.lpSum(cost_matrix[i][j] * x[i][j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for i in range(num_cities):
    prob += pulp.lpSum(x[i][j] for j in range(num_cities) if i != j) == 1
    prob += pulp.lpSum(x[j][i] for j in range(num_cities) if i != j) == 1

for i, j in combinations(range(1, num_cities), 2):
    prob += x[i][j] + x[j][i] <= 1

# Solve the problem
status = prob.solve()
print(f"Status: {pulp.LpStatus[status]}")

# Retrieve the tour
tour = []
visited = [0]
while len(visited) < num_cities:
    for j in range(num_cities):
        if pulp.value(x[visited[-1]][j]) == 1:
            visited.append(j)
            break
tour = visited + [0]  # complete the tour by returning to the depot

# Calculate total travel cost
total_cost = sum(cost_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")