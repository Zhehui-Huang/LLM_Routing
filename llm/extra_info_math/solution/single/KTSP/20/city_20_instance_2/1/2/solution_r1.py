import pulp
import math

# Coordinates of cities including the depot city at the first position
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities
n = len(coords)
# Number of cities to visit including the depot
k = 10
# Create a distance matrix
dist = [[euclidean distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Creating a linear programming problem
model = pulp.LpProblem('k-TSP', pulp.LpMinimize)

# Define variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                         cat=pulp.LpBinary)
y = pulp.LpVariable.dicts("y", (i for i in range(n)),
                         cat=pulp.LpBinary)

# Objective function to minimize total distance
model += pulp.lpSum(dist[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraint: k cities are visited exactly
model += pulp.lpSum(y[i] for i in range(n)) == k, "Visit_k_Cities"

# Constraints: enter and leave each city only if it's visited
for i in range(n):
    model += (pulp.lpSum(x[i, j] for j in range(n) if i != j) == y[i])
    model += (pulp.lpSum(x[j, i] for j in range(n) if i != j) == y[i])

# Solve the model
status = model.solve()

# Check if a valid solution is found
if status == pulp.LpStatusOptimal:
    print("A solution has been found.")
else:
    print("Failed to find a solution.")

# Extract the solution
tour = []
visited = []
for i in range(n):
    if y[i].varValue > 0.99:  # i is visited
        visited.append(i)

# Starting from the depot city
current = 0
for _ in range(k):
    next_city = next(j for j in visited if j != current and x[current, j].varValue > 0.99)
    tour.append(next_city)
    current = next_city

# Adding depot to complete the tour
tour.append(0)

# Calculate the total cost of the tour
total_cost = sum(dist[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output of the results
print("Tour:", tour)
print("Total travel cost:", total_cost)