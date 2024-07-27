import pulp
import math
import itertools

# City coordinates
coordinates = [
    (90, 3),  # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Number of cities
n = len(coordinates)

# Euclidean distance calculation
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i, j] = 0

# Problem definition
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function: minimize the maximum distance
prob += max_distance

# Constraints
# Leave each city once
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Enter each city once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Maximum distance constraint
for i, j in distance_matrix.keys():
    prob += x[i, j] * distance_matrix[i, j] <= max_distance

# Solve
solver = pulp.PULP_CBC_CMD()
prob.solve(solver)

# Extract tour
tour = []
current_city = 0
tour.append(current_city)

for _ in range(1, n):
    next_city = next(j for i, j in x.keys() if i == current_city and pulp.value(x[(i, j)]) == 1)
    tour.append(next_city)
    current_city = next_city

# Close the loop
tour.append(tour[0])

# Calculate the total cost and maximum cost
total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_step_cost = max(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Outputs
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_step_cost)