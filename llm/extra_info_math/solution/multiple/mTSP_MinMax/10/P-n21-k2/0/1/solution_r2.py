from mip import Model, xsum, minimize, BINARY
import math

# Coordinates of the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(coordinates)  # Total number of nodes including depot
m = 2  # Number of robots

# Calculate the Euclidean distance between each pair of nodes
def euclidean_distance(city1, city2):
    return math.sqrt(
        (coordinates[city1][0] - coordinates[city2][0]) ** 2 + 
        (coordinates[city1][1] - coordinates[city2][1]) ** 2
    )

# Create model
model = Model()

# Variables: x[i, j, k] is 1 if robot k travels from city i to j
x = [[[model.add_var(var_type=BINARY) for k in range(m)] for j in range(n)] for i in range(n)]

# Objective: Minimize the maximum distance traveled by any robot
max_distance = model.add_var()
model.objective = minimize(max_distance)

# Constraints
# Every city must be visited exactly once by one robot
for j in range(1, n):
    model += xsum(x[i][j][k] for i in range(n) for k in range(m) if i != j) == 1

# Conservation of flow for robots
for k in range(m):
    for j in range(1, n):
        model += xsum(x[i][j][k] for i in range(n) if i != j) - xsum(x[j][i][k] for i in range(n) if i != j) == 0

# One entry and one exit from depot for each robot
for k in range(m):
    model += xsum(x[0][j][k] for j in range(1, n)) == 1
    model += xsum(x[j][0][k] for j in range(1, n)) == 1

# Set up maximum distance constraints
for k in range(m):
    model += xsum(x[i][j][k] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j) <= max_distance

# Optimize the model
model.optimize()

# Extract the solution
tours = []
for k in range(m):
    tour = [0]
    while True:
        next_city = next(j for j in range(n) if x[tour[-1]][j][k].x >= 0.99)
        if next_city == 0:
            break
        tour.append(next_city)
    tours.append(tour + [0])

# Calculate the costs
costs = [sum(euclidean_distance(tours[k][i], tours[k][i + 1]) for i in range(len(tours[k]) - 1)) for k in range(m)]
max_cost = max(costs)

# Output the results
for k in range(m):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")