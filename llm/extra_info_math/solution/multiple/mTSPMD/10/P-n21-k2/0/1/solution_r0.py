import pulp
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Create the distance matrix
num_cities = len(cities_coords)
distance_matrix = [[calculate_distance(cities_coords[i], cities_coords[j]) for j in range(num_cities)] for i in range(num_cities)]

depots = [0, 1]
robots = len(depots)

# Create the problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables x_ijk
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in depots], 0, 1, pulp.LpBinary)

# Objective Function
prob += pulp.lpSum(distance_matrix[i][j] * x[(i, j, k)] for i in range(num_cities) for j in range(num_cities) for k in depots)

# Constraints
# Each node is visited once and exactly once
for j in range(1, num_cities):
    prob += pulp.lpSum(x[(i, j, k)] for i in range(num_cities) for k in depots) == 1

# Departure and Arrival at depots
for k in depots:
    prob += pulp.lpSum(x[(k, j, k)] for j in range(num_cities) if j != k) == 1
    prob += pulp.lpSum(x[(j, k, k)] for j in range(num_cities) if j != k) == 1

# Correct flow of arrivals and departures
for k in depots:
    for j in range(num_cities):
        if j != k:
            prob += pulp.lpSum(x[(i, j, k)] for i in range(num_cities)) == pulp.lpSum(x[(j, i, k)] for i in range(num_cities))

# Solve the problem
prob.solve()

# Extract the results
tours = {k: [] for k in depots}
for k in depots:
    next_city = k
    while True:
        tours[k].append(next_city)
        next_city_found = False
        for j in range(num_cities):
            if pulp.value(x[(next_city, j, k)]) == 1:
                next_city = j
                next_city_found = True
                break
        if not next_city_found or next_city == k:
            if next_city != k:
                tours[k].append(k)
            break

# Calculate the costs and display the results
total_cost = 0
for k in depots:
    tour_cost = sum(distance_matrix[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {totality}")