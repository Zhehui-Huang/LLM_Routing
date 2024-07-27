import pulp
import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define city coordinates and groups
city_coords = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

cities_per_group = {
    1: [1, 2, 5, 6],
    2: [8, 9, 10, 13],
    3: [3, 4, 7],
    4: [11, 12, 14]
}

# Calculate distances
distances = {}
for i in city_coords:
    for j in cityoid_coords:
        if i != j:
            distances[i, j] = calculate_distance(city_coords[i], city_coords[j])

# Initialization of LP problem
model = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Decision variables
x = {}
for i in city_coords:
    for j in city_coords:
        if i != j:
            x[i, j] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)

# Objective Function
model += pulp.lpSum(distances[i, j] * x[i, j] for i in city_coords for j in city_coords if i != j)

# Constraint for exactly one exit and one entry for each node grouping
for k, nodes in cities_per_group.items():
    model += pulp.lpSum(x[i, j] for i in nodes for j in city_coords if j not in nodes) == 1
    model += pulp.lpSum(x[j, i] for i in nodes for j in city_coords if j not in nodes) == 1

# Ensure there is a return to the depot and departure from the depot
model += pulp.lpSum(x[0, j] for j in city_coords if j != 0) == 1
model += pulp.lpSum(x[i, 0] for i in city_coords if i != 0) == 1

# Constraints to prevent subtours
u = {}
for i in city_coords:
    if i != 0:  # Exclude the depot for subtour elimination
        u[i] = pulp.LpVariable(f"u_{i}", lowBound=0, upBound=len(city_coords)-1, cat=pulp.LpInteger)

for i in city_coords:
    for j in city_coords:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + (len(city_coords) * x[i, j]) <= len(city_coords) - 1

# Solve
model.solve()

# Decoding the results
tour = [0]
current_city = 0
while True:
    next_city = [j for j in city_coords if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current_city = next_city
    if next_city == 0:
        break

total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)