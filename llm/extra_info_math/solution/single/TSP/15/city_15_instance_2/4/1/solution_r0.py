import numpy as np
import pulp

# Coordinates of each city including the depot city (city 0)
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Number of cities including the depot
n = len(coordinates)

# Calculate Euclidean distance matrix
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

dist_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem formulation
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path from i to j is taken
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function: minimize the total traveled distance
prob += pulp.lpSum(dist_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints (SEC) - using Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem using a solver that handles integer programming
prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Parse solution
tour = []
for i in range(n):
    for j in range(n):
        if pulp.value(x[i, j]) == 1:
            tour.append(j)

# Make the tour start and end at 0
starting_city = 0
tour_index = tour.index(starting_city)  # Find where the depot city starts in the list
rearranged_tour = tour[tour_index:] + tour[:tour_index]  # Rearrange to start at the depot city
rearranged_tour.append(0)  # Add depot city to the end to complete the tour

# Calculate the total travel cost
total_cost = sum(dist_matrix[rearranged_tour[i]][rearranged_tour[i+1]] for i in range(len(rearranged_tour)-1))

# Output
print("Tour:", rearranged_tour)
print("Total travel cost:", round(total_cost, 2))