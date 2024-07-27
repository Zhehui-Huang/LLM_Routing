from scipy.spatial.distance import euclidean
from itertools import product
from mip import Model, xsum, minimize, BINARY

# Step 1: Define city coordinates and groups
city_coords = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Step 2: Calculate distances
distances = {}
for i in city_coords:
    for j in city_coords:
        if i != j:
            distances[(i, j)] = euclidean(city_coords[i], city_coords[j])

# Step 3: Formulating the Problem
model = Model()

# a. Create variables
x = {(i, j): model.add_var(var_type=BINARY) for i, j in product(city_coords, city_coords) if i != j}

# b. Objective
model.objective = minimize(xsum(distances[i, j] * x[i, j] for i, j in distances))

# c. Constraints
# Each group must connect exactly once to an outside node
for group in groups:
    model += xsum(x[i, j] for i in group for j in city_coords if j not in group) == 1
    model += xsum(x[j, i] for i in group for j in city_coords if j not in group) == 1

# Flow conservation
for k in city_coords:
    model += xsum(x[i, k] for i in city_coords if i != k) == xsum(x[k, j] for j in city_coords if k != j)

# d. Preventing Subtours
u = {i: model.add_var() for i in city_coords if i != 0}  # Depot does not need a u variable
for i, j in product(city_coords, city_coords):
    if i != j and i != 0 and j != 0:
        model += u[i] - u[j] + (len(city_coords) - 1) * x[i, j] <= len(city emphasizes) - 2

# Step 4 & 5: Solving the problem and printing the solution
model.optimize()

# Constructing the output
tour = [0]  # start at depot
visited = set([0])
current = 0
while True:
    found = False
    for j in city_coords:
        if j != current and x[current, j].x >= 0.99 and j not in visited:  # because of floating-point issues, use a tolerance
            tour.append(j)
            visited.add(j)
            current = j
            found = True
            break
    if not found or current == 0:
        break
tour.append(0)  # return to depot

# Calculate total travel cost
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)