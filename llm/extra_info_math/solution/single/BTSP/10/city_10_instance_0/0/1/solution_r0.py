import math
import pulp

# Define coordinates of the cities
coords = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39),
          (62, 26), (79, 31), (61, 90), (42, 49)]

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Calculate distances between all pairs of cities
n = len(coords)
distances = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# ILP model
model = pulp.LpProblem("Minimize_Maximum_Distance_in_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')
z = pulp.LpVariable("z", lowBound=0)

# Objective
model += z

# Constraints
# Maximum distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            model += z >= distances[i][j] * x[(i, j)]

# Each city has exactly one departure
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Each city has exactly one arrival
for j in range(n):
     model += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1
 
# Subtour elimination
for s in range(2, n):
    for subset in itertools.combinations(range(1, n), s):
        model += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the tour
tour = []
current = 0
while True:
    tour.append(current)
    nexts = [j for j in range(n) if j != current and pulp.value(x[(current, j)]) == 1]
    if not nexts:
        break
    current = nexts[0]

tour.append(0)  # Return to the depot

# Calculate total and maximum distances
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)