import pulp as lp
import itertools
import math

# Coordinates of the cities including the depot city
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Number of cities
n = len(coordinates)

# Create distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = lp.LpProblem("TSP", lp.LpMinimize)

# Create variables
x = lp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')
z = lp.LpVariable("z", lowBound=0)

# Objectives and constraints
problem += z, "Minimize the maximum distance"

for i in range(n):
    problem += lp.lpSum([x[(i, j)] for j in range(n) if i != j]) == 1
    problem += lp.lpSum([x[(j, i)] for j in range(n) if i != j]) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += distances[i][j] * x[(i, j)] <= z

for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):  # Avoid the depot for subtour constraints
        problem += lp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve()

# Extract solution
tour = []
for i in range(n):
    for j in range(n):
        if i != j and lp.value(x[(i, j)]) == 1:
            if not tour or tour[-1] == i:
                tour.append(j)

# Assuming the robot returns to the depot (necessary in TSP)
tour.append(tour[0])  

# Calculate the cost values
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the tour and travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")