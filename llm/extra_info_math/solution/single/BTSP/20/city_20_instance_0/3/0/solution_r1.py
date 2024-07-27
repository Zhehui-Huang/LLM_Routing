from math import sqrt
import mip

# Cities coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Number of cities including the depot
n = len(cities)

# Function to calculate the Euclidean distance between cities
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Distances matrix
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Set up the optimization model
model = mip.Model()

# Variables: x[i, j] is 1 if edge (i, j) is part of the tour
x = [[model.add_var(var_type=mip.BINARY) for j in range(n)] for i in range(n)]

# Objective: Minimize the maximum distance in the tour
M = model.add_var()
model.objective = mip.minimize(M)

# Constraints:
# Each city must be entered and left exactly once
for i in range(n):
    model += mip.xsum(x[i][j] for j in range(n) if i != j) == 1
    model += mip.xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination (using Miller-Tucker-Zemlin formulation)
u = [model.add_var() for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i][j] <= n-1

# Connecting the maximum distance variable to the distances 
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[i][j] <= M

# Solving the model
model.optimize()

# Extract the tour from variables
tour = []
if model.num_solutions:
    for i in range(n):
        for j in range(n):
            if x[i][j].x >= 0.99:
                tour.append((i, j))
    
    # Ordering the tour starting from the depot
    ordered_tour = []
    current_city = 0
    visited = set()
    while len(ordered_tour) < len(tour):
        for trip in tour:
            if trip[0] == current_city and trip[1] not in visited:
                ordered_tour.append(trip[1])
                visited.add(trip[1])
                current_city = trip[1]
                break
    ordered_tour = [0] + ordered_tour + [0]
    
    # Calculating total cost and max distance
    total_cost = sum(distances[ordered_tour[i]][ordered_tour[i+1]] for i in range(len(ordered_tour) - 1))
    max_distance = max(distances[ordered_tour[i]][ordered_tour[i+1]] for i in range(len(ordered_tour) - 1))

    print(f"Tour: {ordered_tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")