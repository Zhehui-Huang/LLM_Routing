import pulp
import math

# Coordinates of the cities (index 0 is the depot)
coordinates = [
    (84, 67),  # Depot
    (74, 40),
    (71, 13),
    (74, 82),
    (97, 28),
    (0, 31),
    (8, 62),
    (74, 56),
    (85, 71),
    (6, 76)
]

# Calculate Euclidean distance between pairs of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
  
n = len(coordinates)
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            cost_matrix[(i, j)] = float('inf')

# Setting up the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i,j] is 1 if we travel from i to j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour elimination constraints need to be formulated.
# Here, we add a rudimentary form of such constraints (more efficient methods exist for larger problems).

for i in range(n):
    for j in range(1, n):
        if i != j:
            prob += x[i, j] + x[j, i] <= 1

# Solve the problem
prob.solve()

# Interpret the output
tour = []
current = 0
visited = set([0])  # to avoid infinite loops if there's an error in solving
while True:
    tour.append(current)
    found_next = False
    for j in range(n):
        if pulp.value(x[current, j]) == 1:
            current = j
            if current in visited:
                break
            visited.add(current)
            found_next = True
            break
    if not found_next or current == 0:
        tour.append(0)  # Return to the depot
        break

# Calculate the total cost
total_cost = sum(cost_matrix[tour[k], tour[k + 1]] for k in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")