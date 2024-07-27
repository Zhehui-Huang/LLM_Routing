import pulp as pl
import math

# Given data
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76),
}
representative_cities = [(0,), (7, 9), (1, 3), (4, 6), (8,), (5,), (2,)]

# Calculate Euclidean distances
def euclidean_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

distances = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# ILP Model
model = pl.LpProblem("TSP_Grouped_Cities", pl.LpMinimize)

# Create variables
x = pl.LpVariable.dicts("x", distances, 0, 1, pl.LpBinary)
u = pl.LpVariable.dicts("u", range(1, len(representative_cities)), 0, None)

# Objective function
model += pl.lpSum(distances[i, j] * x[i, j] for i, j in distances), "Total Cost"

# Constraints
for group in representative_cities:
    model += pl.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1, f"Outgoing_from_group_{group}"
    model += pl.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1, f"Incoming_to_group_{group}"

for i in cities:
    model += pl.lpSum(x[j, i] for j in cities if j != i) == pl.lpAdd(x[i, j] for j in cities if j != i), f"Flow_{i}"

# Subtour elimination
num_groups = len(representative_cities)
for p in range(1, num_groups):
    for q in range(1, num_groups):
        if p != q:
            model += u[p] - u[q] + num_groups * pl.lpSum(x[i, j] for i in representative_cities[p] for j in representative_cities[q]) \
                     + (num-2) * pl.lpSum(x[j, i] for i in representative_cities[p] for j in representative_cities[q]) <= num_groups - 1, f"SEC_{p}_{q}"

# Solve the model
status = model.solve()

# Collect results
tour = []
current_city = 0
visited = set()
while True:
    visited.add(current_city)
    tour.append(current_city)
    next_cities = [j for j in cities if x[current_city, j].varValue == 1]
    if not next_cities:
        break
    current_city = next_cities[0]
    if current_city in visited:
        break

tour.append(0)  # Return to depot
total_cost = pl.value(model.objective)

print("Tour:", tour)
print("Total travel cost:", total_cost)