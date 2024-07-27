import math
import pulp

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Number of depots and robots
num_depots = 8  # Assuming first 8 cities are depots for fairness in robot distribution.
depots = list(range(num_depots))
robots = list(range(num_depots))  # Each robot starts from a depot, each depot has exactly one robot.

# Calculate distances between each pair of cities
distances = {}
for i in range(len(city_coords)):
    for j in range(len(city_coords)):
        if i != j:  # No self-loops
            distances[(i, j)] = euclidean_distance(city_coords[i], city_coords[j])

# Setup the optimization problem
prob = pulp.LpProblem("MDMTSP", pulp.LpMinimize)

# Variables: x[i, j] = 1 if travel from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(city_coords)) for j in range(len(city_coords)) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum([x[(i, j)] * distances[(i, j)] for i, j in distances])

# Constraints
# Each city is entered and left exactly once
for j in range(num_depots, len(city_coords)):  # Customer nodes not depot nodes
    prob += pulp.lpSum([x[(i, j)] for i in range(len(city_coords)) if i != j]) == 1
    prob += pulp.lpSum([x[(j, i)] for i in range(len(city_coords)) if i != j]) == 1

# Each robot leaves its depot
for d in depots:
    prob += pulp.lpSum([x[(d, j)] for j in range(len(city_coords)) if j != d]) == 1

# Each robot terminates at any city (but does not need to return to the depot)
for r in robots:
    prob += pulp.lpSum([x[(j, r)] for j in range(len(city_coords)) if j != r]) == 1

# Solve the problem
prob.solve()

# Output results
total_cost = 0

for r in robots:
    tour = [r]
    next_city = r
    tour_cost = 0

    while True:
        next_city = [j for j in range(len(city_coords)) if j != next_city and pulp.value(x[(next_city, j)]) == 1][0]
        tour.append(next_city)
        tour_cost += distances[(tour[-2], next_city)]
        if len(tour) > len(city_coords) - num_depots or next_city in depots:
            break
    
    print(f"Robot {r} Tour: {tour}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")