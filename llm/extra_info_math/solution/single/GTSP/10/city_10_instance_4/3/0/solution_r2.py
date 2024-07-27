from scipy.spatial.distance import euclidean
from mip import Model, xsum, minimize, BINARY
from itertools import product

# Step 1: Define city coordinates and groups
city_coords = {
    0: (79, 15), 
    1: (79, 55), 
    2: (4, 80), 
    3: (65, 26), 
    4: (92, 9),
    5: (83, 61), 
    6: (22, 21), 
    7: (97, 70), 
    8: (20, 99), 
    9: (66, 62)
}

groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Step 2: Calculate distances
distances = {(i, j): euclidean(city_coords[i], city_coords[j]) for i in city_coords for j in city_coords if i != j}

# Step 3: Formulating the Problem
model = Model()

# Variables
x = {(i, j): model.add_var(var_type=BINARY) for i in city_coords for j in city_coords if i != j}

# Objective: Minimize total travel cost
model.objective = minimize(xsum(distances[i, j] * x[i, j] for i, j in distances))

# Constraints
# In and out connections for each group
for group in groups:
    model += xsum(x[i, j] for i in group for j in city_coords if j not in group) == 1
    model += xsum(x[j, i] for j in group for i in city_coords if i not in group) == 1

# Flow conservation at each city
for k in city_coords:
    model += xsum(x[i, k] for i in city_coords if i != k) == xsum(x[k, j] for j in cityconfigs if k != j)

# Subtour prevention using additional constraints
u = {i: model.add_var() for i in city_coords if i != 0}
P = len(city_coords)
for i in city_coords:
    for j in city_coords:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + P * x[i, j] <= P - 1

# Solve the model
model.optimize()

# Extract the tour
tour = []
current = 0
next_visit = {i: j for i, j in product(city_coords, city_coords) if i != j and x[i, j].x >= 0.99}

# Start constructing the tour from the depot
while True:
    tour.append(current)
    current = next_visit.get(current, 0)
    if current == 0:
        tour.append(0)  # Return to depot
        break

# Calculate the cost of the tour
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Display the results
print("Tour:", tour)
print("Total travel cost:", total_cost)