import numpy as np
import pulp

# Coordinates of the cities including the depot
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Number of cities
n = len(coordinates)

# Calculating the Euclidean distance between each city
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# PuLP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij (1 if the path from city i to city j is chosen, 0 otherwise)
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Maximum distance variable
z = pulp.LpVariable("z", lowBound=0, cat=pulp.LpContinuous)

# Objective function (Minimize the maximum distance between any two consecutive cities visited)
model += z

# Constraints to ensure each city is entered and left only once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i,j] <= n-1

# Constraint to keep z as the maximum distance between any two consecutive cities
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distance_matrix[i][j] <= z

# Solve the model
model.solve()

# If the model has an optimal solution, construct the tour from the results
if model.status == 1:  
    # Extract the tour
    path = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i,j]) == 1:
                path.append((i,j))

    # Start from the depot, find the route
    route = [0]
    last_location = 0
    while len(route) < n:
        next_move = next(move[1] for move in path if move[0] == last_location)
        route.append(next_move)
        last_location = next_move
    
    # Closing the tour by returning to the depot
    route.append(0)

    # Calculating the total travel cost and maximum distance
    total_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    max_distance = max(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

    print("Tour:", route)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("The model did not solve to optimality.")