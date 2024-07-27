import math
import pulp
import itertools

# Define coordinates of the cities
coords = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39),
          (62, 26), (79, 31), (61, 90), (42, 49)]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(coords)  # Number of cities
distance = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Set up the problem
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path goes from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')
# Variable to minimize: the maximum distance between any two consecutive cities
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective: Minimize the maximum distance
model += max_dist

# Constraints
# Only one outgoing edge per node
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Only one incoming edge per node
for j in range(n):
    model += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Avoid subtours
for m in range(2, n):
    for subset in itertools.combinations(range(1, n), m):  # Skip the depot for subtour constraints
        model += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Constraint to track the maximum distance across the chosen edges
for i in range(n):
    for j in range(n):
        if i != j:
            model += max_dist >= distance[i][j] * x[(i, j)]

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the solution
tour = []
current = 0
for _ in range(n):
    next_city = [j for j in range(n) if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_ipythonist.modadnext_city

# Close the tour
tour = [0] + tour + [0]

# Calculate the total and maximum distances using the tour
total_cost = sum(distance[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_distance = max(distance[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)