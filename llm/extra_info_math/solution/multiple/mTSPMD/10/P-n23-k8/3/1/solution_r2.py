import pulp as pl
import math

# Define city coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Distance matrix calculation
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(city_coordinates)
distance_matrix = [[euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(n)] for i in range(n)]

# There are 8 robots, one per each of the first 8 depot cities
num_robots = 8
depot_indices = list(range(num_robots))

# Sets for cities and depots
cities = set(range(n))
depots = set(depot indices)

# Problem initialization
prob = pl.LpProblem("VRP", pl.LpMinimize)

# Variables: x[i, j, k]: 1 if robot k travels from city i to city j; route order variable u
x = pl.LpVariable.dicts("x", ((i, j, k) for k in depots for i in cities for j in cities if i != j), cat='Binary')
u = pl.LpVariable.dicts("u", (i for i in cities), lowBound=0, cat='Continuous')

# Objective: Minimize the total distance
prob += pl.lpSum(distance_matrix[i][j] * x[i, j, k] for k in depots for i in cities for j in cities if i != j), "Total Travel Cost"

# Constraints
# Each robot must start from its depot and return to it
for k in depot_indices:
    prob += pl.lpSum(x[k, j, k] for j in cities if j != k) == 1, f"Leave_depot_{k}"
    prob += pl.lpSum(x[j, k, k] for j in cities if j != k) == 1, f"Return_to_depot_{k}"

# Each city is visited exactly once by exactly one robot
for j in cities:
    prob += pl.lpSum(x[i, j, k] for k in depots for i in cities if i != j) == 1, f"One_visit_{j}"

# subtour elimination
for k in depot_indices:
    for i in cities:
        for j in cities:
            if i != j and (i != k or j not in depots):
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
prob.solve()

# Extract the routes from the decision variables
routes = {}
for k in depot_indices:
    route = [k]
    current_location = k
    while True:
        next_cities = [j for j in cities if pl.value(x[current_location, j, k]) == 1]
        if next_cities:
            next_location = next_cities[0]
            route.append(next_location)
            current_location = next_location
            if next_location == k:
                break
        else:
            break
    routes[k] = route

# Calculate the costs
total_cost = 0
for k, route in routes.items():
    cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    total_cost += cost
    print(f"Robot {k} Tour: {route}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")