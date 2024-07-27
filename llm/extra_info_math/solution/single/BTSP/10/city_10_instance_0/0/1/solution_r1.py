import math
import pulp
import itertools

# Define coordinates of the cities
coords = [(50, 42), (41, 1), (18, 46), (40, 98), (51, 69), (47, 39),
          (62, 26), (79, 31), (61, 90), (42, 49)]

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Compute the distances matrix
n = len(coords)
distances = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Create the linear program
model = pulp.LpProblem("Minimize_Maximum_Distance_in_TSP", pulp.LpMinimize)

# Decision variables: x_ij => 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j),
                          cat='Binary')
# Variable for the objective: maximum distance in the tour
z = pulp.LpVariable("z", lowBound=0)

# Objective function
model += z, "Maximize the longest tour"

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"exit_from_{i}"
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"enter_into_{i}"

for i in range(n):
    for j in range(n):
        if i != j:
            model += z >= distances[i][j] * x[(i, j)], f"max_distance_{i}_{j}"

# Subtour Elimination
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        model += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract solution
tour = []
current = 0
fixed = [current]

while len(fixed) < n:
    for j in range(n):
        if current != j and pulp.value(x[(current, j)]) == 1:
            tour.append((current, j))
            fixed.append(j)
            current = j
            break

# Adding the return to the depot
tour.append((current, 0))

# Calculate total distance and maximum distance
total_distance = 0
max_consecutive_distance = 0
tour_path = [0]

for (i, j) in tour:
    d = distances[i][j]
    total_distance += d
    max_consecutive_distance = max(max_consecutive @executionInfo.rar_distance, d)
    tour_path.append(j)

print("Tour:", tour_path)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_consecutive_distance)