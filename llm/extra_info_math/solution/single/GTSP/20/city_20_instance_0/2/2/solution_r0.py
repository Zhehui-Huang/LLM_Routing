import pulp as pl
import math

# City coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Grouping of cities
city_groups = {
    "Group0": [1, 3, 5, 11, 13, 14, 19],
    "Group1": [2, 6, 7, 8, 12, 15],
    "Group2": [4, 9, 10, 16, 17, 18]
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Problem setup
model = pl.LpProblem("Robot_Tour_Optimization", pl.LpMinimize)

# Decision variables: x_ij
x = pl.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function
model += pl.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraints for maintaining exactly one city visit from each group
for name, group in city_groups.items():
    model += pl.lpSum(x[(0, j)] for j in group) == 1
    model += pl.lpSum(x[(j, 0)] for j in group) == 1
    for i in cities:
        if i not in group:
            model += pl.lpSum(x[(i, j)] for j in group) == pl.lpSum(x[(j, i)] for j in group)

# Flow conservation constraint
for i in cities:
    model += pl.lpSum(x[(j, i)] for j in cities if j != i) == pl.lpSum(x[(i, j)] for j in cities if j != i)

# Sub-tour elimination
u = pl.LpVariable.dicts('u', list(cities)[1:], lowBound=0, cat='Continuous')
k = len(cities)
for i in list(cities)[1:]:
    for j in list(cities)[1:]:
        if i != j:
            model += u[i] - u[j] + k * x[(i, j)] <= k - 1

# Solve problem
model.solve()

# Get the solution
tour = [0]
current = 0
while True:
    next_city = [j for j in cities if j != current and pl.value(x[(current, j)]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city
    if current == 0:
        break

# Travel cost
travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", travel_cost)