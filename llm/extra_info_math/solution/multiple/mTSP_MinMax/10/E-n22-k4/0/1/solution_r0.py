from pulp import *
import math

# Constants
num_robots = 4
num_cities = 22
depot_city = 0

# Coordinates of cities including depot city
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
               (155, 185), (139, 182)]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Define the model
model = LpProblem("mTSP", LpMinimize)

# Create decision variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) 
                           for j in range(num_cities) 
                           for k in range(num_robots)], cat='Binary')

u = LpVariable.dicts("u", [i for i in range(num_cities)], lowBound=0)

# Objective to minimize
model += lpMax([lpSum([distance(i, j) * x[i, j, k] for i in range(num_cities) for j in range(num_cities)]) for k in range(num_robots)])

# Constraints
for j in range(1, num_cities):
    model += lpSum([x[i, j, k] for i in range(num_cities) for k in range(num_robots)]) == 1  # Visit each city exactly once

for k in range(num_robots):
    for i in range(1, num_cities):  # Flow conservation
        model += lpSum([x[i, j, k] for j in range(num_cities)]) == lpSum([x[j, i, k] for j in range(num_cities)])

    model += lpSum([x[depot_city, j, k] for j in range(num_cities) if j != depot_city]) == 1  # Leaving depot
    model += lpSum([x[j, depot_city, k] for j in range(num_cities) if j != depot_city]) == 1  # Returning to depot

for k in range(num_robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                model += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Solve the model
model.solve()

# Results extraction and printing
max_cost = 0
for k in range(num_robots):
    tour = []
    costs = 0
    current_city = depot_city
    visited = [current_city]
    while True:
        next_city = None
        for j in range(num_cities):
            if x[current_city, j, k].varValue == 1:
                next_city = j
                break
        if next_city == depot_city:
            tour.append(depot_city)
            break
        tour.append(next_city)
        costs += distance(current_city, next_city)
        current_city = next_city
        visited.append(current_city)
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {costs}")

    if costs > max_cost:
        max_cost = costs

print("Maximum Travel Cost:", max_cost)