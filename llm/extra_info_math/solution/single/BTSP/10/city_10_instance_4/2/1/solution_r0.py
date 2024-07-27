import pulp
import math
from itertools import combinations

# Define the coordinates of the cities
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}
n = len(cities)

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distance matrix
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Define the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Auxiliary variable for the maximum distance
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective: minimize the maximum distance
problem += max_distance

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"outgoing_from_{i}"
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"incoming_to_{i}"

# Subtour elimination
for s in range(2, n):
    for S in combinations(range(1, n), s):  # Consider subsets that don't include the depot
        problem += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Maximum distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[(i, j)] * distances[(i, j)] <= max_distance

# Solve the problem
status = problem.solve()
assert pulp.LpStatus[status] == 'Optimal', "No optimal solution found."

# Extract the tour
tour = [0]
current = 0
remaining = set(range(1, n))
while remaining:
    for j in range(n):
        if j in remaining and pulp.value(x[(current, j)]) == 1:
            tour.append(j)
            remaining.remove(j)
            current = j
            break
tour.append(0)  # return to depot

# Calculate tour cost and maximum distance
total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
max_dist = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_dist)