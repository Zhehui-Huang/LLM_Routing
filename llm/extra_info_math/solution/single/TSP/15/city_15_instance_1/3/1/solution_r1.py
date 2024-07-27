import pulp
import math
import itertools

# Coordinate list of the cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create the distance matrix
n = len(coordinates)
cost = [[euclidean_factor(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the TSP problem
model = pulp.LpProblem(name="TSP", sense=pulp.LpMinimize)

# Variables: x[i, j] is 1 if the route goes from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective function: Minimize the total sum of distances
model += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
# Each city has one incoming connection
for i in range(n):
    model += pulp.lpSum(x[j][i] for j in range(n) if j != i) == 1, f"Incoming_{i}"

# Each city has one outgoing connection
for i in range(n):
    model += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1, f"Outgoing_{i}"

# Preventing subtours
for i in range(2, n):
    subsets = itertools.combinations(range(1, n), i)
    for subset in subsets:
        model += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = model.solve()

# Checking the status
if status == pulp.constants.LpStatusOptimal:
    tour = []
    for i in range(n):
        for j in range(n):
            # If this path is used in the optimal solution
            if pulp.value(x[i][j]) == 1:
                tour.append((i, j))

    # Reform the path according to the starting point at the depot (city 0)
    optimized_tour = []
    next_city = 0
    while len(optimized_tour) < n:
        for i, j in tour:
            if i == next_city:
                optimized_tour.append(i)
                next_city = j
                break
    optimized_tour.append(0)  # return to depot

    # Calculate the total travel cost using the optimized tour
    total_cost = sum(cost[optimized_tour[i]][optimized_tour[i+1]] for i in range(len(optimized_tour)-1))

    print("Tour:", optimized_tour)
    print("Total travel cost:", total_cost)
else:
    print("Failed to solve. Status:", status)