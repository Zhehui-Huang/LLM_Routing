import pulp as pl
import math

# Coordinates of each city including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots and their start/end depots
robots = {0: 0, 1: 1}
depots = [0, 1]

# Number of cities and depots
n = len(cities)
d = len(depots)

# Calculate distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Distance matrix
distance_matrix = {}
for i in range(n):
    distance_matrix[i] = {}
    for j in range(n):
        distance_matrix[i][j] = euclidean1000_distance(cities[i], cities[j])

# Initialize model
model = pl.LpProblem("Multiple_Depot_Multiple_Traveling_Salesman_Problem", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", [(i, j, k) for k in depots for i in range(n) for j in range(n)], cat='Binary')

# Objective function: Minimize the total distance traveled
model += pl.lpSum(distance_matrix[i][j] * x[(i, j, k)] for k in depots for i in range(n) for j in range(n)), "Total travel cost"

# Constraints
# Departure from depots and return to depots
for k in depots:
    model += pl.lpSum(x[(k, j, k)] for j in range(n) if j != k) == 1, f"Depart_from_depot_{k}"
    model += pl.lpSum(x[(j, k, k)] for j in range(n) if j != k) == 1, f"Return_to_depot_{k}"
    
# Each city visited exactly once
for j in range(n):
    if j not in depots:
        model += pl.lpSum(x[(i, j, k)] for k in depots for i in range(n) if i != j) == 1, f"Visit_city_{j}_exactly_once"

# Continuity of route
for k in depots:
    for i in range(n):
        if i != k:
            model += (pl.lpSum(x[(i, j, k)] for j in range(n) if j != i) == pl.lpSum(x[(j, i, k)] for j in range(n) if j != i)), f"Continuity_at_node_{i}_for_depot_{k}"

# Solve model
model.solve()

# Extract results
for k in robots:
    tour = [k]
    next_city = k
    while True:
        next_city = next(j for j in range(n) if pl.value(x[(next_city, j, k)]) == 1 and j != next_city)
        tour.append(next_city)
        if next_city == k:
            break
    print(f"Robot {k} Tour: {tour}")
    tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Total Travel Cost: {tour_cost}")