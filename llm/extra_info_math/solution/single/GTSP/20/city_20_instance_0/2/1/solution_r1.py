import pulp
import math

# Define city coordinates
city_coords = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25),
    14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Define groups of cities
group_cities = {
    0: [1, 3, 5, 11, 13, 14, 19],
    1: [2, 6, 7, 8, 12, 15],
    2: [4, 9, 10, 16, 17, 18]
}

# City index for reference in the model
cities = list(city_coords.keys())

# Euclidean distance calculator
def distance(c1, c2):
    return math.sqrt((city_coords[c1][0] - city_coords[c2][0])**2 + (city_coords[c1][1] - city_coords[c2][1])**2)

# Initialize the LP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables x_ij: 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j),
                          cat=pulp.LpBinary)
# Determine selected cities from each group
selected = pulp.LpVariable.dicts("selected", ((g, j) for g in group_cities for j in group_cities[g]), cat=pulp.LpBinary)

# Objective: Minimize total distance
model += pulp.lpSum(distance(i, j) * x[i, j] for i in cities for j in cities if i != j)

# Constraints
# Ensure one outgoing connection per city and one incoming connection
for i in cities:
    model += pulp.lpSum(x[i, j] for j in cities if i != j) == pulp.lpSum(x[j, i] for j in cities if i != j)

# Each group should have exactly one city selected
for group in group_cities:
    model += pulp.lpSum(selected[group, j] for j in group_cities[group]) == 1

# Link x_ij to selected variable
for group in group_cities:
    for j in group_cities[group]:
        model += pulp.lpSum(x[i, j] for i in cities if i != j) >= selected[group, j]
        model += pulp.lpSum(x[j, i] for i in cities if i != j) >= selected[group, j]

# One outgoing and one incoming connection for chosen cities from each group
for group in group_cities:
    model += pulp.lpSum(x[j, i] for j in cities for i in group_cities[group] if i != j) == 1
    model += pulp.lpSum(x[i, j] for i in group_cities[group] for j in cities if i != j) == 1

# Subtour elimination
u = pulp.LpVariable.dicts("u", scope=(0, len(cities)-1), lowBound=0, upBound=len(cities)-1, cat=pulp.LpInteger)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + (len(cities) * x[i, j]) <= len(cities) - 1

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

# Retrieve the tour from the solution
tour = [0]
while len(tour) < 6:  # Including one city from each group and returning back
    next_cities = [j for j in cities if pulp.value(x[tour[-1], j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)

# Back to the depot
tour.append(0)
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")