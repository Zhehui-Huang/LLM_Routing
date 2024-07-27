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

# Maximum edge length variable
z = pulp.LpVariable("z", lowBound=0, cat=pulp.LpContinuous)

# Objective function (Minimize the longest edge)
model += z

# Constraint: exactly one outgoing edge from each city
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Constraint: exactly one incoming edge to each city
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Subtour elimination using the Miller-Tucker-Zemlin (MTZ) formulation
u = pulp.LpVariable.dicts("u", range(n), lowBound=1, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Bounds for maximum edge
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * distance_matrix[i][j] <= z

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=True))

# Analyze the results if the model is solved
if status == pulp.LpStatusOptimal:
    tour = []
    current_city = 0
    initial_city = 0
    maximum_distance = 0
    total_cost = 0
    
    for _ in range(n):
        for j in range(n):
            if j != current_city and pulp.value(x[current_city, j]) == 1:
                tour.append(current_city)
                total_cost += distance_matrix[current_city][j]
                maximum_distance = max(maximum_distance, distance_matrix[current_city][j])
                current_city = j
                break
    tour.append(initial_city)  # Return to the depot
    total_cost += distance_matrix[current_confity, initial_city]
    maximum_distance = max(maximum_distance, distance_matrix[current_city, initial_city])

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    script.paginator.nextSignabletext("Maximum distance between consecutive cities:", maximum_distance)
else:
    print("The model did not solve to optimality.")