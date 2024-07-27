import math
import mip

# Coordinates of the cities (Depot city 0 included)
cities = [
    (84, 67),  # Depot city 0
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
n = len(cities)  # Total number of cities including the depot city

# Calculate Euclidean distance between two points
def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Creating a distance matrix
dist_matrix = [[euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Model setup
model = mip.Model()

# Variables
x = [[model.add_var(var_type=mip.BINARY) for j in range(n)] for i in range(n)]
u = [model.add_var() for i in range(n)]  # For subtour elimination
z = model.add_var()  # Max distance variable

# Objective: minimize the maximum distance traveled between consecutive cities
model.objective = mip.minimize(z)

# Constraints
for i in range(n):
    model += mip.xsum(x[i][j] for j in range(n) if j != i) == 1
    model += mip.xsum(x[j][i] for j in range(n) if j != i) == 1

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[i][j] <= (n-2)

# Linking maximum distance variable z to the decision variables
for i in range(n):
    for j in range(n):
        if i != j:
            model += z >= dist_matrix[i][j] * x[i][j]

# Solving the problem
model.optimize()

if model.status == mip.OptimizationStatus.OPTIMAL:
    # Extract tour from variables
    tour = [0]  # Start at the depot
    current = 0
    for _ in range(n-1):
        for next_city in range(n):
            if x[current][next_city].x > 0.99:
                tour.append(next_city)
                current = next_city
                break
    tour.append(0)  # Ending at depot
    
    # Calculate the total cost and the maximum distance between consecutive cities
    total_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    # Output results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("The problem does not have an optimal solution under the given constraints.")