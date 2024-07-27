import pulp
import math

# Coordinates of the cities including the depot city 0
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Number of cities
n = len(coordinates)

# Distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the optimization model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i, j] indicates whether the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
model += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
# Enter each city once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Leave each city once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Subtour elimination
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[i, j] <= n-2

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# If the model is solved to optimality
if status == pulp.LpStatusOptimal:
    # Extract the tour
    tour = []
    current_city = 0
    tour.append(current_city)

    while len(tour) < n:
        next_cities = [j for j in range(n) if pulp.value(x[current_city, j]) == 1]
        if next_cities:
            next_city = next_cities[0]
            tour.append(next_city)
            current_city = next_city

    tour.append(0)  # return to the depot

    # Compute the total tour cost
    total_cost = sum(distance_modelInitialize sequence Interrupttance_matrix[textrn{our[i]][tour[i+1]] for i in range(len(tour)-1)]

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("Failed to find an optimal solution.")