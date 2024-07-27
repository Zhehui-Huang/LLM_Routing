import pulp as pl
import math

# Coordinates of each city including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of cities including depots
n = len(cities)

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = 0

# Define problem
model = pl.LpProblem("MDVRP", pl.LpMinimize)

# Variables: x[i, j, k] is 1 if robot k travels from city i to city j
x = pl.LpVariable.dicts("x", [(i, j, k) for k in range(2) for i in range(n) for j in range(n)], cat='Binary')

# Objective Function
model += pl.lpSum(x[i, j, k] * distance_matrix[i][j] for k in range(2) for i in range(n) for j in range(n)), "Total Travel Cost"

# Each city visited exactly once per robot 
for k in range(2):
    for j in range(n):
        if j != k:  # except depot itself
            model += pl.lpSum(x[i, j, k] for i in range(n) if i != j) == 1  # incoming
            model += pl.lpSum(x[j, i, k] for i in range(n) if i != j) == 1  # outgoing

# Coming back to start depot
for k in range(2):
    model += pl.lpSum(x[i, k, k] for i in range(n) if i != k) == 1  # can return back to the same depot

# Leaving start depot
for k in range(2):
    model += pl.lpSum(x[k, j, k] for j in range(n) if j != k) == 1  # can leave the same depot

# Solve the problem
model.solve()

# Output the results
overall_cost = 0
for k in range(2):
    city = k
    tour = [city]
    total_cost = 0
    while True:
        next_city = next(j for j in range(n) if pl.value(x[city, j, k]) == 1)
        if next_city == k:
            break
        total_cost += distance_matrix[city][next_city]
        tour.append(next_city)
        city = next_train_city
    tour.append(k)
    overall_cost += total_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")