import math
import pulp

# City coordinates
coordinates = {
    0: (16, 90),  # depot
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Groups of cities (selection groups)
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance between pairs of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create all-points list of cities and a distance dictionary
n, V = len(coordinates), list(coordinates.keys())
c = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in V for j in V if i != j}

# Integer Programming Model
model = pulp.LpProblem("TSP_with_Groups", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", (c.keys()), cat='Binary')  # Travel selections
u = pulp.LpVariable.dicts("u", (range(2, len(groups) + 1)), lowBound=0)  # Help eliminate subtours

# Objective Function: Minimize total distance
model += pulp.lpSum(c[i, j] * x[i, j] for i, j in c), "Minimize_Distance"

# Each group must connect externally exactly once
for group_num, group in enumerate(groups, start=1):
    all_group_cities = [0] + group  # including depot city
    rest_cities = [city for city in V if city not in all_group_cities]
    
    # Outgoing from group
    model += pulp.lpSum(x[i, j] for i in group for j in rest_cities if (i, j) in x) == 1
    # Incoming to group
    model += pulp.lpSum(x[j, i] for i in group for j in rest_cities if (j, i) in x) == 1

# Subtour prevention constraints (Miller-Tucker-Zemlin)
for i in V:
    for j in V:
        if i != j and i != 0 and j != 0 and (i, j) in x:
            model += u[i] - u[j] + len(V) * x[i, j] <= len(V) - 1

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD())

# Retrieve the results
tour, total_cost = [0], 0
current_city = 0
while True:
    next_cities = [j for j in V if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    total_cost += c[current_city, next_city]
    current_city = next_city
    if current_city == 0:
        break

# Finish the tour by returning to the depot
if tour[-1] != 0:
    tour.append(0)
    total_cost += c[tour[-2], 0]

print("Tour:", tour)
print("Total travel cost:", total_cost)