import pulp
import math

# Coordinates of the cities
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distance matrix
c = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Integer programming model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", c.keys(), cat=pulp.LpBinary)

# Objective function: minimize the total cost of the tour
model += pulp.lpSum(c[i, j] * x[i, j] for i, j in c.keys()), "Total Travel Cost"

# Constraints that ensure each city is left exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if (i, j) in x) == 1, f"Leave_{i}"

# Constraints that ensure each city is entered exactly once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if (i, j) in x) == 1, f"Enter_{j}"

# Solving the model
status = model.solve()
if status != pulp.LpStatusOptimal:
    print("Failed to solve the problem.")
    exit()

# Extracting the solution
tour = []
visited = [0]
i = 0

while len(tour) < n:
    for j in range(n):
        if (i, j) in x and pulp.value(x[i, j]) == 1:
            tour.append(j)
            i = j
            if j == 0:
                break
    if i == 0:
        break
    visited.append(i)

# Adding the depot to complete the cycle
tour.append(0)

# Calculating the total travel cost
total_cost = pulp.value(model.objective)

print("Tour:", tour)
print("Total travel cost:", total_cost)