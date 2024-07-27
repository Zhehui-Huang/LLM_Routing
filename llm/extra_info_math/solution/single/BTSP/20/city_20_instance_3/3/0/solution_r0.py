import math
import pulp

# Define the coordinates of the cities
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

n = len(city_coords)  # Number of cities

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclidean_distance(city_coords[i], city_coords[j])

# Define the problem
model = pulp.LpProblem("Minimize_Max_Distance_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)
d_max = pulp.LpVariable("d_max", lowBound=0, cat=pulp.LpContinuous)

# Objective: Minimize the maximum distance in the tour
model += d_max

# Constraints

# Each city must be left exactly once
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Each city must be entered exactly once
for j in range(n):
    model += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Subtour elimination (MTZ constraints)
u = pulp.LpVariable.dicts("u", [i for i in range(n)], lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Constraint to ensure d_max is the maximum distance between consecutive cities
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[(i, j)] * x[(i, j)] <= d_max

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the solution
tour = []
current_location = 0
while len(tour) < n:
    tour.append(current_location)
    next_locations = [j for j in range(n) if j != current_location and pulp.value(x[(current_location, j)]) == 1]
    if next_locations:
        current_location = next_locations[0]
tour.append(0)  # Returning to the depot

# Calculate total travel cost and max distance
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(n))
max_distance = max(distances[(tour[i], tour[i+1])] for i in range(n))

# Output
output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

output