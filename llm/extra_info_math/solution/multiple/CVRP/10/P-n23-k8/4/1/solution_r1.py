import pulp as pl
import math

# City coordinates and demands
city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64),
                    (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
                    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
                    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63),
                    (63, 69), (45, 35), (32, 39), (56, 37)]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14,
           6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robots information
robot_count = 8
capacity = 40

# Calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
n = len(city_coordinates)
distance_matrix = [[euclidean_distance(city_coordinates[i], city_coordinates[j]) for j in range(n)] for i in range(n)]

# Model
model = pl.LpProblem("CVRP", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts('x', ((r, i, j) for r in range(robot_count) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pl.lpSum(distance_matrix[i][j] * x[r, i, j] for r in range(robot_count) for i in range(n) for j in range(n) if i != j)

# Constraints
for j in range(1, n):
    model += pl.lpSum(x[r, i, j] for r in range(robot_count) for i in range(n) if i != j) == 1

for r in range(robot_count):
    model += pl.lpSum(x[r, 0, j] for j in range(1, n)) <= 1  # Leave depot
    model += pl.lpSum(x[r, j, 0] for j in range(1, n)) <= 1  # Return to depot
    for i in range(n):
        model += pl.lpSum(x[r, i, j] for j in range(n) if j != i) - pl.lpSum(x[r, j, i] for j in range(n) if j != i) == 0
    # Capacity constraints
    model += pl.lpSum(demands[j] * pl.lpSum(x[r, i, j] for i in range(n) if i != j) for j in range(1, n)) <= capacity

# Solve
status = model.solve()

# Output
if status == pl.LpStatusOptimal:
    total_cost = 0
    for r in range(robot_count):
        tour = [0]
        next_place = 0
        while True:
            next_places = [j for j in range(n) if pl.value(x[r, next_place, j]) == 1]
            if not next_places:
                break
            next_place = next_places[0]
            tour.append(next_place)

        if len(tour) > 1:
            print(f"Robot {r} Tour: {tour + [0]}")
            tour_cost = sum(distance_matrix[tour[k]][tour[k+1]] for k in range(len(tour) - 1))
            print(f"Robot {r} Total Travel Cost: {tour_cost}")
            total_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No optimal solution found. Status:", pl.LpStatus[status])