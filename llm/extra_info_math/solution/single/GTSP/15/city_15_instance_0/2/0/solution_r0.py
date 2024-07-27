import pulp
import math

# Coordinates for each city including depot
coordinates = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59),
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40),
    (3, 21), (60, 55), (4, 39)
]

# Groups of cities
groups = [
    [2, 7, 10, 11, 14],  # Group 0
    [1, 3, 5, 8, 13],    # Group 1
    [4, 6, 9, 12]        # Group 2
]

# Calculate Euclidean distance between pairs of cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities including the depot
n = len(coordinates)

# Create the distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Create the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if path from i to j is taken, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective Function: Minimize the total travel cost
prob += pulp.lpSum(distance_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints for the model
# Constraint to ensure exactly one city from each group is visited
for group in groups:
    prob += pulp.lpSum(x[0, j] for j in group) == 1  # From depot to exactly one in each group
    prob += pulp.lpSum(x[j, 0] for j in group) == 1  # From group to depot exactly once

# General flow conservation constraints for all other cities
for i in range(1, n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == pulp.lpSum(x[j, i] for j in range(n) if i != j)

# Solve the problem
prob.solve()

# Output 
if pulp.LpStatus[prob.status] == "Optimal":
    solution = [0]
    current_city = 0
    visited = set([0])
    while len(visited) < len(groups) + 1:
        for j in range(n):
            if j != current_city and pulp.value(x[current_city, j]) == 1:
                solution.append(j)
                visited.add(j)
                current_city = j
                break
    solution.append(0)  # end at the depot
    total_cost = sum(distance_matrix[solution[i], solution[i+1]] for i in range(len(solution)-1))
    print(f"Tour: {solution}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")