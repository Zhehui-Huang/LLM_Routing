import pulp as pl
import math

# Define cities and coordinates including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of cities
n = len(cities)

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Each robot starts and ends at its specific depot city
depots = {0: 0, 1: 1}  # Robot id and corresponding depot city

# Setup model
model = pl.LpProblem("Multiple_TSP_with_Depots", pl.LpMinimize)

# Travel decision variable x[i, j, k] where robot k travels from city i to city j
x = pl.LpVariable.dicts("x", [(i, j, k) for k in depots for i in cities for j in cities if i != j], 0, 1, pl.LpInteger)

# Objective function: Minimize the total distance
model += pl.lpSum(distance_matrix[i][j] * x[(i, j, k)] for k in depots for i in cities for j in cities if i != j)

# Constraints
# Each city must be visited exactly once by exactly one robot
for j in cities:
    if j not in depots.values():
        model += pl.lpSum(x[(i, j, k)] for k in depots for i in cities if i != j) == 1

# Maintain the flow for each robot, arrive at a city and leave it
for k, depot in depots.items():
    for i in cities:
        if i != depot:
            model += pl.lpSum(x[(i, j, k)] for j in cities if j != i) == pl.lpSum(x[(j, i, k)] for j in cities if j != i)

# Each robot must leave its depot and return to it
for k, depot in depots.items():
    model += pl.lpSum(x[(depot, j, k)] for j in cities if j != depot) == 1  # Leave depot
    model += pl.lpSum(x[(j, depot, k)] for j in cities if j != depot) == 1  # Return to depot

# Solve the problem
model.solve()

# Retrieve and display results
for k, depot in depots.items():
    current_city = depot
    tour = [depot]
    distance_covered = 0
    while True:
        next_city = [j for j in cities if j != current_city and pl.value(x[(current_city, j, k)]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        tour.append(next_city)
        distance_covered += distance_matrix[current_city][next_city]
        current_city = next_city
        if current_city == depot:
            break

    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {distance_covered}")

# Calculate the total cost of the tours
overall_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for k in depots for i in range(len(tour) - 1))
print(f"Overall Total Travel Cost: {overall_cost}")