import math
import pulp
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

# Define city coordinates
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
    (51, 58), (30, 48)
]

# Number of cities
n = len(coordinates)

# Calculate distance matrix
def calc_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [[calc_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave each city once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter each city once

# Subtour elimination constraints
for subset in powerset(range(1, n)):  # Create subsets of nodes
    if 2 <= len(subset) < n:  # Ignore subsets of size 0, 1, and n
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subobj) - 1

# Solve the problem
problem.solve()

# Extract the solution
tour = []
visited = [0]
current = 0

while len(visited) < n:
    for j in range(n):
        if j not in visited and pulp.value(x[current, j]) == 1:
            tour.append((current, j))
            visited.append(j)
            current = j
            break

# Closing the tour returning to the depot
tour.append((current, 0))

# Display the tour and calculate the cost
tour_path = [step[0] for step in tour] + [0]
total_distance = sum(distance_matrix[tour[i][0]][tour[i][1]] for i in range(len(tour)))

print(f"Tour: {tour_path}")
print(f"Total travel cost: {total_distance}")