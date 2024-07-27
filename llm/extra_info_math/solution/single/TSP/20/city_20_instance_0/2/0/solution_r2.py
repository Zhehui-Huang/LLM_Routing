import pulp
import math

# Defined coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Number of cities including the depot
n = len(coordinates)

# Euclidean distance function
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Creating the cost matrix
cost_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the LP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
model += pulp.lpSum(cost_matrix[i][j] * x[(i, j)] for i in range(n) for j in range(n))

# Constraints
# Each city must be entered and left exactly once
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1, "leaving_city_%s" % i
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1, "entering_city_%s" % i

# Subtour prevention constraints
for l in range(2, n):
    for s in itertools.combinations(range(1, n), l):  # To avoid loop in the depot city
        model += pulp.lpSum(x[(i, j)] for i in s for j in s if i != j) <= len(s) - 1

# Solve the problem
model.solve()

# Extract the tour from the variables
tour = []
partial_tour = [0]  # Start at the depot
visited = [False] * n
current = 0
while not all(visited):
    for j in range(n):
        if x[(current, j)].varValue == 1 and not visited[j]:
            visited[current] = True
            partial_tour.append(j)
            current = j
            break
    if current == 0:
        break

# Include returning to the depot
partial_tour.append(0)

# Total distance of tour
total_distance = sum(cost_matrix[partial_tour[i]][partial_tour[i + 1]] for i in range(len(partial_tour) - 1))

# Output results
print(f"Tour: {partial_tour}")
print(f"Total travel cost: {total_distance:.2f}")