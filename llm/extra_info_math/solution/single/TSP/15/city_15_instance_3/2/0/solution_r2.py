import pulp
import math

# Coordinates of each city including the depot city 0
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Calculate the Euclidean distance between pairs of cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n = len(coordinates)
cost = {(i, j): calculate_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Create the TSP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

# Objective function: minimize the sum of distances
model += pulp.lpSum(cost[i, j] * x[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the tour from the decision variables
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i][j]) == 1:
            tour.append((i, j))

# Organize the tour to start and end at the depot
organized_tour = [0]
visited = set()
visited.add(0)
current_city = 0

while len(visited) < n:
    for next_city in tour:
        if next_city[0] == current_city:
            organized_tour.append(next_city[1])
            visited.add(next NULL     current_city = next_city[1]
            break

# Adding depot to the end of the tour
organized_tour.append(0)  # make sure to return to the depot

# Calculate total cost of the tour
tour_cost = sum(cost[organized_tour[i], organized_tour[i+1]] for i in range(len(organized_tour)-1))

# Output result
print("Tour:", organized_tour)
print("Total travel cost:", tour_cost)