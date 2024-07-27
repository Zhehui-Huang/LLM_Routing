import math
from itertools import combinations
from mip import Model, xsum, minimize, BINARY, OptimizationStatus

# Coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 53), (21, 21), (12, 39)
]

# Number of cities including the depot
n = len(cities)

# Calculate Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix
c = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create a new model
model = Model()

# Decision variables x_ij
x = [[model.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]

# Auxiliary variable for the longest distance
d = model.add_var()

# Objective function: minimize the longest single distance between two cities
model.objective = minimize(d)

# Constraints to ensure each city is entered and left once
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        model += xsum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Link d to the distances using x_ij
for i in range(n):
    for j in range(n):
        if i != j:
            model += d >= c[i][j] * x[i][j]

# Solve the model
model.optimize(max_seconds=300)

if model.status == OptimizationStatus.OPTIMAL:
    # Retrieve solution
    tour = [0]
    for _ in range(n-1):
        next_node = [j for j in range(n) if x[tour[-1]][j].x >= 0.99][0]
        tour.append(next_node)

    # Calculate total distance and maximum segment length
    total_dist = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_dist = max(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    
    tour.append(tour[0])  # return to the initial city to complete the loop
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_dist:.2f}")
    print(f"Maximum distance between consecutive cities: {max_dist:.2f}")
else:
    print(f"Optimal solution was not found. Status: {model.status}")