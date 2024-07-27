import math
import pulp

# Coordinates of each city
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Groups of cities
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Helper function to compute Euclidean distance
def compute_distance(coor1, coor2):
    return math.sqrt((coor1[0] - coor2[0])**2 + (coor1[1] - coor2[1])**2)

# Building distance matrix
num_cities = len(coordinates)
distances = [[compute_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Prepare the problem
model = pulp.LpProblem("Minimize_Tour", pulp.LpMinimize)

# Variables x_ij where i, j are cities, x_ij = 1 if robot moves from city i to j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat="Binary") for i in range(num_cities) for j in range(num_cities) if i != j}

# Objective Function
model += pulp.lpSum(x[i, j] * distances[i][j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Adding Constraints

# Each group must connect exactly once externally
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in range(num_cities) if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in range(num_cities) if j not in group) == 1

# Flow conservation at each node
for i in range(num_cities):
    model += pulp.lpSum(x[i, j] for j in range(num_cities) if i != j) - pulp.lpSum(x[j, i] for j in range(num_cities) if i != j) == 0

# The problem is modeled and ready to solve
status = model.solve()
if status == pulp.LpStatusOptimal:
    print('A solution has been found.')
else:
    print('No optimal solution found.')

# Extracting tour and cost
tour = []
current_city = 0
visited = {0}
tour.append(0)
finished = False

while not finished:
    for j in range(num_cities):
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            tour.append(j)
            visited.add(j)
            current_city = j
            break
    if current_city == 0:
        finished = True

# Computing the total travel cost
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))