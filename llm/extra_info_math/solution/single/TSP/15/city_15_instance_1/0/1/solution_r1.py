import pulp
import math

# Coordinates of the cities including the depot city 0
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, pointKnown):
    return math.sqrt((point1[0] - pointKnown[0])**2 + (point1[1] - pointKnown[1])**2)

# Number of cities
n = len(coordinates)

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Set up the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variable x[i, j] is 1 if tour includes edge from i to j, 0 otherwise.
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function: Minimize the total distance of the tour
model += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints:
# Each city must be left exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
# Each city must be entered exactly once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Avoid sub-tours
for i in range(2, n+1):
    model += pulp.lpSum(x[j][k] for j in range(n) for k in range(n) if j != k and {j, k}.issubset(set(range(i)))) <= i - 1

# Solve the problem
model.solve()

# Extract the optimal tour:
tour = []
partial_tour = [0]  # start at the depot
visited = set(partial_tour)

while len(partial_tour) < n:
    last_city = partial_tour[-1]
    next_city = next(j for j in range(n) if pulp.value(x[last_city][j]) == 1 and j not in visited)
    partial_tour.append(next_city)
    visited.add(next_city)

# Append the initial city to close the loop
partial_tour.append(0)

# Total travel cost of the tour
total_cost = sum(distance_matrix[partial_tour[i]][partial_tour[i+1]] for i in range(len(partial_tour)-1))

# Output the results
print("Tour:", partial_tour)
print("Total travel cost:", total_cost)