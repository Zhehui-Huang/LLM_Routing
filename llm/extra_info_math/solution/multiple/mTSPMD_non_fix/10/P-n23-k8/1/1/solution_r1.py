import math
from pulp import *

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Calculate Euclidean distances between cities
def euclidean(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

num_cities = len(coordinates)
cost_matrix = {
    (i, j): euclidean(coordinates[i], coordinates[j])
    for i in range(num_cities)
    for j in range(num_cities)
    if i != j
}

# Model setup
prob = LpProblem("VRP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j) for i in range(num_cities) for j in range(num_cities) if i != j], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(num_cities), lowBound=0, cat=LpContinuous)

# Objective function
prob += lpSum(cost_matrix[i, j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Subtour elimination
for i in range(num_cities):
    for j in range(1, num_cities):
        if i != j:
            prob += u[i] - u[j] + num_cities * x[i, j] <= num_cities - 1

# Only one departure from each city
for i in range(num_cities):
    prob += lpSum(x[i, j] for j in range(num_cities) if i != j) == 1

# Only one arrival to each city
for j in range(num_cities):
    prob += lpSum(x[i, j] for i in range(num_cities) if i != j) == 1

# Solve problem
prob.solve()

# Output results
overall_travel_cost = 0
for robot in range(num_robots):
    print(f"Robot {robot} Tour: ", end='')
    current_city = depot
    tour = [current_city]
    traveled_cost = 0
    while True:
        found = False
        for j in range(num_cities):
            if pulp.value(x[current_city, j]) == 1:
                tour.append(j)
                traveled_cost += cost_matrix[current_city, j]
                current_city = j
                found = True
                break
        if not found or current_city == depot:
            break
    print(tour)
    print(f"Robot {robot} Total Travel Cost: {traveled_cost}")
    overall_travel_cost += traveled_cost

print(f"Overall Total Travel Cost: {overall_travel_cost}")