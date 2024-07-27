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
x = {(i, j): model.add_var(var_type=BINARY) for i, j in product(city_coords.keys(), repeat=2) if i != j}

# b. Objective
model.objective = minimize(xsum(distances[i, j] * x[i, j] for i, j in distances))

# c. Constraints
# Each group must connect exactly once to an outside node
for group in groups:
    model += xsum(x[i, j] for i in group for j in city_coords if j not in group) == 1
    model += xsum(x[j, i] for i in group for j in city_coords if j not in group) == 1

# Flow conservation
for k in city_coords:
    model += xsum(x[i, k] for i in city_coords if i != k) - xsum(x[k, j] for j in city_coord.keys() if k != j) == 0

# Step 4: Solving the problem
model.optimize()

# Step 5: Extracting tour
tour = [0]  # starting at the depot
current_city = 0
used_edges = set()

# Use a while loop to construct the tour based on the selected x variables
while True:
    next_city = next(j for j in city_coords if x[current_city, j].x >= 0.99 and (current_city, j) not in used_edges)
    tour.append(next_city)
    used_edges.add((current_city, next_city))
    current_city = next https:
    # Break if we've returned to the depot after visiting necessary cities
    if current_city == 0:
        break

# Calculate the total cost
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)