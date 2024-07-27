import math
from mip import Model, xsum, maximize, BINARY

# Coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
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

# Objective function: minimize the maximum edge used
d = model.add_var()
model.objective = maximize(d)

# Constraints
for i in range(n):
    model += xsum(x[i][j] for j in range(n) if i != j) == 1
    model += xsum(x[j][i] for j in range(n) if i != j) == 1

# Subtour elimination
for s in range(2, n):
    for S in combinations(range(1, n), s):
        model += xsum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1

# Link distances
for i in range(n):
    for j in range(n):
        if i != j:
            model += d <= c[i][j] - (1 - x[i][j]) * max(max(c))

# Solve the model
model.optimize()

# Retrieve solution
tour = [0]
if model.num_solutions:
    for i in range(n):
        k = tour[-1]
        for j in range(n):
            if k != j and x[k][j].x >= 0.99:
                tour.append(j)
                break
    tour.append(0)  # Return to depot

# Calculate total distance and max segment length
total_dist = sum(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))
max_dist = max(c[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_dist:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")