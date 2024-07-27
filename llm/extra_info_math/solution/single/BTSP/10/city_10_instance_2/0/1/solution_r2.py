import math
import pulp

# Coordinates of the 10 cities including the depot city 0
coordinates = [
    (90, 3),  # depot city 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Total number of cities
n = len(coordinates)

# Function to compute Euclidean distance between two points
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Set up the optimization model
model = pulp.LpProblem("Min_Max_Distance_TSP", pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if path from i to j is chosen
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), lowBound=0, upBound=1, cat='Binary')

# Auxiliary variable to minimize maximum distance traveled between two consecutive cities
max_dist = pulp.LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective function: minimize the maximum distance
model += max_dist

# Constraints
for i in range(n):
    # Each city must be left exactly once
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    
    # Each city must be entered exactly once
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Limit max_dist to the distance used in the connection
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distances[i][j] <= max_dist

# Solve the problem
model.solve()

# Extraction of the tour
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Organize tour to start and end with 0 (depot)
organized_tour = [0]
current_city = 0
while len(organized_tour) < n:
    for (i, j) in tour:
        if i == current_city:
            organized_tour.append(j)
            current_city = j
            break
organized_tour.append(0)  # back to depot

# Calculate the total cost and the maximum distance
total_cost = sum(distances[organized_tour[i]][organized_tour[i+1]] for i in range(len(organized_tour) - 1))
max_distance = max(distances[organized_tour[i]][organized_tour[i+1]] for i in range(len(organized_tour) - 1))

# Print results
print(f"Tour: {organized_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")