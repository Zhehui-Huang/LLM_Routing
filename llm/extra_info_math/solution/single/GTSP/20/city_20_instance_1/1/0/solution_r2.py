import pulp
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Coordinates of the cities including depot
coordinates = [
    (14, 77),  # Depot city
    (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), (54, 82),
    (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],    # Group 0
    [1, 4, 8, 13, 16],    # Group 1
    [2, 10, 15, 18, 19],  # Group 2
    [3, 9, 12, 14]        # Group 3
]

# Setup the problem
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Create decision variables
x = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat=pulp.LpBinary)

# Objective Function: Minimize the distance traveled
model += pulp.lpSum(x[(i, j)] * euclidean_distance(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints to ensure each group exactly has one successor
for group in groups:
    model += sum(x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Constraints to ensure each group exactly has one predecessor
for group in groups:
    model += sum(x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group) == 1

# From the depot
model += sum(x[(0, j)] for j in range(1, len(coordinates))) == 1
# To the depot
model += sum(x[(j, 0)] for j in range(1, len(coordinates))) == 1

# Solve the problem
model.solve()

# Extract the tour by following the path from the starting node (depot: 0)
tour = []
next_city = 0
while True:
    tour.append(next_city)
    next_city = next(j for j in range(len(coordinates)) if x[(next_city, j)].varValue > 0.5)
    if next_city == 0:
        break

# Output the tour and calculate total travel cost
tour.append(0)
total_cost = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)