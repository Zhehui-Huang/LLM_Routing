import math
import pulp

# Coordinates of the cities including the depot
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

n = len(city_coords)  # Number of cities

# Euclidean distance function
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distances = {(i, j): euclidean_distance(city_coords[i], city_coords[j]) for i in range(n) for j in range(n) if i != j}

# Define the optimization model
model = pulp.LpProblem("Minimize_Max_Distance_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)
d_max = pulp.LpVariable("d_max", lowBound=0, cat=pulp.LpContinuous)

# Objective function
model += d_max

# Constraints
# Ensure every city is entered and left exactly once
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[(i, j)] * distances[(i, j)] <= d_max

# Prevent sub-tours using MTZ constraints
u = pulp.Lers("u", lowBound=0, upBound=n-1, cat=pulp.LpContinuous)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[(i, j)] <= n - 2

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the route from the solution
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    current_city = next_cities[0]

# Ensure tour is closed
if tour[0] != tour[-1]:
    tour.append(tour[0])

# Calculate total and maximum distance in the tour
total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour)-1))
max_distance = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour)-1))

# Prepare the results
result = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_distance
}

print(result)