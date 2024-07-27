import numpy as np
import pulp

# Define the cities' coordinates
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute the Euclidean distance between each pair of cities
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# PuLP model setup
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}") for i in range(n) for j in range(n)}
M = pulp.LpVariable("Max_distance", lowBound=0, cat=pulp.LpContinuous)

# Objective function
model += M

# Constraints
for i in range(n):
    model += sum(x[i, j] for j in range(n) if i != j) == 1  # Leaving each city
    model += sum(x[j, i] for j in range(n) if i != j) == 1  # Entering each city

# Subtour elimination constraints
for i in range(2, n):
    for S in itertools.combinations(range(1, n), i):
        model += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distance_matrix[i][j] <= M

# Solve TSP
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    # Extract solution
    tour = []
    visited = [0]
    current = 0
    
    while len(visited) < n:
        for j in range(n):
            if pulp.value(x[current, j]) == 1:
                tour.append((current, j))
                current = j
                visited.append(j)
                break
    tour.append((current, 0))  # Closing the tour to return to depot

    # Calculate cost metrics
    tour_path = [t[0] for t in tour] + [0]
    tour_length = sum(distance_matrix[tour[i][0]][tour[i][1]] for i in range(len(tour)))
    max_edge_length = max(distance_matrix[tour[i][0]][tour[i][1]] for i in range(len(tour)))

    # Output results
    print(f"Tour: {tour_path}")
    print(f"Total travel cost: {tour_length}")
    print(f"Maximum distance between consecutive cities: {max_edge nosPACE_length}")
else:
    print("No optimal solution found.")