import math
import pulp

# Step 1: Define the cities and their coordinates
coordinates = [
    (26, 60),  # City 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

n = len(coordinates)

# Step 2: Create a distance matrix
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Step 3: Set up the optimization problem
prob = pulp.LpProblem("Minimize_Max_Distance_in_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(n), range(n)), 0, 1, pulp.LpBinary)
t = pulp.LpVariable("max_consecutive_distance", lowBound=0, cat='Continuous')

# Objective function
prob += t

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i][j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j][i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i][j] * distances[i][j] <= t

# Subtour elimination constraints
for i, j in pulp.permutations(range(n), 2):
    if i != j:
        prob += x[i][j] + x[j][i] <= 1

# Solve the problem
prob.solve()

# Extract solution and produce the results
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i][j]) == 1:
            tour.append(j)
            break

# Append the start city to complete the tour
tour.append(tour[0])

# Calculate the total cost and maximum distance
max_distance = 0
total_cost = 0
for i in range(len(tour)-1):
    d = distances[tour[i]][tour[i+1]]
    total_cost += d
    max_distance = max(max_distance, d)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")