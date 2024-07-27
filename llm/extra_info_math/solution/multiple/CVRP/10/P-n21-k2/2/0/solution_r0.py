import pulp
import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Problem parameters
num_cities = len(coordinates)
vehicle_capacity = 160
num_vehicles = 2
depot = 0

# Distance calculation
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create the distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create the LP problem
problem = pulp.LpProblem("CVRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(v, i, j) for v in range(num_vehicles) for i in range(num_cities) for j in range(num_cities)], cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[v, i, j] for v in range(num_vehicles) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for j in range(1, num_cities):
    problem += pulp.lpSum(x[v, i, j] for v in range(num_vehicles) for i in range(num_cities) if i != j) == 1 # each city visited exactly once

for v in range(num_vehicles):
    problem += pulp.lpSum(x[v, depot, j] for j in range(1, num_cities)) == 1 # each vehicle leaves depot exactly once

for v in range(num_vehicles):
    for j in range(num_cities):
        problem += pulp.lpSum(x[v, i, j] for i in range(num_cities) if i != j) == pulp.lpSum(x[v, j, k] for k in range(num_cities) if k != j) # flow conservation

for v in range(num_vehicles):
    problem += pulp.lpSum(demands[j] * x[v, i, j] for i in range(num_cities) for j in range(num_cities) if i != j) <= vehicle_capacity # capacity constraints

# Solve the problem
problem.solve()

# Output results
total_travel_cost = 0
for v in range(num_vehicles):
    tour = [depot]
    next_location = depot
    travel_cost = 0
    while True:
        next_locations = [(j, distance_matrix[next_location][j]) for j in range(num_cities) if pulp.value(x[v, next_location, j]) == 1]
        if not next_locations:
            break
        next_location, cost = next_locations[0]
        tour.append(next_location)
        travel_cost += cost
        if next_location == depot:
            break
    print(f"Robot {v} Tour: {tour}")
    print(f"Robot {v} Total Travel Cost: {travel_cost:.2f}")
    total_travel_cost += travel_cost

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")